#!/usr/bin/perl

if ($#ARGV+1 != 4) {
    print "mL of first ingredient ";
    $vol1 = <STDIN>;
print '%ABV of first ingredient';
$solute1 = <STDIN>;
print "\n", "mL of second ingredient";
$vol2 = <STDIN>;
print '%ABV of second ingredient';
$solute2 = <STDIN>;
}

else {
    $vol1 = $ARGV[0];
    $solute1 = $ARGV[1];
    $vol2 = $ARGV[2];
    $solute2 = $ARGV[3];
}

$solute = ($solute1 * $vol1 + $solute2 * $vol2)/($vol1 + $vol2);
$vol = $vol1 + $vol2;
print "\npercent = $solute\%\nvolume = $vol mL\n\n"

