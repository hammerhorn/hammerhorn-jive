public class logb {
   public static void main(String[] args){
       String [] prompts = {"base", "m"};
       MyOpts Args = new MyOpts(2, args, prompts, "Usage: log <base> <m>");

       double base = Args.getAsDouble(0),
 	         m = Args.getAsDouble(1);
 
       System.out.println("log(" + TuiTeX.format(base) + ") " + TuiTeX.format(m)
		         + " = " + TuiTeX.format(MyMath.log(base, m)));
  }
}
