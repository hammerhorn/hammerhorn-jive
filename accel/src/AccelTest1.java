//import java.io.*;

public class AccelTest1
{
  public static void main(String[] args)
  {
    MyOpts Args = new MyOpts(args, 3, "Usage: java AccelTest $(MPH1) $(MPH2) $(DELTA-T_SECONDS)");

    Velocity speed1 = new Velocity("mph", Args.getAsDouble(0) ),
             speed2 = new Velocity("mph", Args.getAsDouble(1));

    Time amount_of_time = new Time(Args.getAsDouble(2));

     speed1.mphToMperS();
     speed2.mphToMperS();

     Accel acceler = new Accel( speed1, speed2, amount_of_time );
     acceler.convertToMPHperS();
     acceler.printMag();
     System.out.println( " mph/s" );
     
     acceler.convertToMperS();
     //     acceler.printFull();
     acceler.printMag();
     System.out.println( " m/s^2");
  }
}
