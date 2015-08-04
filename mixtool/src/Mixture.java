public class Mixture
{
   //
   // DATA
   //////////
   double percentMinor;
   Volume vol;
   

   //
   // CONSTRUCTORS
   ////////////////// 

   public Mixture(double p, double v)
   {
      percentMinor=p;
      vol = new Volume(v);
   }


    //
    // GET & SET
    //////////////

    public double getPercent(){return percentMinor;}
    public double getVolume(){return vol.ml();}


    //
    // CALCULATE
    ///////////////

    public Mixture mix(Mixture m)
    {
	return new Mixture(
(m.getPercent() * m.getVolume() +this.getPercent() * this.getVolume())/(m.getVolume() + this.getVolume()), (m.getVolume() + this.getVolume()));
    }


    //
    // I/O
    /////////

    public void print()
    {
       System.out.println("percent = " + TuiTeX.format(percentMinor*100)+"%");
     //System.out.println("volume=");
       vol.printout();
    }
}
