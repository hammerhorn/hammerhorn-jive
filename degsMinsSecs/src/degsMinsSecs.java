public class degsMinsSecs 
{
   public static void main(String[] args) 
   {
       MyOpts Args = new MyOpts(1, args);
      Angle theta = new Angle();
      theta.setByDegrees(Args.getAsDouble(0));
      theta.printDegsMinsSecs();
   }
}
