public class AngleInfo
{
    public static void main(String[] args) {
        //////////////////////////////////
        // DECLARATION & INITIALIZATION //
        //////////////////////////////////
        boolean verbose = false;
        
        MyOpts Argz = new MyOpts(args);
            Angle a = new Angle();
	   
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
        if(Argz.length() > 0) a.set(Argz.getAsDouble(0));
        else {
	    System.out.print(TuiTeX.rightAlign("th(" + a.units.abbrev + "): ", 10));
            a.set(Keyboard.readDouble());            
	}
         
        ////////////////
        // PRINT DATA //
        ////////////////
	//        TuiTeX.vspace(1);

        if(verbose){
            System.out.println(TuiTeX.box("Slope"));
            a.printDetailed();
TuiTeX.vspace(1);
	}
        else a.printBrief();
	//        a.printDegsMinsSecs();
        
        
   }
}
