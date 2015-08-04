import java.io.*;

public class unicode
{
    public static void main(String args[])
    {
        int min = 1;
        int max = 0x10000;
        String s = "display";
        String s1 = "Unicode Compatibility Test";

        MyOpts Argz=null;

        if(args.length!=0) {
            Argz = new MyOpts(1, args, "Usage: java unicode <lowerLimit> " +
                   "(<upperLimit (65536)>) (<alternate filename>).");
        }
        else {
            System.err.println("\nUsage: java unicode <lowerLimit> (<upperLimit" +
                               " (65536)> (<alternate filename>[.html]) )\n");
            System.exit(1);
        }

        //  strippedArgz=Argz.stripFlags();
        //System.out.println("There are "+Argz.lengthMinusFlags()+" non-flag arguments");


        //////////////////////////////////////////////////////////////////////
        // If the MyOpts has no args that are not flags, print an error and //
        // terminate the program.                                           //
        //////////////////////////////////////////////////////////////////////
        if(Argz.lengthMinusFlags() == 0) {
            System.err.println("\nUsage: java unicode <lowerLimit> (<upperLimit " +
                               "(65536)> (<alternate filename>[.html]) )\n");
	    System.exit(1);
        }


        //////////////////////////////////////
        // if only two arguments are found, //
        // the max is set to the min + 100. //
        //////////////////////////////////////
        else if(Argz.lengthMinusFlags() == 1) {
            //System.out.println("There is exactly 1 non-flag argument.");
            min = Argz.stripFlags().getAsInt(0);

            if(min >= 65436) max = 0x10000;
  	    else max = min + 100;
        }

        else if(Argz.lengthMinusFlags() > 1) {
            min = Argz.stripFlags().getAsInt(0);
   	    max = Argz.stripFlags().getAsInt(1);
        }


        ////////////////////////////////////////////////////////////////////////
        // If either the max or min is lower than 1 or higher than 65536, the //
        //  program aborts.                                                   //
        ////////////////////////////////////////////////////////////////////////
        if(min < 1 || min > 0x10000 || max < 1 || max > 0x10000) {
            System.out.print("Request out of range.  Write to " + s + ".html FAILED.");
            System.exit(1);
        }


        ////////////////////////////////////////////////////////////////////////
        // If the -p flag is specified, output is directed to standard out as //
        // plain text.                                                        //
        ////////////////////////////////////////////////////////////////////////
        if( Argz.detectShortOption('p') ) {
            System.out.println('\n' + s1);
	    TuiTeX.hrule();

            if(max < min) {
 	        int l = max;
	        max = min;
	        min = l;
	    }

  	    for(; min <= max; min++) {
                //System.out.println(TuiTeX.rightAlign(i) + ": &#" + min + ";");
                System.out.println(TuiTeX.rightAlign(min, 5) + ": "+ (char)min);
	    }

  	    TuiTeX.hrule();
	    System.out.println();
        }

        else {
            try
 	    {
	        if(Argz.lengthMinusFlags() > 2) {
	            int k = 1;
	            s = Argz.stripFlags().getElement(2);

		    if(s.charAt(0) >= 'a' && s.charAt(0) <= 'z') {
 	 	        s1 = "" + (char)(s.charAt(0) - 32);

		        for(; k < s.length(); k++) {
		            s1 = s1 + s.charAt(k);
		        }
	            }

	            else s1 = s;
	        }

                FileWriter filewriter = new FileWriter(s + ".html");
  	        filewriter.write("<HTML><HEAD>");
	        filewriter.write("<TITLE>" + s1 + "</TITLE>" +
                                 "<LINK Rel=\"stylesheet\" Type=\"text/css\" Href=\"serious.css\">" +
                                 "</HEAD><BODY><h1>" + s1 + "</h1><hr>");

   	        if(max < min) {
	            int l = max;
	            max = min;
	            min = l;
	        }

   	        for(; min <= max; min++) {
	            filewriter.write(min + ": &#" + min + ";<BR>");
	        }

  	        filewriter.write("<hr></BODY></HTML>");

 	        System.out.println(s + ".html" + " has been written.  ");
	        System.out.print("To view, open ");

	        if(args.length < 3) System.out.println("viewer.html");
	        else System.out.println(s + ".html");

	        if(filewriter != null) filewriter.close();
	    }

            catch(Exception exception)
  	    {
	        exception.printStackTrace();
	    }
        }
    }
}
