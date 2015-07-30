#!/bin/bash

[[ -z $1 ]] && sides=6 || sides=$1 
left=$(( RANDOM % $sides + 1 ))
right=$(( RANDOM % $sides + 1 )) 
sum=$((left + right))
echo "$sum = $left + $right"

