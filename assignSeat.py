#!/usr/bin/python
import random
import sys
import secrets
import os
os.chdir(secrets.GPATH)
'''
Script to generate random seating pattern
usage: python assignSeat.py section
'''

COMPU_SIZE = 47
POPULATION = {"5": 45, "11": 45}
ROSTER = "./roster/section%s.csv"
OUTPUT = "./roster/seating%s.csv"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python assignSeat.py section"
        exit()
    sec_num = sys.argv[1]
    rand_num = random.sample(range(1, COMPU_SIZE), POPULATION[sec_num])
    with open(OUTPUT % sec_num, "w+") as f:
        for line in open(ROSTER % sec_num):
            f.write("%s,%d\n" % (line.rstrip(), rand_num.pop()))    
        while rand_num:
            f.write(",,,,,%s\n" % rand_num.pop())
