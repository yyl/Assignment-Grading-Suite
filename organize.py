#!/usr/bin/python
'''
This script is used to move all valid reports and logs to proper place for grading.
Move all reports from reports/ to grading/
'''

import secrets
import utility
import os, sys
import shutil

OUTPUT = "grading"
LOG = "logs"
REPORT = "published"
os.chdir(secrets.GPATH)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    dst = sys.argv[1]
    '''
    # move log files
    logdir = os.path.join(OUTPUT, dst, "logs")
    utility.createIfNotExist(logdir)
    print logdir
    utility.movefiles(os.path.join(os.getcwd(), LOG), logdir, ".txt")
    '''
    # move reports
    reportdir = os.path.join(OUTPUT, dst, "reports")
    utility.createIfNotExist(reportdir)
    print reportdir
    utility.movefiles(os.path.join(os.getcwd(), REPORT), reportdir, ".html")
    # copy two rosters accordingly
    '''
    r5 = "5.csv"
    r11 = "11.csv"
    src5 = os.path.join(os.getcwd(), "rosters", r5)
    src11 = os.path.join(os.getcwd(), "rosters", r11)
    dst5 = os.path.join(os.getcwd(), OUTPUT, r5)
    dst11 = os.path.join(os.getcwd(), OUTPUT, r11)
    shutil.copyfile(r5, dst5)
    shutil.copyfile(r11, dst11)
    '''
