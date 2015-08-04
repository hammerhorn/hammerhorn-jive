#!/usr/bin/perl
print "\ndiameter(in.)?";
$diameter = <STDIN>;

print "price(\$)?";
$price = <STDIN>;

printf "\$%.2f/sq in\n\n", ($price /(($diameter/2)**2 * 3.14159265358979323846));
