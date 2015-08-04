import java.util.*;

public class ThingTest {
    public static void main(String[] args) {

	ArrayList<Thing> things = new ArrayList<Thing>();
        ArrayList<String> LabelPile;

	String[] MenuOptions = { "Add a [Thing] to your pile.",
	                         "View your pile.",
                                 "Discard a [Thing].", 
	                         "Exit" };

        NumMenu MainMenu = new NumMenu(MenuOptions);

        System.out.print(TuiTeX.box("Things"));

        while(true){			
	    switch(MainMenu.getSelection(true)){

                case 1:
    	            things.add(new Thing());
                    break;		    		

	        case 2:
                    LabelPile = new ArrayList<String>();
	            for(int x = 0; x < things.size(); x++) LabelPile.add(TuiTeX.emph(things.get(x).label));
	  	    TuiTeX.enumerate("Inventory", LabelPile);	
                    break;
	       
                case 3:
                    LabelPile = new ArrayList<String>();
	            for(int x = 0; x < things.size(); x++) LabelPile.add(TuiTeX.emph(things.get(x).label));
                    NumMenu DiscardMenu = new NumMenu(LabelPile, "Choose a [Thing] to Discard: ");
                    things.remove(DiscardMenu.getSelection(true) - 1);
		    break;

                case 4:
	 	    System.exit(1);
                                 
	        default:
	   }
	   TuiTeX.vspace();
        }
    }
}
