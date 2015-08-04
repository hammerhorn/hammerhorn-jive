public class MixTool{
  public static void main(String[] args){
      String [] prompts = { "mL of first ingredient", "%ABV of first ingredient", "\nmL of second ingredient", "%ABV of second ingredient"};
      //      String usage = "Usage: java MixTest ((((A_mL) A_%solute) B_mL) B_%solute)";
      MyOpts i = new MyOpts( 4, args, prompts );

      Mixture m1 = new Mixture( i.getAsDouble(1) / 100, i.getAsDouble(0) );
      Mixture m2 = new Mixture( i.getAsDouble(3) / 100, i.getAsDouble(2) );
      System.out.println();
      Mixture m3 = m1.mix(m2);
      m3.print();
      System.out.println();
  }
}
