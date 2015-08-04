public class VelDiff
{
    public static void main(String[] args)
    {
        Velocity A = new Velocity(),
	         B = new Velocity();

        String [] prompts = {
            "\n " + A.units.str() + "(1): ", "     θ(1) (°): ",
            "\n " + B.units.str() + "(2): ", "     θ(2) (°): "
        };

        MyOpts argz = new MyOpts(4, args, prompts);

        A.assign(new Velocity(argz.getAsDouble(0), argz.getAsDouble(1)));
        B.assign(new Velocity(argz.getAsDouble(2), argz.getAsDouble(3)));

        System.out.println();
	A.minus(B).println();
    }
}
