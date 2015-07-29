#!/bin/bash

while :
  do
    clear 
    ls /usr/share/cowsay/cows
    echo
    read -p "Character:" COW
    echo
    clear

    [[ -z $1 ]] && 
      (fortune -a|cowsay -f $COW
       printf "\n\n\nPress 'q' to return to cow list...\n") | less || 
      (echo "$@" | cowsay -f $COW 
       printf "\n\n\nPress 'q' to return to cow list...\n") | less
done
