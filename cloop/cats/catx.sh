#!/bin/bash
if [ $# -ne 0 ]; then
   x="$1"
   view $x
   echo
else
   clear
   while : ; do
      (echo -n `pwd`
      for((count=1; count<`pwd|wc -c`;count++)); do
         echo -ne "\b"
      done
      for((count=1; count<`pwd|wc -c`;count++)); do 
         echo -ne "_"
      done 
      echo ":") | ul

      ls --color --group -XF
      echo
      echo "Press ^C to exit."
      read x
      clear
      if [ -d  "$x" ]; then
         echo -e "\aERROR - $x is a directory.\n" 1>&2
      elif [ $(file $x | grep "[Tt]ext"|wc -l) -lt 1 ]; then
         echo -e "\aERROR - $x is a binary file.\n" 1>&2
      else
         (echo -n "$x"
         for((count=1; count<`echo "$x"|wc -c`;count++)); do
            echo -ne "\b"
         done
         for((count=1; count<`echo "$x"|wc -c`;count++)); do
            echo -ne "_"
         done
         echo ":")|ul
         echo -e "(`file "$x"|cut -d: -f2-|sed 's/^ //'`)\n"
#for((count=-2; count<`echo "$x"|wc -c`;count ++)); do
#   echo -n "="
#done
#echo
         if [ `cat $x | wc -l` -gt $((`tput lines` - 4)) ]; then
            (view `pwd`/$x | sed 's/^/>/'|| cat `pwd`/$x)| less -R
         else
            view `pwd`/$x || cat `pwd`/$x 
            echo -e "\n"
            echo "Press any key to continue, ^C to exit."
            read -n 1
         fi
         clear
      fi
   done
fi
