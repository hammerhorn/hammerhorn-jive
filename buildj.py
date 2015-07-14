#!/usr/bin/env python
import os
import sys

command = 'gcj -c -g -O'
javafiles = ''
classfiles = ''
ofiles = ''

for arg in sys.argv[1:]:
    javafiles += ' {}.java'.format(arg)
    classfiles += ' {}.class'.format(arg)
    ofiles += ' {}.o'.format(arg)


def main():
    # Compile Java source.
    os.system('javac {} 2>&1 >/dev/null|more'.format(javafiles))

    # Compile to an executable, strip, and make executable.
    command += '{} && gcj --main={}'.format(classfiles, sys.argv[1])
    command += '{0} -o {1} && rm -f {0} && strip -s {1} && chmod +x {1}'.format(
        ofiles, sys.argv[1])
    os.system(command)

main()
# I don't remember how to make jar files
