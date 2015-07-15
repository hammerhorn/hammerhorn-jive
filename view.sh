#!/bin/bash
if [[ -z $1 ]]
   then read -p "filename: " filename
else
   filename=$@
fi

clear
cat "$filename"
for i in $(seq `cat "$filename"|wc -l` $(expr `tput lines` - 2) ); do 
   echo 
   done  
