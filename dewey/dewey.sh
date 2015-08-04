#!/bin/bash

#if [ $# -gt 0 ]
#  then
#    call_number=$1
#  else
#    call_number=0
#  fi

[ -z $1 ] && call_number=0 || call_number=$1



while [ "$keypress" != ';' ]
  do
#    echo "Call number = $call_number"
#    read x
    clear
    echo -e "\tl/h) +/-\tj/k) +/-10\ti/u) +/-100\t;) quit\n"
    java CallNumTest $call_number -t | sed 's/^/\t/' # Because of an error in one of my java classes,
    read -n 1 keypress                               #          -t must go at the end.

    case "$keypress" in 
      l)
        [ $call_number -lt 999 ] && ((call_number++))
        ;;
      h)
        [ $call_number -gt 0 ] && ((call_number--))
        ;;
      j)
        [ $call_number -lt 990 ] && ((call_number+=10))
        ;;
      k)
        [ $call_number -gt 9 ] && ((call_number-=10))
        ;;
      u)
        [ $call_number -gt 99 ] && ((call_number-=100))
        ;;
      i)
        [ $call_number -lt 900 ] && ((call_number+=100))
        ;;
      \;)
        echo
        ;;
      *)
        ;;
      esac
  done

