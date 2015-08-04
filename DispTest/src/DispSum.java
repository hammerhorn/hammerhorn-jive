public class DispSum {
   public static void main(String[] args) {
      displacement A = new displacement(), 
                   B = new displacement();

      String [] prompts = {  
	 "\n " + A.units.str() + "(1): ", "  θ(1) (°): ", 
         "\n " + B.units.str() + "(2): ", "  θ(2) (°): " };

        MyOpts argz = new MyOpts(4, args, prompts); 
   
	A.assign(new displacement(argz.getAsDouble(0), argz.getAsDouble(1)));
	B.assign(new displacement(argz.getAsDouble(2), argz.getAsDouble(3)));

        System.out.println(); 
	A.plus(B).println();
    }
}
