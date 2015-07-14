#!/bin/bash
clear
cat $@
for i in $(seq `cat $@|wc -l` $(expr `tput lines` - 2) ); do 
   echo 
   done  
