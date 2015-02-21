#!/usr/bin/python
import random
import sys
import secrets
import os
os.chdir(secrets.GPATH)

COMPU_SIZE = 45
POPULATION = 43
ROSTER = "./roster/section%s.csv"
OUTPUT = "./roster/seating%s.csv"

if __name__ == "__main__":
	if len(sys.argv) == 2:
		exit()
	sec_num = sys.argv[1]
	rand_num = random.sample(range(1, COMPU_SIZE), POPULATION)
	with open(OUTPUT % sec_num, "a+") as f:
		for line in open(ROSTER % sec_num):
			f.write("%s,%d\n" % (line.rstrip(), rand_num.pop()))
		while rand_num:
			f.write(",,,,,%s\n" % rand_num.pop())