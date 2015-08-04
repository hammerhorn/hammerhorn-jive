public class accel_
{
    public static void main(String[] args)
    {
        MyOpts Args = new MyOpts(args, 3);

        Velocity v = new Velocity(Args.getAsDouble(1) - Args.getAsDouble(0), 0.0);
        Time delta = new Time(Args.getAsDouble(2));

        System.out.print("avg. ");
        (new Accel(v,delta)).printout();
    }
}
