//import java.io.*;

public class PointTest
{
  public static void main(String[] args)
  {
      String[] prompts = {"x: " , "y: "};
      MyOpts Args = new MyOpts(2, args, prompts);
      Point p, q;



      p = new Point(Args.getAsDouble(0), Args.getAsDouble(1));

      System.out.println();
      p.print();

      q = new Point(0,0);
      q.PromptUser();

      System.out.println();
      q.print();
  }
}
