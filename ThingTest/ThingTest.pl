#!/usr/bin/perl

#import java.util.*;
#
#public class ThingTest
#{
#    public static void main(String[] args)
#    {
#        System.out.print(TuiTeX.box("Things"));
system(qq(java mybanner "Things"));
#
#	ArrayList<Thing> things = new ArrayList<Thing>();
#
#	ArrayList<String> options = new ArrayList<String>();
$options[0] = "Add a [Thing] to your pile.";
$options[1] = "View your pile.";
$options[2] = "Exit";

#	options.add("Add a [Thing] to your pile.");
#	options.add("View your pile.");
#	options.add("Exit");
#
#        NumMenu menu = new NumMenu(options);
#
#        while(true){			
#	    switch(menu.getSelection()){
#
#            case 1:
#	       things.add(new Thing());
#               break;		    		
#
#	    case 2:
#	       ArrayList<String> LabelPile = new ArrayList<String>();
#	       for(int x = 0; x < things.size(); x++){
#	           LabelPile.add(TuiTeX.emph(things.get(x).getLabel()));
#
#	  	} 
#	       TuiTeX.enumerate("Inventory", LabelPile);	
#   break;
#	       
#
#            case 3:
#		System.exit(1);
#                break;
#             
#
#	      
#	       default:
#	    }
#	    TuiTeX.vspace();
#        }
#    }
#}
