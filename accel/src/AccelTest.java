public class AccelTest
{
  public static void main(String[] args)
  {
//  if(args.length==0){
//    System.err.println("\nUsage: java AccelTest $(MPH1) $(MPH2) $(DELTA-T_SECONDS)\n");
//    System.exit(1);
//  }
    MyOpts opts = new MyOpts(args, 3, "Usage: java AccelTest $(MPH1) $(MPH2) $(DELTA-T_SECONDS)");



//  Velocity speed1 = new Velocity( "mph", Double.parseDouble( args[0] ) ),
//           speed2 = new Velocity( "mph", Double.parseDouble( args[1] ) );
    Velocity speed1 = new Velocity("mph", opts.getAsDouble(0) ),
             speed2 = new Velocity("mph", opts.getAsDouble(1));

//  Time amount_of_time = new Time( Double.parseDouble( args[2]) ); 
    Time amount_of_time = new Time(opts.getAsDouble(2));

     speed1.mphToMperS();
     speed2.mphToMperS();
     Accel acceler = new Accel( speed1, speed2, amount_of_time );
     acceler.convertToMPHperS();
     acceler.printMag();
     System.out.println( " mph/s" );
  }
}
