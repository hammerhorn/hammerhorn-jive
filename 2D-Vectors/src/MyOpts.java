//import java.io.*;
//import java.text.*;
import java.util.*;

public class MyOpts{
    //
    // DATA
    //////////
    ArrayList<String> myArgs;

    //
    // CONSTRUCTORS
    //////////////////
    public MyOpts(){
        myArgs = new ArrayList<String>();
    }


    /////////////////////////////////////////////////////////////
    // takes an array of args. no predetermined size parameter //
    /////////////////////////////////////////////////////////////
    public MyOpts( String [] argz ){
        myArgs = new ArrayList<String>();
	setStringArray(argz);
    }



    ///////////////////////////////////////////////////////////////////////////
    // takes an array of args, and an exact number of fields, otherwise fails /
    ///////////////////////////////////////////////////////////////////////////
    public MyOpts(String[] argz, int no_of_args){
        myArgs = new ArrayList<String>();        
        setStringArray(argz);

        if (lengthMinusFlags() != no_of_args){
            // Get class name
	    StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
	    StackTraceElement main = stack[stack.length - 1];
	    String mainClass = main.getClassName ();

 	    System.err.println("\n\t" + mainClass + ": exactly " + no_of_args + " argument(s) expected.\n");
            System.exit(-1);
	}
    }


    //I need to figure out how to deal with flags in interactive mode
     
    //////////////////////////////////////////////
    // reads from stdin if argument not present // 
    // Extra fields are thrown away.            //
    //////////////////////////////////////////////
    public MyOpts(int min_no_of_args, String[] argz){
        myArgs = new ArrayList<String>();
 	if(argz.length >= min_no_of_args){ 
            setStringArray(argz); 
            for (int index = min_no_of_args; index < myArgs.size(); index++){
                if(myArgs.get(index).charAt(0) != '-') myArgs.remove(index);
            }
        }
	else { 
	    //            if(myArgs == null) myArgs = new ArrayList<String>();
            do{
                myArgs.add(Keyboard.readLine());
            } while(lengthMinusFlags() < min_no_of_args);
        }
    }




    ////////////////////////////////////////////////////////////
    // Prints custom errorMessage if number of args is wrong. //
    // Extra fields are thrown away.                          //
    ////////////////////////////////////////////////////////////
    public MyOpts(String[] argz, int no_of_args, String errorMessage){
        MyOpts tmp = new MyOpts(argz);
        
        if(tmp.lengthMinusFlags() < no_of_args){
	    System.err.println(/*"\n" +*/ errorMessage + "\n");
            System.exit(1);
        }
	else{
            myArgs = new ArrayList<String>();
            for(int x = 0; x < tmp.length(); x++){
                myArgs.add(argz[x]);
                if(argz[x].charAt(0)=='-'){
                    
                }
	    }
        }
    }


    //////////////////////////////////////////////////////////////////
    // takes a minimum no. of args, args array, custom error string //
    //////////////////////////////////////////////////////////////////
    public MyOpts(int min_no_of_args, String[] argz, String errorMessage) {
        myArgs = new ArrayList<String>();
	if(argz.length >= min_no_of_args) setStringArray(argz);
        else { 
            System.err.println("\n" + errorMessage + "\n"); 
            System.exit(1);
       }
    }


