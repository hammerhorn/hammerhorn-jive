import java.util.*;

public class ItemTest
{
    public static void main(String[] args)
    {
	// if(args.length > 0){
        //            Enumeration list1 = new ItemList(args);
	//  list1.print();

	ItemList list1;
	    // if(args.length > 0) orderedList1 = new Enumeration(args);                                                                       
	    // else {                                                                                                                  
        ArrayList<String> lines = new ArrayList<String>();
        Scanner in = new Scanner(System.in);
	while(in.hasNext()) {
	    String input = in.nextLine();
	    lines.add(input);
	}
	list1 = new ItemList(lines);
	if(args.length > 0)
            list1.setLabel(args[0]);
	    // }                                                                                                                          

	list1.print();
    }
}

