public class VectorSum
{
    public static void main(String[] args)
    {
        String [] prompts = {
            "\n magnitude(1): ", "     θ(1) (°): ",
            "\n magnitude(2): ", "     θ(2) (°): "
        };

        MyOpts argz = new MyOpts(4, args, prompts); 
   
        MyVector A = new MyVector(argz.getAsDouble(0), argz.getAsDouble(1)),
                 B = new MyVector(argz.getAsDouble(2), argz.getAsDouble(3));

        TuiTeX.vspace(1);	   

     // A.print();
     // B.print();
        A.plus(B).println();
   }
}
