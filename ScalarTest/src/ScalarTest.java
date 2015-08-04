import java.util.*;

public class ScalarTest{
    public static void main(String[] args){
        System.out.print(TuiTeX.box("Scalars"));
        //         System.out.println('\n' + s.longform() + '\n');

        ArrayList<Scalar> scalars = new ArrayList<Scalar>();
        ArrayList<String> options = new ArrayList<String>();
        options.add("Add a Scalar object to your pile.");
        options.add("View your pile.");
        options.add("Exit");

        NumMenu menu = new NumMenu(options);

        while(true){
 	    switch(menu.getSelection(true)){
 	      case 1:
	        scalars.add(new Scalar());
	        break;


	      case 2:
	        ArrayList<String> LabelPile = new ArrayList<String>();
	        for(int x = 0; x < scalars.size(); x++){
	  	   LabelPile.add(scalars.get(x).label);
	        }

	        TuiTeX.enumerate("Inventory", LabelPile);
	        break;

	      case 3:
	        System.exit(1);
	        break;

	      default:
	   }
        }
    }
}
