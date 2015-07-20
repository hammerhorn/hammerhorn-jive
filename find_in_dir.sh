#!/bin/bash

for i in *
  do
    if [[ -d "$i" ]]
      then :
    
    elif grep "$1" "$i" > /dev/null
      then
        echo -n "$i"| bin/ulcat.sh
        echo ": "
        #nl "$i"| grep --color "$1"
        grep -n --color "$1" "$i"
        echo
    fi
  done
