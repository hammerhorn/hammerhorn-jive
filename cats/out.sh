#!/bin/bash
if [ $# -eq 0 ]
   then
      echo "Usage: $0 [-v] filenames..." 1>&2
      exit 1
fi

if [ "$1" = "-v" ]
   then
      shift
      less -- "$@"
   else
      cat -- "$@"
fi
