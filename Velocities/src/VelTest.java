public class VelTest
{
    public static void main(String[] args)
    {
        System.out.print("\nmph1:");
        Velocity minuend = new Velocity("mph", Keyboard.readDouble());

     // System.out.print(minuend.format());
     // System.out.print("\nmph2:");
     // Velocity subtractend = new Velocity("mph", Keyboard.readDouble());
     // System.out.print(subtractend.format());
     // System.out.print(minuend.format());
     // System.out.print(" minus ");
     // System.out.print(subtractend.format());
     // System.out.print(" equals ");
     // System.out.println((minuend.minus(subtractend)).format());

        minuend.PrintLabel();
	TuiTeX.vspace(3);
        minuend.println();
	TuiTeX.vspace(3);
        minuend.print();
	TuiTeX.vspace(3);
        minuend.printFull();
   }
}
