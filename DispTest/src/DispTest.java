//import java.io.*;

public class DispTest 
{
   public static void main(String[] args)
   {
       displacement dA = new displacement("DISPLACEMENT A"),
  	            dB = new displacement("DISPLACEMENT B"),
	            dC = new displacement("DISPLACEMENT C"),
	            dD = new displacement("DISPLACEMENT D"),
	            dE = new displacement("DISPLACEMENT E");

       //      System.out.println();
       //      dA.PrintLabel();	   
       //      dA.PromptUser();
       //      MyFormat.whitespace(2);
       //      dB.PrintLabel();
       //      dB.PromptUser();
       //
       //      System.out.println("\n\n\n A + B");
       //      System.out.println("========");
      dC.assign(dA.vplus(dB));
      //      dC.printout("US");

      System.out.print("     ( ");
      dC.printFull("SI");
      System.out.println("\n   {" + MyFormat.format(dC.Inches()) + " inches");
      System.out.println("   "    + MyFormat.format(dC.Feet())   + " feet");
      System.out.println("   "    + MyFormat.format(dC.Miles())  + " miles");
      System.out.println("   "    + MyFormat.format(dC.Meters()) + " meters}");
      dC.printXandY();
      System.out.println();
 
 
      System.out.println("\n\n\n B - A");
      System.out.println("========");
      dD.assign(dB.minus(dA));
      dD.printout("US");
      System.out.print("     ( ");
      dD.printFull("SI");
      System.out.println("\n   {" + MyFormat.format(dD.Inches()) + " inches");
      System.out.println("   " + MyFormat.format(dD.Feet()) + " feet");
      System.out.println("   " + MyFormat.format(dD.Miles()) + " miles");
      System.out.println("   " + MyFormat.format(dD.Meters()) + " meters}");
      dD.printXandY();
      System.out.println();
      

      dE.PromptUser();
      dE.printout("US");
      System.out.println();

      dE.print();

/*      System.out.println("\n\n\n");
      d5.println_mag();
      
      d5.printFull("US");
      d5.printFull("SI");
      
      d5.printout("US");
      d5.printout("SI");
      
      System.out.println();
 
      //System.out.println("\nprintout(\"US\")");
      //d4.printout("US");
      //d4.printout("SI");
      //System.out.println("\nprintout(\"SI\")");*/
   }
}
