public class pow
{
    public static void main(String args[])
    {
        if(args.length == 0){
	    System.err.println("\tUsage: pow arg1 (arg2) ...");
            System.exit(1);
        }
        else if (args.length == 1){
	    System.out.println(TuiTeX.format(Float.parseFloat(args[0])));
        }
        else{
            double result1 = Double.parseDouble(args[0]),result2;
            for(int count = 1; count < args.length; count++) {
                result2 = Math.pow(result1, Double.parseDouble(args[count]));
                result1 = result2;
            }   
            System.out.println(TuiTeX.format(result1));
        }
    } 
}
