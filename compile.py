#!/usr/bin/python

'''
Script to pre-check before generating reports:
1. any file missing?
'''

import re
import os
import shutil
import sys
from datetime import datetime, timedelta
import secrets
import shlex, subprocess

os.chdir(secrets.GPATH)
COPY_DIR = "./test"
OUTPUT = "./published"

# walk dir/files within given dir and level
def levelwalk(top, level):
    for dirpath, dirnames, filenames in os.walk(top):
        depth = os.path.relpath(dirpath, top).count(os.path.sep)
        if depth == level:
            yield dirpath, dirnames, filenames
            del dirnames

def main():
    args = ["matlab", "-nodisplay", "-nosplash", "-nodesktop", "-r"]
    command = "addpath('%s');publish('%s', 'format', 'html', 'outputDir', '%s');exit;"
    for root, dirs, files in levelwalk(COPY_DIR, 0):
        name = os.path.basename(root)
        for f in files:
            if f.endswith('.m'):
                print name, f
                output_dir = os.path.join(OUTPUT, name)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                args.append(command % (root, os.path.join(root, f), output_dir))
                subprocess.call(args)
                args.pop()

if __name__ == '__main__':
    main()
