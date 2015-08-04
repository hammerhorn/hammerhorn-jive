import java.util.*;

public class NumMenu extends Thing{
    ArrayList<String> options;

    public  NumMenu(ArrayList<String> opts){         
	label="Make a choice (1-" + opts.size() + ")";
	options = opts;	 //        TuiTeX.enumerate(opts);
     }	
     
    public  NumMenu(String[] opts){         
        options = new ArrayList<String>();
	label="Make a choice (1-" + opts.length + ")";
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

     public int getSelection(boolean showMenu){
	 if(showMenu) displayOptions();
         if(!showMenu) System.out.print("(1-" + options.size() + ")");
         System.out.print(">");

 	 try{
 	     String s;
             s = Keyboard.readLine();
             int i = Integer.parseInt(s);
             //if (s.matches("[0-9]*")) return i;
             if (i < 0 || i > options.size()) return -1;
             //else return -1;
	     else return i;
	 } 
         catch(Exception e){
             return -1;
         }
     }
}
