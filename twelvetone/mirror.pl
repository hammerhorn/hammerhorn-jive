#!/usr/bin/perl
chomp(@lines = <STDIN>);
foreach (0..$#lines){
   @chars = split(' ', $lines[$_]);
   print join(" ", reverse (@chars)), "\n";
}
