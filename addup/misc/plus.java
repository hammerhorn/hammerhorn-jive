import java.io.*;

public class plus
{
  public static void main(String args[])
  {
      double sum = 0.0;
      for(int count=0;count<args.length;count++) sum+=Double.parseDouble(args[count]);
      System.out.println(sum);
  }
}