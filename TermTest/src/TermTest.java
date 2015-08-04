//import java.io.*;

public class TermTest
{
  public static void main(String[] args)
  {
      boolean verbose = false;
      double value;
      String[] prompts = {"Coefficient: " , "Exponent: "};
      MyOpts Args = new MyOpts(2, args, prompts);
      Term t;

      if(Args.detectShortOption('v')) verbose = true;
      Args = Args.stripFlags();
      t = new Term(Args.getAsDouble(0), Args.getAsDouble(1));
  
      while(true){
          if(verbose) System.out.println("f(x) = " + t.getString());
	  value = Keyboard.readDouble("x:");
          if(verbose) System.out.print("f(" + TuiTeX.format(value) + ") = ");
	  System.out.print(TuiTeX.format(t.eval(value)));
	  TuiTeX.vspace();
      }
   }
}
