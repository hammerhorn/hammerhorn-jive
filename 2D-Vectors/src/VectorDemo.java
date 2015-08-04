public class VectorDemo
{
    public static void main(String[] args)
    {
        MyOpts Args = new MyOpts(args, 4, "\tUsage: VectorTest mag1 ang1 mag2 ang2");
        MyVector A = new MyVector(Args.getAsDouble(0), Args.getAsDouble(1)),
                 B = new MyVector(Args.getAsDouble(2), Args.getAsDouble(3));

        System.out.println("Units(A): " + A.units.str());	       
        System.out.println("2-D Vectors can be added...");

        A.vplus(B);

        TuiTeX.hrule(80);
        TuiTeX.vspace(1);

        Keyboard.raw_input("Press <ENTER>");
        System.out.println("...or subtracted.");
        B.vminus(A);
    }
}
