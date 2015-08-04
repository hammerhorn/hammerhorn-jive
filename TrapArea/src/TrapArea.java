public class TrapArea{
   public static void main(String[] args){
       StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
             StackTraceElement main = stack[stack.length - 1];
             String mainClass = main.getClassName ();
	     String use = "\tUse: java " + mainClass + " $WIDTH $BASE $HEIGHT";

	   MyOpts Args = new MyOpts(args, 3, use);
       Trapezoid quad;
       /*       if (args.length == 0){
           while(true){
	   *  System.out.println();
               quad = new Trapezoid();
               System.out.println("Trapezoid:" + TuiTeX.emph(quad.classify().toUpperCase()));
               quad.printout();
           }
       }
       else {*/
	   quad = new Trapezoid(Args.getAsDouble(0), Args.getAsDouble(1), Args.getAsDouble(2));
           System.out.println();
           System.out.println("Trapezoid:" + TuiTeX.emph(quad.classify().toUpperCase()));
           quad.printout();
           System.out.println();
	   // }
   }
}
