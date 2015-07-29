//import java.io.*;

public class die6x2
{
  public static void main(String[] args)
  {

      MyOpts Args = new MyOpts(args);
      TwoD6 dice = new TwoD6();

      if(Args.detectShortOption('a') || Args.detectShortOption('v')) dice.print();
      else  System.out.println(dice.value());

      if(Args.detectShortOption('v')) System.out.println();
      if(Args.detectShortOption('a')) dice.drawFaces();

      if(Args.detectShortOption('v')){
          TuiTeX.hfill(1);
          TuiTeX.hrule(21);
          dice.left.display();
          System.out.println();
          dice.right.display();
          TuiTeX.vspace();
      }

  }
}
