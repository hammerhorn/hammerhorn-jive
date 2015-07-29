#!/bin/bash
# cat, with bold text

tput bold
cat $@
tput sgr0
