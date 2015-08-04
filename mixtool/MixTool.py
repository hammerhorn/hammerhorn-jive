#!/usr/bin/python

import sys;

# Calculate how much of 2 different solutions you need to 
#    combine to reach a target %ABV and volume.

# Use: MixTool.py $%ABV1 $%ABV2 $TARGET_%ABV $TARGET_VOLUME

# If no arguments are given, input is from stdin.  
# Pretty much a direct translation of MixTool.pl

if len(sys.argv[1:])==0 :
    abv1 = input("%ABV of first ingredient: ")

else :
    abv1 = float(sys.argv[1])

if len(sys.argv[1:]) < 2 : 
    abv2 = input("%ABV of second ingredient: ")

else :
    abv2 = float(sys.argv[2])

if len(sys.argv[1:]) < 3 :
    target_abv = input("Target %ABV: ")
    if (target_abv > abv1 and target_abv > abv2) or (target_abv < abv1 and target_abv < abv2) :
        sys.exit('Sorry, that\'s not possible.')

else : 
    target_abv = float(sys.argv[3])

if len(sys.argv[1:]) < 4 :
    target_vol = input("Target volume (fl. oz.): ")

else : 
    target_vol = float(sys.argv[4])

vol1 = target_vol * (target_abv - abv2) / (abv1 - abv2)
vol2 = target_vol - vol1

print "\nYou will need " + str(vol1) + " fl. oz. of the first ingredient (" + str(abv1) + "% ABV), and"
print "\t      " + str(vol2) + " fl. oz. of the second ingredient (" + str(abv2) + "% ABV).\n"
