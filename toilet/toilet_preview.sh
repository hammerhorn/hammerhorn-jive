#!/bin/bash

clear
while :
  do
    echo
    ls --hide=*.flc /usr/share/figlet
    echo
    phrase="$@"
    test `printf "%s" $phrase | wc -c` -gt 0 || phrase="Hello!"
    read -e -p "Font:" figlet_font;
    printf '\n'
    toilet --gay -f $figlet_font "$phrase"
    printf '\n'
done
