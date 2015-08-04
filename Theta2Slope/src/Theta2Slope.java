public class Theta2Slope
{
    public static void main(String[] args) {
        //////////////////////////////////
        // DECLARATION & INITIALIZATION //
        //////////////////////////////////
        boolean verbose = false;
	//	MyOpts Argz ;//= new MyOpts(); //not efficient
        Angle a = new Angle();
        //try{
          MyOpts Argz = new MyOpts(args);
	    //Angle a = new Angle();
	    //}   
	
	    //        catch(Exception e){
            //StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
            //StackTraceElement main = stack[stack.length - 1];
            //String mainClass = main.getClassName ();
            //System.out.println(mainClass);
            //System.exit(-1);
	    //}
     
        ////////////////////////////////////////////////////////////////////////////
        // IF THE FIRST ARGUMENT IS -r , THROW IT AWAY AND GET DATA INTERACTIVELY //
        ////////////////////////////////////////////////////////////////////////////
        if(! Argz.detectShortOption('r')) a.units.set("degrees", "°");
        if(  Argz.detectShortOption('v')) verbose = true;

        ///////////////////////////////////
        // STRIP FLAGS OUT FROM THE DATA //
        ///////////////////////////////////
        Argz = Argz.stripFlags();

        //Handle the args manually like this:
        //while(true){   
	if(Argz.length() > 0) {a.set(Argz.getAsDouble(0));
	    System.out.println();}
        else {
	    //	    System.out.print(TuiTeX.rightAlign("th(" + a.units.abbrev + "): ", 10));
            System.out.print(a.units.abbrev);
            a.set(Keyboard.readDouble());            
	}
         
        ////////////////
        // PRINT DATA //
        ////////////////
	//        TuiTeX.vspace(1);

        if(verbose){
            //System.out.println(TuiTeX.box(a.getLabel(), 18));
		//TuiTeX.hfill(19);
		//a.PrintLabel();
            a.printDetailed();
            System.out.println();
	}
        else a.printBrief();
	//        a.printDegsMinsSecs();
//a= new Angle();
//	}        
        }
    

}
