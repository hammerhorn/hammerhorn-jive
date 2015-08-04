//import java.io.*;

public class AccelTest2
{
  public static void main(String[] args)
  {
      Velocity v = new Velocity(Double.parseDouble(args[1]) - Double.parseDouble(args[0]), 0.0);
	
      Time delta = new Time(Double.parseDouble(args[2]));
      Accel a = new Accel(v, delta);
      
      System.out.println();
      a.PrintLabel();  

      System.out.print("avg. ");
      a.printout();
      System.out.println();
  }
}
