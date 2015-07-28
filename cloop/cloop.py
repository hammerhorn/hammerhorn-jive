#!/usr/bin/env python
"""
Simple C "Interpreter"

User can test lines of C code, by inputting them and hitting ^D to compile and
run the code on the fly.
"""
import os
import subprocess
import sys

from cjh import cli


def main():
    """
    Preprocessor "include" statements are the only thing the interpreter
    remembers from previously-input commands.  ^C will discard all data, erase
    all data files, and end the program.
    """
    includes = '#include <stdio.h>\n'
    cli.Cli()
    try:
        while True:
            block = 'int main(int argc, char* argv[])\n{'
            cli.write('%')
            while True:
                try:
                    line = cli.Cli.input()
                    if line.startswith('#include'):
                        includes += line + '\n'
                    else:
                        block += line + '\n'

                except EOFError:
                    block += '\nreturn 0;}'
                    break
            try:
                file_ptr = open('./tmp.c', 'w')
                file_ptr.write(includes + '\n' + block)
            finally:
                file_ptr.close()

            compile_command = 'gcc ./tmp.c'

            return_val = subprocess.check_call(compile_command, shell=True)
            if return_val == 0:
                proc = subprocess.Popen('./a.out')
                proc.wait()

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
