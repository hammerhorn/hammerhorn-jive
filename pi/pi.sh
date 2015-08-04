#!/bin/sh
# returns pi or pi times a number

if [ $# -ne 0 ] 
then 
   echo "3.14159265358979323846 * $1"|bc -l
else
   echo 3.14159265358979323846
fi
