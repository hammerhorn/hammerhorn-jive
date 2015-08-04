public class TuiTest
{
    public static void main(String[] args)
    {
     // TwoD6 diePair= new TwoD6(); 
        Die randNum = new Die(100);

        TuiTeX.vspace();
        TuiTeX.underline("HOW TO MAKE A SIMPLE TABLE", 5);
        TuiTeX.vspace(1);
        TuiTeX.hfill(3);
        System.out.println("     COL1    COL2     COL3");
        TuiTeX.hfill(3);
        TuiTeX.hrule(31);
        TuiTeX.hfill(3);
        System.out.print(TuiTeX.rightAlign(randNum.value(), 8)); 
        randNum.roll();
        System.out.print(TuiTeX.rightAlign(randNum.value(), 8));
	randNum.roll();
        System.out.println(TuiTeX.rightAlign(randNum.value(), 8));

      //TuiTeX.hrule();
      //diePair.roll();
        randNum.roll();
        TuiTeX.hfill(3);
        System.out.println(TuiTeX.rightAlign(randNum.value(), 8) + 
	 		   TuiTeX.rightAlign(randNum.value(),8));
      //TuiTeX.hrule();
        randNum.roll();
        TuiTeX.hfill(3);

        System.out.println(TuiTeX.rightAlign(randNum.value(),8) + 
  			   TuiTeX.rightAlign(randNum.value(),8));
      //TuiTeX.hrule();
        TuiTeX.vspace();

        TuiTeX.itemize("", args);

        TuiTeX.enumerate("", args);

        System.out.println(TuiTeX.rightAlign("right", 70));
    }
}
