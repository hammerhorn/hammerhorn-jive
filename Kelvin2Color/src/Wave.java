public class Wave extends Thing
{
    //
    // DATA
    //////////

	  Scalar freq;
    displacement wavelength; 
        Velocity speed;
      static int count = 0;

    //
    // CONSTRUCTORS
    //////////////////
	
    public Wave()
    {
	count++;
        setLabel("WAVE #" + count);
    }

    public Wave(double f, double s)
    {
	count++;
        setLabel("WAVE #" + count);
        freq = new Scalar(f, new Unit("Hertz", "Hz"));
        speed = new Velocity(s ,new Angle());
        wavelength = new displacement(s/f);
    }


    //
    // I/O
    /////////

    public void print()
    {
	System.out.println();
        PrintLabel();

	//Wave:printfreq();  
	System.out.println("      Freq: " + freq.str());
        System.out.println("Wavelength: " + wavelength.SIformat());
        System.out.println("     Speed: " + speed.format() + "\n");
    }

    public void printfreq()
    {
	System.out.println("      Freq: " + freq.str());
    }
}
