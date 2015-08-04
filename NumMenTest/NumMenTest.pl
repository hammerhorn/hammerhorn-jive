#!/usr/bin/perl

#
#if($#ARGV+1 > 0){
#    system("java NumMenTest " . "@ARGV");
#}
#
#else{
#    chomp(@items = <STDIN>);
#    print "java NumMenTest " . "@items";
#}



foreach (<>) {
    print ">";
    chomp;
    print "> $_\n";
}

print ">\n";

