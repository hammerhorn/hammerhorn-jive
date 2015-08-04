public class Accel extends MyVector
{

    static int count = 0;

    //
    // CONSTRUCTORS
    //////////////////

    // Construct an Accel object with all fields zeroed out 
    // and units set to m/s^2.
    public Accel()
    {
        count++;
        setLabel("ACCELERATION #" + count);
        magnitude = 0.0D;
        theta = new Angle();
        units = new Unit("m/s²");
        resolve();
    }

    // Construct an Accel object with the angle set to zero 
    // and magnitude set to a given double in m/s^2.
    public Accel(double MperSperS)
    {
        count++;
        setLabel("ACCELERATION #" + count);
        magnitude = MperSperS;
        theta = new Angle();
        units = new Unit("m/s²");
    }

    // Construct an Accel object with the supplied magnitude in 
    // m/s^2 and angle in degrees.
    public Accel(double mag, double degrees)
    {
        count++;
        setLabel("ACCELERATION #" + count);
        units = new Unit("m/s²");
        magnitude = mag;
        if(mag == 0.0D)
            theta = new Angle();
        else theta = new Angle("deg",degrees);
        resolve();
    }

    // Construct an Accel object with the supplied magnitude in
    // m/s^2 and angle as a predefined Angle object.
    public Accel(double mag, Angle angle)
    {
        count++;
        setLabel("ACCELERATION #" + count);
        magnitude = mag;
        theta = angle;
        resolve();
        units = new Unit("m/s²");
    }

    // Construct Accel resulting from change in Velocity over a duration of time.
    public Accel(Velocity delta_v, Time delta_t)
    {
        count++;
        setLabel("ACCELERATION #" + count);
        magnitude = delta_v.MperS() / delta_t.Seconds();
        theta = delta_v.theta();
        resolve();
        units = new Unit("m/s²");
    }

    // Construct Accel resulting from an initial and final Velocity 
    // over a duration of time.
    public Accel(Velocity v_init, Velocity v_final, Time delta_t)
    {
        count++;
        setLabel("ACCELERATION #" + count);
        Velocity delta_v = v_final.minus(v_init);
        magnitude = delta_v.magnitude() / delta_t.Seconds();
        theta = delta_v.theta();
        resolve();
        units = new Unit("m/s²");
    }

        /*public Accel(Velocity velocity, Frequency frequency)
        {
          Time time = new Time(MyMath.recip(frequency.Hertz()));
          magnitude = (6.2831853071795862D * velocity.magnitude()) / time.Seconds();
          units = "m/s^2";
	}*/

    //
    // CALCULATE
    ///////////////
    public Accel plus(Accel accel)
    {
        resolve();
        double d = x_magnitude + accel.x_magnitude;
        double d1 = y_magnitude + accel.y_magnitude;
        Accel accel1 = new Accel(Math.sqrt(Math.pow(d, 2D) + Math.pow(d1, 2D)), Math.atan(d1 / d));
        if(d < 0.0D) accel1.magnitude *= -1D;
        accel1.theta.units.set("radians", "rad");
        return accel1;
    }

    public Accel minus(Accel accel)
    {
	accel.set(accel.magnitude() * -1D);
        accel.resolve();
        return this.plus(accel);
    }

    public Velocity times(Time time)
    {
        return new Velocity(magnitude * time.Seconds(), theta());
    }

    public void convertToMPHperS()
    {
        if(units.abbrev.equals("m/s²")){
	    units.set("miles per hour per second", "mph/s");
            magnitude *= 2.2369363;
        }
    }

    public void convertToMperS()
    {  
	if(units.abbrev.equals("mph/s")){
	    units.set("meters per second per second", "m/s^2");
            magnitude /= 2.2369363;
        }
    }


    //
    // I/O
    /////////
    public Scalar getScalar()
    {
	return new Scalar(magnitude, units);
    }

    public void PromptUser()
    {
        System.out.print("(m/s²)?");
        set(Keyboard.readDouble());
        if(magnitude != 0.0D) theta.PromptUser();
        resolve();
    }

    public String SIformat()
    {
        return format();
    }

    public String USFormat()
    {
        return format() + ", at " + theta.degreeFormat();
    }

    public String SIfullFormat()
    {
        return format() + ", at " + theta.degreeFormat();
    }

    public String USfullFormat()
    {
        return format() + ", at " + theta.degreeFormat();
    }

    public String str()
    {
        return format() + ", at " + theta.degreeFormat();
    }

    public void printFull()
    {
        System.out.println(str());
    }

    public void printout()
    {
        System.out.print("acceleration = ");
        if(magnitude == 0.0D) System.out.println(0);
	else printFull();
    }

    public void ScalarPrintout()
    {
        System.out.print("avg. acceleration = ");
        if(magnitude == 0.0D)  System.out.println(0);
        else System.out.println(format());
    }
}
