public class WaveTest
{
    public static void main(String[] args)
    {
        double f1 = 440.0,
               f2 = 440.0,
               f3 = 440.0,
               s = 344.21;

        MyOpts Args = new MyOpts(args);

        if(Args.length() > 0) f1 = Args.getAsDouble(0);
        if(Args.length() > 1) f2 = Args.getAsDouble(1);
        if(Args.length() > 2) f3 = Args.getAsDouble(2);
        if(Args.length() > 3)  s = Args.getAsDouble(3);

        System.out.println();

        Wave awave = new Wave(f1,s);
        awave.print();

        Wave bwave = new Wave(f2,s);
        bwave.print();

        Wave cwave = new Wave(f3,s);
        cwave.print();
    }
}

