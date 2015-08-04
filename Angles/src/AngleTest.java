//import java.io.*;

public class AngleTest
{
   public static void main(String[] args)
   {
       MyOpts Args = new MyOpts(args);
       Angle a = new Angle("deg", Args.getAsDouble(0)), 
             b, 
             c;

        a.print();
	TuiTeX.vspace();
	a.printout();
	TuiTeX.vspace();
	a.printDetailed();
	TuiTeX.vspace();
	a.printBrief();
        TuiTeX.hrule();

        b = new Angle();
        b.PromptUser();

        System.out.println(b.degreeFormat() + "\n" + b.SIformat());
        b.print();
        TuiTeX.vspace();
        b.printout();
        TuiTeX.vspace();
	b.printDetailed();
	TuiTeX.vspace();
        b.printBrief();
        TuiTeX.hrule();

        c = new Angle(MyMath.PI/2);
  
        c.print();
        TuiTeX.vspace();
        c.printout();
        TuiTeX.vspace();
	c.printDetailed();
        TuiTeX.vspace();
        c.printBrief();
   }
}
