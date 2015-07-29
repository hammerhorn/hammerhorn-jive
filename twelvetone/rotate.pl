#!/usr/bin/perl

@tokens = split(' ', <STDIN>);
@output = @tokens;

#print join(" ", @output), "\n";

foreach $count1 (1..$#tokens+1){
   foreach $count2 (0..$#tokens){
       if($tokens[$count2] == $count1){
	  $index = $count2;
          #print $count1, " is ", $index + 1, "th in the sequence.\n"; 
          $output[$count1-1] = $#tokens + 1 - $index;
#          print $index, " is the index of ", $count2, "\n";
       }
   }   
}

print join(" ", @output), "\n";
