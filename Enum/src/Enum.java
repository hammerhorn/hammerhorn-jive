import java.util.*;

public class Enum {

    public static void main(String[] args) {
        Enumeration orderedList1;
        //if(args.length > 0) orderedList1 = new Enumeration(args); 

	//        else {
            ArrayList<String> lines = new ArrayList<String>();
            Scanner in = new Scanner(System.in);
            while(in.hasNext()) {
                String input = in.nextLine();
                lines.add(input); 
	    }
            orderedList1 = new Enumeration(lines); 
            if(args.length > 0) orderedList1.setLabel(args[0]);
	    // }

        orderedList1.print();
    }
}
