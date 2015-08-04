#!/bin/bash

#import library, please check path
#source /usr/lib/simple_curses.sh
source /usr/local/lib/simple_curses.sh

#Then, you must create a "main" function:
main (){
    #your code here, you can add some windows, text...
    window "Unicode" "red" 15
    #append "What the fuck is wrong with this shit?"
    append_command "head -35 unicode.txt"
    endwin
}
#str = "$1"
#then, you can execute loop:
./unicode.jar -xp $1 $2 |grep '0x' > unicode.txt
main_loop 1


