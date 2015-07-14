#!/usr/bin/env python
"""
Simple C "Interpreter"

User can test lines of C code, by inputting them and hitting ^D to compile and
run the code on the fly.
"""
import argparse
import os
import subprocess
import sys

from cjh import cli


def _parse_args():
    """
    Parse arguments.
    """
    parser = argparse.ArgumentParser(description='Interactive Code Runner')
    parser.add_argument(
        '--cpp', action='store_true', help='set language to C++')
    parser.add_argument(
        '--f90', action='store_true', help='set language to Fortran 90')
    if __name__ == '__main__':
        return parser.parse_args()
    else:
        return  None

ARGS = _parse_args()

def main():
    """
    Preprocessor "include" statements are the only thing the interpreter
    remembers from previously-input commands.  ^C will discard all data, erase
    all data files, and end the program.
    """
    if ARGS.f90:
        if ARGS.cpp:
            sys.exit('Please choose one language.\n')
        else:
            includes = ''           
    elif ARGS.cpp:
        includes = '#include <iostream>\n'
    else:
        includes = '#include <stdio.h>\n'

    cli.Cli()
    try:
        while True:
            if ARGS.f90:
                block = 'PROGRAM Interactive\nIMPLICIT NONE\n'
            else:
                if ARGS.cpp:
                    block = 'using namespace std;'
                else:
                    block = ''
                block += 'int main(int argc, char* argv[])\n{\n'

            if ARGS.f90:
                prompt = '+'
            elif ARGS.cpp:
                prompt = '%%'
            else:
                prompt = '%'

            cli.write(prompt)
            while True:
                try:
                    line = cli.Cli.input('')
                    if line.startswith('#include'):
                        includes += line + '\n'
                    else:
                        block += ('\t' + line + '\n')

                except EOFError:
                    if ARGS.f90:
                        block += 'END PROGRAM Interactive'
                    else:
                        block += '\n\treturn 0;\n}'
                    break

            if ARGS.cpp:
                filename = './tmp.cpp'
            elif ARGS.f90:
                filename = './tmp.f90'
            else:
                filename = './tmp.c'

            try:
                file_ptr = open(filename, 'w')
                file_ptr.write(includes + '\n' + block)
            finally:
                file_ptr.close()

            if ARGS.f90:
                command = 'gfortran ./tmp.f90'
            elif ARGS.cpp:
                command = 'g++ ./tmp.cpp'
            else:
                if "math.h" in includes:
                    command = 'gcc -lm ./tmp.c'
                else:
                    command = 'tcc ./tmp.c'

            return_val = subprocess.check_call(command, shell=True)
            if return_val == 0:

                # There is probably a better way 
                # than having to run the code twice....
                #proc = subprocess.Popen('./a.out', shell=True)
                #proc.wait()
                output = subprocess.check_output('./a.out', shell=True)
                if not output.endswith('\n'):
                    print('\033[7m\033[1m%\033[0m')

    except KeyboardInterrupt:
        sys.stdout.write('\b\b\b')
        sys.stdout.flush()
        try:
            os.remove('./tmp.c')
        except OSError:
            pass
        try:
            os.remove('./a.out')
        except OSError:
            pass

if __name__ == '__main__':
    main()
