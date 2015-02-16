#!/usr/bin/python

'''
Script to compile all mfiles into html format
Execute all files from reports/, and generate html file into published/
'''

import re
import os
import shutil
import sys
from datetime import datetime, timedelta
import secrets
import shlex, subprocess
from utility import levelwalk

os.chdir(secrets.GPATH)
COPY_DIR = "./reports"
OUTPUT = "./published"
LOG = "./logs"

def main():
    args = ["matlab", "-nodisplay", "-nosplash", "-nodesktop", "-r"]
    command = "addpath('%s');publish('%s', 'format', 'html', 'outputDir', '%s');exit;"
    for root, dirs, files in levelwalk(COPY_DIR, 0):
        name = os.path.basename(root)
        for f in files:
            if f.endswith('.m'):
                print "========> %s, %s" % (root, f)
                output_dir = os.path.join(OUTPUT, name)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                logdir = os.path.join(LOG, name)
                if not os.path.exists(logdir):
                    os.makedirs(logdir)
                logfile = os.path.join(logdir, os.path.splitext(f)[0] + ".txt")
                # args.append(logfile)
                # args.append("-r")
                args.append(command % (root, os.path.join(root, f), output_dir))
                subprocess.call(args)
                #print args
                args.pop()

if __name__ == '__main__':
    main()