    //////////////////////////////////
    // This constructor seems buggy //
    //////////////////////////////////
    public MyOpts(int min_no_of_args, String[] argz, String[] prompts, String useMessage) {
        System.err.println(useMessage);
        myArgs = new ArrayList<String>();
        MyOpts temp = new MyOpts(argz);
	if(temp.lengthMinusFlags() >= min_no_of_args) setStringArray(argz);

	else {
	    myArgs = new ArrayList<String>(); 

            for(int count = 0; count < argz.length; count++){
	        myArgs.add(argz[count]);
            }

	    int promptCount = 0;
    
            for(int count = temp.lengthMinusFlags(); count < min_no_of_args; count++){
                promptCount = count;
 	        System.out.print(prompts[promptCount]);
                myArgs.add(Keyboard.readLine());
                if(promptCount < prompts.length - 1) promptCount++;                 
                else promptCount = 0;
            }
        }


        /*myArgs = new ArrayList<String>(); 
        if(argz.length >= min_no_of_args) setStringArray(argz);
        else {
            System.err.println("\n" + errorMessage + "\n");    

            for(int count = 0; count < myArgs.size(); count++) {
                myArgs.add(argz[count]);
            }
     
            for(int count = 0; count < argz.length; count++) {
                System.out.println(prompts[count] + " = " + argz[count]);
            }

            for(int count = argz.length; count < min_no_of_args; count++) {
                System.out.print(prompts[count]);
                myArgs.add(Keyboard.readLine());                 
            }
	    }*/
    }


    // Extra args are kept
    ////////////////////////////////////////////////////////////////////////
    // Gets fields from stdin if necessary, with a ring of custom prompts // works
    ////////////////////////////////////////////////////////////////////////
    public MyOpts(int min_no_of_args, String[] argz, String[] prompts) {
        myArgs = new ArrayList<String>();
        MyOpts temp = new MyOpts(argz);
	if(temp.lengthMinusFlags() >= min_no_of_args) setStringArray(argz);

	else {
	    myArgs = new ArrayList<String>(); 

            for(int count = 0; count < argz.length; count++){
	        myArgs.add(argz[count]);
            }

	    int promptCount = 0;
    
            for(int count = temp.lengthMinusFlags(); count < min_no_of_args; count++){
                promptCount = count;
 	        System.out.print(prompts[promptCount]);
                myArgs.add(Keyboard.readLine());
                if(promptCount < prompts.length - 1) promptCount++;                 
                else promptCount = 0;
            }
        }
    }

/*    ///////////////////////////////////////////////////////////////////////////////////////
    // takes a minimum no. of args, array of args, array of prompts, custom error string //
    ///////////////////////////////////////////////////////////////////////////////////////
    public MyOpts(int min_no_of_args, String[] argz, String[] prompts, String errorMessage, boolean interactive)
    {
     //  errorMessage="\n"+errorMessage+"\n";
       if(argz.length>=min_no_of_args){ myArgs=argz;}
       //else
       //{ 
         // myArgs = new String[min_no_of_args];
          //System.err.println(errorMessage);    
          //for(int count=0;count < argz.length; count++)
          //{
           //   myArgs[count]=argz[count];
         // }
    
	   //           System.err.println("("+min_no_of_args+" or more arguments expected.)");
      if(interactive)
      {
          System.out.println("Going into interactive mode");
myArgs=stripFlags().getStringArray();
          for(int count=argz.length;count<min_no_of_args;count++)
          {
             System.out.print(prompts[count]+"?");
             myArgs[count]=Keyboard.readLine();                 
          }
      }
   }
       // System.out.println();
*/


    //
    // GET & SET
    ///////////////
    public String getElement(int subscript) { 
        if(subscript > myArgs.size() - 1){
            if(myArgs.size() == 0) System.err.println("Error - Attempt to access empty array.");
    	    else System.err.println("Error - Subscript must be between 0 and " + myArgs.size() + ", so " + subscript + " is an invalid value.");
            System.exit(1);
        }
	return myArgs.get(subscript);
    }


    public double getAsDouble(int subscript){ 
	/* if(subscript > this.length() - 1 || subscript < 0){
	    System.err.println("ERROR - MyOpts.getAsDouble(): Subscript out of bounds. ");
            System.exit(1);
	    }*/
        try{
	   return Double.parseDouble(this.getElement(subscript));
	}
        catch(Exception e){
	    System.err.println("ERROR - MyOpts.getAsDouble(): Expecting argument of type double.");
            System.exit(1);
	}
        return -1;
    }


