#!/usr/bin/perl

@tokens = split(' ', <STDIN>);

foreach (0..$#tokens){
#    print $tokens[$_], "->";
    $tokens[$_] += $ARGV[0];
#   print $tokens[$_], "\n";
}
print join(" ", (@tokens)), " ";
