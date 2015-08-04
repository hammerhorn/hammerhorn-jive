#!/usr/bin/python
# Interface for Enumeration java class
# depends: Enum.class, Enumeration.class

import subprocess
import sys

command = "java Enum "

if len(sys.argv[1:]) > 0:
    for arg in sys.argv[1:]:
        command += arg + ' '

else:
    for line in sys.stdin:
        command += line[:len(line) - 1] + ' '

proc = subprocess.Popen(command, shell=True)
proc.wait()