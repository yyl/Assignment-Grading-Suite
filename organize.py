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
REPORT = "published"
os.chdir(secrets.GPATH)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit()
    dst = sys.argv[1]
    # move reports
    reportdir = os.path.join(OUTPUT, dst, "reports")
    utility.createIfNotExist(reportdir)
    print "moving gradable reports to %s" % reportdir
    utility.movefiles(os.path.join(os.getcwd(), REPORT), reportdir, ".pdf")