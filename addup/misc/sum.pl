#!/usr/bin/perl

foreach $argnum (0..$#ARGV ){
   $sum += $ARGV[$argnum]; 
}

print sprintf("%.1f",$sum), "\n"
