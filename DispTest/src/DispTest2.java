//import java.io.*;

public class DispTest2
{
  public static void main(String[] args)
  {
      MyOpts Args = new MyOpts(args, 4, "\tUsage: VectorTest mag1 ang1 mag2 ang2");
	  
      displacement A = new displacement(Args.getAsDouble(0), Args.getAsDouble(1)),
 	           B = new displacement(Args.getAsDouble(2), Args.getAsDouble(3)),
                   C =  A.vplus(B);

      MyFormat.hr();
      C.quickview();
      System.out.println();
   }
}