    public int getAsInt(int subscript){ 
        if(subscript > length() - 1){
	   System.err.println("Expecting argument(s) of type: int");
           System.exit(1);
	}
	return Integer.parseInt(getElement(subscript));
    }




    public int length() {
        return myArgs.size();
    } 


    public int lengthMinusFlags() {
        int net_length = this.length();
        for(int x = 0; x < myArgs.size(); x++){
            if(myArgs.get(x).charAt(0) == '-') net_length--;
        }
        return net_length;
    }



    public int countFlags(){
	int flagCount = 0;
        for(int x = 0; x < this.length(); x++){
	    if(myArgs.get(x).charAt(0) == '-'){ 
	        for(int q = 0; q < myArgs.get(x).length() - 1; q++){
		    flagCount++;
                }
	    }
        }
        return flagCount;
    }


    
    public MyOpts stripFlags(){
        String[] stript = new String [this.lengthMinusFlags()];

	int netIndex = 0;
        for(int rawIndex = 0; rawIndex < this.length(); rawIndex++){
            if(getElement(rawIndex).charAt(0) != '-'){
	        stript[netIndex] = getElement(rawIndex); 
		netIndex++;
	    }	
        }
	MyOpts i = new MyOpts(stript);
	return i;
    }

    
    
    
    public static boolean detectShortOption(String [] Args, char c) {
	boolean flagDetected = false;
        for(int count = 0; count < Args.length; count++) {
            if(Args[count].charAt(0) == '-') { 
                for(int j = 1; j < Args[count].length(); j++) {
		    if(Args[count].charAt(j) == c) flagDetected = true;
	        }
	    }
        }
	return flagDetected;
    }

    
     public boolean detectShortOption(char c) {
	 boolean flagDetected = false;
         for(int count = 0; count < myArgs.size(); count++){
             if(this.myArgs.get(count).charAt(0) == '-') { 
                 for(int j = 1; j < myArgs.get(count).length(); j++){
		     if(myArgs.get(count).charAt(j) == c) flagDetected = true;
	         }
	     }
         }
	 return flagDetected;
    }

    
    
    public int firstFlagIndex(){
	for(int count = 0; count < myArgs.size(); count++){
            if(myArgs.get(count).charAt(0) == '-') return count;
        }
        return -1;
    }


    
    public String getShortOptions(){      
	String flags = "";
        for(int count = 0; count < length(); count++){
            if(myArgs.get(count).charAt(0) == '-'){ 
	        if(myArgs.get(count).length() >= 2){ 
                    for(int j = 1; j < myArgs.get(count).length(); j++){
		        flags += myArgs.get(count).charAt(j);
                    }
                }
	    }
	}
        return flags;
    }


    public char[] getFlagList(){
        String flags = getShortOptions();
        char[] flaglist = new char[flags.length()];
        for(int x = 0; x < flags.length(); x++){
            flaglist[x] = flags.charAt(x);
        }
        return flaglist;
    }


    private void setStringArray(String [] a){
	myArgs.clear();
	for(int x = 0; x < a.length; x++){ //maybe an arbitrary +1 in there will fix it
            myArgs.add(a[x]);            //not sure what's going wrong here
        }
    }

    ////////////////////////////////////////
    // returns raw args as a String array //
    ////////////////////////////////////////
    public String[] getStringArray(){
	String[] array = new String[myArgs.size()];
        for(int x = 0; x < myArgs.size(); x++){
            array[x] = myArgs.get(x);
        }
        return array;
    }


    //
    // I/O
    /////////
    public void printArgs(){
	System.out.print("[");
	for(int count = 0; count < this.length(); count++){
	    System.out.printf("\'%s\'", myArgs.get(count));
            if(count != this.length() - 1) System.out.print(", ");
	}
	System.out.println("]");
    }


    public void flagList(){
        System.out.print("[");

        for (int count = 0; count < countFlags(); count++){
	    if(count != 0) System.out.print(", ");
	    System.out.print(getShortOptions().charAt(count));
        }

        System.out.println("]");
    } 
}
