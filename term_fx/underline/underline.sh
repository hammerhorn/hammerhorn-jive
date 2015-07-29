#!/bin/bash

#( 

set `xargs`
#for count in "$@"

underline=`tput smul`
nounderline=`tput rmul`

#l-n "$*"

#do
#echo "$count"
#done
#echo "`echo $x|wc -c` characters"

#for((count=1;count<`echo "$*"|wc -c`;count++)); do
#   echo -ne "\b"
#done
#for((count=1;count<`echo "$*"|wc -c`;count++)); do
#   echo -ne "_"
#done
#)|ul

echo "${underline}$*${nounderline}"
