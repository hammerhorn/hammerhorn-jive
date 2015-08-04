import java.util.*;

public class NumMenu extends Thing
{
    ArrayList<String> options;

    public  NumMenu(ArrayList<String> opts){         
	label="MENU";
	options = opts;	 //        TuiTeX.enumerate(opts);
     }	
     
    public  NumMenu(String[] opts){         
        options = new ArrayList<String>();
	label="MENU";
        for(int index = 0; index < opts.length; index++){
	    options.add(opts[index]);	 //        TuiTeX.enumerate(opts);
        }
    }	
     

       public  NumMenu(String[] opts, String caption){         
	label=caption;
	for(int index = 0; index < opts.length; index++){
	    options.add(opts[index]);	 //        TuiTeX.enumerate(opts);
        }     
    }	
 
    
    
    public  NumMenu(ArrayList<String> opts, String caption){         
        options = new ArrayList<String>();
	label=caption;
	options = opts;	 //        TuiTeX.enumerate(opts);
     }	
     

    public void displayOptions(){

	//	PrintLabel();
        TuiTeX.enumerate(label, options);
    }

     public int getSelection(){
	 displayOptions();
        System.out.print(">");
	return Keyboard.readInt();
     }
}
