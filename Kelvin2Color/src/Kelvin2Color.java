//import java.io.*;

public class Kelvin2Color
{
  public static void main( String[] args )
  {
     String[] prompts = {"K"};
          MyOpts Args = new MyOpts(1, args, prompts);
     Photon lightwave = new Photon(Args.getAsDouble(0));        

      System.out.println();
      lightwave.print();
      System.out.println(lightwave.EMtype() + " (at peak)\n");
  }
}
