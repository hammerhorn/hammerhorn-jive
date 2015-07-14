#!/bin/bash

for i in *
  do
    if (grep "$1" "$i" > /dev/null)
      then
        echo -n "$i"|~/bin/ulcat.sh
        echo ": "
        nl "$i"| grep --color "$1"
    fi
  done
