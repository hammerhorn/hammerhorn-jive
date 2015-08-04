#!/bin/bash

[[ -z $1 ]] && sides=6 || sides=$1 
echo $(( RANDOM % $sides + 1 ))
