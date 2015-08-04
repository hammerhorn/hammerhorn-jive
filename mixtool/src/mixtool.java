public class mixtool {
    public static void main(String[] args){
        // Calculate how much of 2 different solutions you need to 
        //    combine to reach a target %ABV and volume.
        //
        // Use: MixTool.py $%ABV1 $%ABV2 $TARGET_%ABV $TARGET_VOLUME
        //
        // If no arguments are given, input is from stdin.  
        // Pretty much a direct translation of MixTool.pl
 	    double abv1,
	          abv2,
            target_abv,
		target_vol,
                vol1,
		vol2;


        if (args.length == 0){
            System.out.print("%ABV of first ingredient: ");
            abv1 = Keyboard.readDouble();
        }
        else abv1 = Double.parseDouble(args[0]);

       if (args.length < 2 ) {
           System.out.print("%ABV of second ingredient: ");
           abv2 = Keyboard.readDouble(); 
       }
       else abv2 = Double.parseDouble(args[1]);

       if (args.length < 3 ){
           System.out.print("Target %ABV: ");
           target_abv = Keyboard.readDouble();
       }
       else target_abv = Double.parseDouble(args[2]);

       if ((target_abv < abv1 && target_abv < abv2) || (target_abv > abv1 && target_abv > abv2)){
           System.err.println("Sorry, that's not possible.");
           System.exit(1);
       }

       if(args.length < 4){
           System.out.print("Target volume (fl. oz.): ");
           target_vol = Keyboard.readDouble();
       }
       else target_vol = Double.parseDouble(args[2]);

       vol1 = target_vol * (target_abv - abv2) / (abv1 - abv2);
       vol2 = target_vol - vol1;
 
       System.out.println("\nYou will need " + vol1 + " fl. oz. of the first ingredient (" + abv1 + "% ABV), and" +
	                        "\n\t      " + vol2 + " fl. oz. of the second ingredient (" + abv2 + "% ABV).\n");
    }
}
