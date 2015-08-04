#!/bin/bash
for x in "$@"                                                                                        
  do
    hr
    echo "$x:"
    for (( count=0; count<=`echo $x|wc -c`; count++ ))
      do
        echo -n "="
      done
    echo
#    pygmentize $x
    cat $x
  done  | less -R
