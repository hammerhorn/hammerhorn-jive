#!/bin/bash
if [[ -z $1 ]]
   then read -p "filename: " filename
else
   filename="$*"
fi

clear
cat "$filename"
lines=$(wc -l "$filename"|cut -d' ' -f1) 
screenh=$(( $(tput lines) - 2 ))
for((n=lines; n<=screenh; n++))
{
  echo
}

#for i in $(seq "$lines" "$screenh")
#  do 
#    echo 
#  done  
