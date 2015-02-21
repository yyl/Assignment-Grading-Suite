#!/usr/bin/python

'''
This script is used to select only assignments of students that met requirements
Select qualified folders from submissions/ and copy into reports/
Usage: python script.py section date(MMDD)
'''
import re
from collections import defaultdict
import os
import shutil
import sys
from datetime import datetime, timedelta
import secrets
from utility import levelwalk

os.chdir(secrets.GPATH)
REPORT_DIR = "./submissions"
COPY_DIR = "./codes"

# return roster hashmap
def getRosterHash(path):
    return dict((line.rstrip().rstrip(","), True) for line in open(path))

# collect valid reports
def collect(roster, duetime):
    max_delay = timedelta(days=2)
    duetime = datetime.strptime(duetime, "%Y%m%d_%I%M%p")
    count = 0
    for root, dirs, files in levelwalk(REPORT_DIR, 1):
        ## check if it is my student
        ## skip it if not
        name = os.path.basename(root)
        match = re.search(r'\((.+)\)', name)
        if match:
            if not roster.get(match.group(1), False):
                continue
            netid = match.group(1)
        ## check if he has valid report
        ## copy the report if it is
        sub_dates = []
        for sub in dirs:
            match = re.search(r'(^[\d_AMPM]+)', sub)
            if match:
                cur_date = datetime.strptime(match.group(1), "%Y%m%d_%I%M%p")
                sub_dates.append((sub, cur_date))
        chose_sub = None
        for sub, date in sub_dates:
            if date <= max_delay + duetime:
                chose_sub = sub
            else:
                break
        if chose_sub:
            count += 1
            if not os.path.exists(os.path.join(COPY_DIR, netid)):
                shutil.copytree(os.path.join(root, chose_sub), 
                                os.path.join(COPY_DIR, netid))
    print "%d set of codes collected." % count

if __name__ == '__main__':
    if len(sys.argv) != 3: exit()
    section = sys.argv[1]
    date = sys.argv[2]
    roster = getRosterHash("./roster/%s.csv" % section)
    collect(roster, "2015%s_0700PM" % date)
