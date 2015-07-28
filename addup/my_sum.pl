#!/usr/bin/perl

foreach $argnum (0..$#ARGV ){
   $sum += $ARGV[$argnum]; 
}

print $sum, "\n"
