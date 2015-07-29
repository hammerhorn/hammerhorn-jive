#!/usr/bin/python
import sys;

sum = 0;

for x in range(1, len(sys.argv)):
  sum = sum + float(sys.argv[x]);
print sum
