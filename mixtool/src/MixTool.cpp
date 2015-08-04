#include <iostream>
//#!/usr/bin/perl
//# Calculate how much of 2 different solutions you need to 
//#    combine to reach a target %ABV and volume.
//# Use: MixTool.pl $%ABV1 $%ABV2 $TARGET_%ABV $TARGET_VOLUME
//# If no arguments are given, input is from stdin. 
//

int main(int argc, char* argv[])
{
  double abv1,
    abv2,
    target_abv,
    target_volume,
    vol1,
    vol2;


  cout << "%ABV of first ingredient: ";

}
//if ($#ARGV+1==0) {
//   print '%ABV of first ingredient: ';
//   chomp($ABV1 = <STDIN>);
//}
//
//else {
//   $ABV1 = $ARGV[0];
//}
//
//if ($#ARGV+1 < 2) {
//   print '%ABV of second ingredient: ';
//   chomp($ABV2 = <STDIN>);
//}
//
//else {
//   $ABV2 = $ARGV[1];
//}
//
//if ($#ARGV+1 < 3) {
//   print 'Target %ABV: ';
//   $targetABV = <STDIN>;
//}
//
//else {
//    $targetABV = $ARGV[2];
//}
//    
//if ($#ARGV+1 < 4) {
//   print 'Target volume (fl. oz.): ';
//   $target_volume = <STDIN>;
//}
//
//else {
//   $target_volume = $ARGV[3];
//}
//
//$vol1 = $target_volume * ($targetABV - $ABV2) / ($ABV1 - $ABV2);
//$vol2 = $target_volume - $vol1;
//
//print "\nYou will need ", sprintf ("%.1f",$vol1) , " fl. oz. of the first ingredient (", $ABV1, "\% ABV), and";
//print "\n              ", sprintf("%.1f",$vol2), " fl. oz. of the second ingredient (", $ABV2, "\% ABV).\n\n"; 
