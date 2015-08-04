public class Mix2
{
  public static void main(String[] args)
  {
      String [] prompts = { "%ABV of first ingredient", "%ABV of second ingredient", "Target %ABV", "Target volume (fl. oz.)"};
      //String usage = "Usage: java Mix2 $ABV1 $ABV2 $targetABV $targetVOL";
      MyOpts i = new MyOpts( 4, args, prompts );

double vol1 = (i.getAsDouble(2)*i.getAsDouble(3)-i.getAsDouble(1) * i.getAsDouble(3))/(i.getAsDouble(0)-i.getAsDouble(1));    
Mixture m1 = new Mixture(i.getAsDouble(0)/100, vol1);
//Mixture m2 = new Mixture(i.getAsDouble(1)/100, i.getAsDouble(3)-vol1);

System.out.print("\nYou will need "+ m1.getVolume() + "of the first ingredient");
System.out.print("(" + m1.getPercent() + "), ");
//m1.print();
//m2.print();


      /*      Mixture m1 = new Mixture( i.getAsDouble(1) / 100, i.getAsDouble(0) );
      Mixture m2 = new Mixture( i.getAsDouble(3) / 100, i.getAsDouble(2) );
      System.out.println();
      Mixture m3 = m1.mix(m2);
      m3.print();
      System.out.println();*/
  }
}
