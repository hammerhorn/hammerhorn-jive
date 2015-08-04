import java.util.*;

public class NumMenu extends Thing{
    ArrayList<String> options;

    //
    // Constructors
    /////////////////
    public  NumMenu(ArrayList<String> opts){         
	label = "Make a choice (1-" + opts.size() + ")";
	options = opts;
     }	
     
    public  NumMenu(String[] opts){         
        options = new ArrayList<String>();
	label = "Make a choice (1-" + opts.length + ")";
        for(int index = 0; index < opts.length; index++){
	    options.add(opts[index]);
        }
    }	

    public  NumMenu(String[] opts, String caption){         
	label = caption;
	for(int index = 0; index < opts.length; index++){
	    options.add(opts[index]);
        }     
    }	
     
    public  NumMenu(ArrayList<String> opts, String caption){         
        options = new ArrayList<String>();
	label=caption;
	options = opts;
     }	
     
    //
    // Methods
    ////////////
    public void displayOptions(){
        TuiTeX.enumerate(label, options);
    }

     public int getSelection(boolean showMenu){
	 if(showMenu) displayOptions();
         if(!showMenu) System.out.print("(1-" + options.size() + ")");

         int i = 0;
	 while(i < 1 || i > options.size()){
             System.out.print(">");
  	     try{
                 i = Keyboard.readInt();
	     } 
             catch(Exception e){
		 continue;
             }
             if (i < 0 || i > options.size()) continue;
        }
        return i;
    }
}
