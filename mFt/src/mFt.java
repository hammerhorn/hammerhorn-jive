public class mFt
{
  public static void main(String[] args)
  {
      final String usage = "\tUse: java mFt \"US\"/\"SI\" $MAGNITUDE";
      MyOpts Args = new MyOpts(2, args, usage);
      displacement disp=new displacement(Args.getAsDouble(1),Args.getElement(0));
      
      if(Args.getElement(0).equals("US")){
	  disp.SIprintln();
      }
      else if(Args.getElement(0).equals("SI")){
	  disp.USprintln();
      }
      else{
	   System.err.println(usage);
      }
  }
}
