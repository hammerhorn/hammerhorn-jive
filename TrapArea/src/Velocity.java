public class Velocity extends MyVector
{
    //    double metersPerSecond;
    static int count = 0;
    //
    // CONSTRUCTORS
    //////////////////
    public Velocity(String unt, double mag)
    {
	count++;
        setLabel("VELOCITY #" + count);
        magnitude = mag;
        units = new Unit(unt);
        theta = new Angle();
    }

    public Velocity(double d, double degrees)
    {
	count++;
        setLabel("VELOCITY #" + count);
	units = new Unit("m/s");
        magnitude = d;

        if(d == 0.0D) {
	   theta = new Angle();
	} 
	else {
	    //	   theta = new Angle(Math.toRadians(degrees));
	    theta = new Angle("deg", degrees);
	}
        resolve();
    }

    public Velocity( )
    {
	count++;
        setLabel("VELOCITY #" + count);
    }

    public Velocity(double d, Angle angle)
    {
	    count++;
        setLabel("VELOCITY #" + count);
	units = new Unit("m/s");
        magnitude = d;
        if(d == 0.0D)
	    {
                theta = new Angle();
            } else
            {
                theta = angle;
            }
	resolve();
        //units = "";
    }

      
    //public Velocity(double,Angle )
    //{
    //    metersPerSecond = d;
    //}


    //
    // GET & SET
    ///////////////
    public double MperS(){return magnitude;}


    //
    // CALCULATE
    ///////////////
    public Velocity minus(Velocity myvel)
    {
	myvel.set(myvel.magnitude() * -1D);
        myvel.resolve();
        return this.plus(myvel);
    }

    public Velocity plus(Velocity myvector)
    {
        resolve();
        double d = x_magnitude + myvector.x_magnitude();
        double d1 = y_magnitude + myvector.y_magnitude();
	Velocity myvector1 = new Velocity(Math.sqrt(Math.pow(d, 2D) + Math.pow(d1, 2D)), Math.atan(d1 / d));
        if(d < 0.0D)
            {
		myvector1.magnitude *= -1D;
            }
        myvector1.theta.units.set("radians", "rad");
        return myvector1;
    }

    public String format() {
       return magnitude + " " + units.abbrev;
    }

    public double mph()
    {
       if(units.label.equals("mph")) return magnitude;
       else //( units.equals("m/s")) 
          return magnitude * 2.2369363;
    }

    public void mphToMperS()
    {
       if(units.label.equals("mph"))
       {
          units.set("m/s");
          magnitude *= .44704;
       }
    }
}
