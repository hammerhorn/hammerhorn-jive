#!/bin/bash
# I need to figure out how to make this 
# work with multi-char patterns.

[[ -z $1 ]] && pattern='-' || pattern="$1"
for i in `seq 1 $(tput cols)`
  do
    echo -n "$pattern"
  done
