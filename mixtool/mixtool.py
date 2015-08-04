#!/usr/bin/python

import sys
from cjh.shell import Cli

# Calculate how much of 2 different solutions you need to 
#    combine to reach a target %ABV and volume.

# Use: MixTool.py $%ABV1 $%ABV2 $TARGET_%ABV $TARGET_VOLUME

# If no arguments are given, input is from stdin.  
# Pretty much a direct translation of MixTool.pl

if len(sys.argv[1:])==0 :
    abv1 = Cli.input("%ABV of first ingredient: ")

else :
    abv1 = sys.argv[1]
abv1 = float(abv1)

if len(sys.argv[1:]) < 2 : 
    abv2 = Cli.input("%ABV of second ingredient: ")

else :
    abv2 = sys.argv[2]
abv2 = float(abv2)

print('')


if len(sys.argv[1:]) < 3 :
    target_abv = Cli.input("Target %ABV: ")

else : 
    target_abv = sys.argv[3]
target_abv = float(target_abv)

if (target_abv < abv1 and target_abv < abv2) or (target_abv > abv1 and target_abv > abv2) : 
   print "Sorry, that's not possible."
   sys.exit(0)
   
if len(sys.argv[1:]) < 4 :
   target_vol = eval(Cli.input("Target volume (fl. oz.): "))

else : 
   target_vol = float(sys.argv[4])
   #target_vol = float(target_vol)

vol1 = target_vol * (target_abv - abv2) / (abv1 - abv2)
vol2 = target_vol - vol1 

print("\nYou will need {} fl. oz. of the first ingredient ({}% ABV), and".format(vol1, abv1))
print("\t      {} fl. oz. of the second ingredient ({}% ABV).\n".format(vol2, abv2))
