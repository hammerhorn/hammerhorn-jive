public class CallNumTest{
  public static void main(String[] args){
     boolean tree = false;
     MyOpts Args; // = new MyOpts(1, args);
     CallNum c = new CallNum(0.0);

     try{
	 //         CallNum c; // = new CallNum(-999); 
         Args = new MyOpts(1, args);
         c = new CallNum(Args.getAsDouble(0));
         if(Args.detectShortOption('t')) tree = true;
         Args = Args.stripFlags();

     }

     catch(Exception exception){
       	     StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
       	     StackTraceElement main = stack[stack.length - 1];
       	     String mainClass = main.getClassName ();
             System.err.println("usage: " + mainClass + ".jar [-t] $CALL_NUMBER\n\n  -t\t\t\tdewey decimal number"); 
             System.exit(-1);
     }

     finally{
         System.out.println();
         if (tree) c.printLong();
         else c.printShort();
         System.out.println("\n");
     }
  }
}
