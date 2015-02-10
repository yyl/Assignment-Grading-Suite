#!/usr/bin/python
'''
A set of programs that are often used.
'''
import os

# create the path to the folder if not exist
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# walk dir/files within given dir and level
def levelwalk(top, level):
    for dirpath, dirnames, filenames in os.walk(top):
        depth = os.path.relpath(dirpath, top).count(os.path.sep)
        if depth == level:
            yield dirpath, dirnames, filenames
            del dirnames

# move all files with given extension from src to dst
# the objective is to get rid of folders
def movefiles(src, dst, extension):
    createIfNotExist(dst)
    for root, dirs, files in levelwalk(src, 0):
        name = os.path.basename(root)
        for f in files:
            if f.endswith(extension):
                newfile = os.path.join(dst, name + "_" + f) 
                curfile = os.path.join(root, f)
                os.rename(curfile, newfile)

