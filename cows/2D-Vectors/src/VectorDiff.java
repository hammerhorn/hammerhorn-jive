public class VectorDiff{
    public static void main(String[] args)
    {
	MyVector A = new MyVector(),
	         B = new MyVector();

     // String [] prompts = {
     //     "\n " + A.units.str() + "(1): ", "     θ(1) (°): ",
     //     "\n " + B.units.str() + "(2): ", "     θ(2) (°): " 
     // };

     // MyOpts argz = new MyOpts(4, args, prompts); 
   
     // A.assign(new MyVector(argz.getAsDouble(0), argz.getAsDouble(1)));
     // B.assign(new MyVector(argz.getAsDouble(2), argz.getAsDouble(3)));

     // System.out.println();  
     // A.minus(B).println();
     // System.out.println();  
     // A.vminus(B);

        String[] prompts = {
     // { "\n " + A.units.str() + "(1): ", "     θ(1) (°): ",  
     //     "\n " + B.units.str() + "(2): ", "     θ(2) (°): "};  
	    "\n " + "magnitude" + "(1): ", "     θ(1) (°): ",  
            "\n " + "magnitude" + "(2): ", "     θ(2) (°): "
        };  
        MyOpts Args = new MyOpts(4, args, prompts);
        A = (new MyVector(Args.getAsDouble(0), Args.getAsDouble(1)));
	//        System.err.println(A.str());
        B = (new MyVector(Args.getAsDouble(2), Args.getAsDouble(3)));
        //System.err.println(B.str());

        //METHOD 1
        //System.out.println("\n" + (A.minus(B)).str());

        //METHOD 2
        System.out.println();  
        MyVector C = A.minus(B);
        
	//        (A.minus(B)).println();
        System.out.println(C.str());  
	//        A.vminus(B);


	/*        System.out.println(TuiTeX.box("MyVector.print()"));
        C.print();

        System.out.println(TuiTeX.box("MyVector.println()"));
        C.println();

        System.out.println(TuiTeX.box("MyVector.printFull()"));
        C.printFull();

        System.out.println(TuiTeX.box("MyVector.quickview()"));
        C.quickview();

        System.out.println(TuiTeX.box("MyVector.printXandY()"));
        C.printXandY();

        System.out.println(TuiTeX.box("MyVector.printMag()"));
        C.printMag();

        System.out.println(TuiTeX.box("System.out.println(MyVector.format())"));
	System.out.println(C.format());

	System.out.println(TuiTeX.box("System.out.println(MyVector.str())"));
	System.out.println(C.str());*/

   }
}
