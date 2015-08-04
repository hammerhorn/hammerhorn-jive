public class displacement extends MyVector{	
   static int count=0;
	
   public displacement(){
      count++;
      label = "DISPLACEMENT #" + count;	   
      units = new Unit("meters","m");
      magnitude = 0.0D;
      theta = new Angle();
   }

   public displacement(String s){
      count++;
      label = s;
      units = new Unit("meters","m");
      magnitude = 0.0D;
      theta = new Angle();
   }

    public displacement(double d){
        count++;
        label = "DISPLACEMENT #" + count;	   
	units = new Unit("meters","m");
        magnitude = d;
        theta = new Angle();
        resolve();
    }
    
    public displacement(double d, double th){
	count++;
        label = "DISPLACEMENT #" + count;	     
        units = new Unit("meters","m");
        magnitude = d;
	if(d==0.0D){ theta=new Angle(); }
        else{ theta = new Angle("deg", th); }
        resolve();
    }
    
    public displacement(double d, Angle angle){
	count++;
        label = "DISPLACEMENT #" + count;	   
        units = new Unit("meters","m");
        magnitude = d;
        theta = angle;
        resolve();
    }
    
    public displacement(double d, String s){
	count++;
        label = "DISPLACEMENT #" + count;	   

        if(s.equals("US")){
	   units = new Unit("feet","ft");
	   magnitude = d * 0.30480000000000002D;
	} 

	else{
	   units = new Unit("meters","m");
	   magnitude = d;
	   if(!s.equals("SI")){
	      System.out.println("Setting displacement to METERS by default");
	   }
	}

        theta = new Angle();
        resolve();
    }
    
    public displacement(MyVector myvector){
	count++;
        magnitude = myvector.magnitude();
        theta = myvector.theta();
        x_magnitude = myvector.x_magnitude;
        y_magnitude = myvector.y_magnitude;
    }
    /*
    public displacement(Velocity velocity, Time time)
    {
        displacement displacement1 = new displacement(velocity.times(time));
        units = "m";
        magnitude = displacement1.magnitude();
        theta = displacement1.theta();
        resolve();
    }

    public displacement(Velocity velocity, Accel accel, Time time)
    {
        units = "m";
        magnitude = ((new displacement(velocity, time)).magnitude() + (new displacement(accel, time)).magnitude()) / 2D;
        resolve();
    }

    public displacement(Accel accel, Time time)
    {
        units = "m";
        magnitude = accel.times(time).times(time).magnitude();
        theta = accel.times(time).times(time).theta();
    }
    */

    public void assign(displacement v){
        units = v.units;
        magnitude = v.magnitude;
        theta = v.theta;
    }




    public double Inches()
    {
        units = new Unit("inches","in");
        return Feet() * 12D;
    }

    public double Feet()
    {
        units = new Unit("feet","ft");
        return magnitude * 3.2808398950000002D;
    }

    public double Miles()
    {
        units = new Unit("miles","mi");
        return magnitude / 1609.3440000000001D;
    }

    public double Meters()
    {
        units = new Unit("meters","m");
        return magnitude;
    }

    //This function isnt ready yet
    public displacement vplus(displacement myvector)
    {
        //System.out.println(MyFormat.banner('*',-30,label + " + " + myvector.getLabel()));

        System.out.println(TuiTeX.box('#', str() + " + " + myvector.str()));

        this.print();
        System.out.println("\n" + TuiTeX.box('+',-24, "PLUS"));
        myvector.print();
        System.out.println("\n"+ TuiTeX.box('=',-24,"EQUALS"));

        displacement myvector1 = this.plus(myvector);

        myvector1.print();
        System.out.println();
        return myvector1;
    }

    public displacement plus(displacement displacement1)
    {
	//        System.out.println(MyFormat.banner('#', getLabel() + " + " + displacement1.getLabel()));
	//			System.out.println(getLabel() + " + " + displacement1.getLabel());

        resolve();
        double d = x_magnitude + displacement1.x_magnitude();
        double d1 = y_magnitude + displacement1.y_magnitude();

        displacement displacement2 = new displacement(Math.sqrt(Math.pow(d, 2D) + Math.pow(d1, 2D)), Math.atan(d1 / d));
	if(d < 0.0D){displacement2.magnitude *= -1D;}
	displacement2.theta.units.set("radians", "rad");
        return displacement2;
    }

    public displacement minus(displacement displacement1)
    {
	displacement1.set(displacement1.magnitude() * -1D);
        displacement1.resolve();
        return this.plus(displacement1);
    }

    public void printXandY()
    {
        System.out.print("\n  X Component: ");
        (new displacement(xVector())).print_mag();
        System.out.print("\n  Y Component: ");
        (new displacement(yVector())).print_mag();
    }

    /*    public Velocity per(Time time)
    {
        return new Velocity(magnitude / time.Seconds(), theta);
	}*/

    public displacement times(double d)
    {
        return new displacement(magnitude * d, theta);
    }

    public void setByFeet(double d)
    {
        magnitude = d / 3.2807999790000002D;
    }

    public void PromptUser(String s)
    {
        System.out.print("(" + giveUnits(s) + ")?");

        if(s.equals("SI")){
	   set(Keyboard.readDouble());
	} 

        else if(s.equals("US")){
           setByFeet(Keyboard.readDouble());
	}
 
        else{
	 System.err.println("Method Failed -- diplacement::PromptUser(String)");
	}

        if(magnitude != 0.0D){
	   theta.PromptUser();
	}

        resolve();
    }

    public void PromptUser(){
	System.out.print(units.str() + ":");
        magnitude = Keyboard.readDouble();
        System.out.print("degrees:");
        theta.setByDegrees(Keyboard.readDouble());
    }




    public void PromptScalar(String s)
    {
        System.out.print("(" + giveUnits(s) + ")?");
        if(s.equals("SI"))
	    {
		set(Keyboard.readDouble());
	    } else
	    if(s.equals("US"))
		{
		    setByFeet(Keyboard.readDouble());
		} else
		{
		    System.err.println("Method Failed -- diplacement::PromptUser(String)");
		}
    }

    String giveUnits(String s)
    {
        if(s.equals("US"))
	    {
		return "ft";
	    } else
	    {
		return "m";
	    }
    }

    public String USformat()
    {
        if(Math.abs(Feet()) >= 5280D)
	    {
		return TuiTeX.format(Miles()) + " mi";
	    }
        if(Math.abs(Feet()) >= 1.0D)
	    {
		return TuiTeX.format(Feet()) + " ft";
	    } else
	    {
		return TuiTeX.format(Inches()) + " in";
	    }
    }

    public String USfullFormat()
    {
        return USformat() + ", at " + theta.degreeFormat();
    }

    public void print_mag(String s)
    {
        if(s.equals("SI"))
	    {
		SIprint();
	    } else
	    if(s.equals("US"))
		{
		    USprint();
		} else
		{
		    System.err.print("Unknown unit system error");
		}
    }

    /* public void println(String s)
    {
	        print_mag(s);
	
		}*/

    public void print()
    {
	SIprint();
    }

    public void USprint()
    {
        System.out.print(USformat());
    }

    public void USprintln()
    {
        System.out.println(USformat());
    }

    public void USprintFull()
    {
        System.out.println(USfullFormat());
    }

    public String SIformat()
    {
        return TuiTeX.format(magnitude) + " m";
    }

    public String SIfullFormat()
    {
        return SIformat() + ", at " + theta.degreeFormat();
    }

    public void SIprint()
    {
        System.out.print(format());
    }

    public void SIprintln()
    {
        System.out.println(format());
    }

    public void SIprintFull()
    {
        System.out.println(SIfullFormat());
    }

    public String format()
    {
        if(units.equals("SI") || units.equals("m"))
	    {
		return SIformat();
	    }
        if(units.equals("US") || units.equals("ft") || units.equals("mi"))
	    {
		return USformat();
	    } else
	    {
		return SIformat() + " (" + USformat() + ")";
	    }
    }

    public String format(String u)
    {units=new Unit(u,u);
        if(units.abbrev.equals("SI") || units.abbrev.equals("m"))
	    {
		return SIformat();
	    }
        if(units.abbrev.equals("US") || units.abbrev.equals("ft") || units.abbrev.equals("mi"))
	    {
		return USformat();
	    } else
	    {
		return SIformat() + " (" + USformat() + ")";
	    }
    }

    /*    public String fullFormat()
    {
        return format() + ", at " + theta.degreeFormat();
	}*/

    public void print_mag()
    {
        if(units.abbrev.equals("m") || units.abbrev.equals("SI"))
	    {
		SIprint();
	    } else
	    if(units.abbrev.equals("US") || units.abbrev.equals("ft") || units.abbrev.equals("mi"))
		{
		    USprint();
		} else
		{
		    System.out.print(SIformat() + " (" + USformat() + ")");
		}
    }

    public void println_mag()
    {
        print_mag();
        System.out.println();
    }

    public void printFull()
    {
        if(units.abbrev.equals("SI") || units.abbrev.equals("m"))
	    {
		SIprintFull();
	    } else
	    if(units.abbrev.equals("US") || units.abbrev.equals("ft") || units.abbrev.equals("mi"))
		{
		    USprintFull();
		} else
		{
		    System.out.println(SIformat() + " (" + USformat() + "), at " + theta.degreeFormat());
		}
    }

    public void printFull(String s)
    {
        if(s.equals("SI"))
	    {
		SIprintFull();
	    } else
	    if(s.equals("US"))
		{
		    USprintFull();
		} else
		{
		    System.out.println(SIformat() + " (" + USformat() + "), at " + theta.degreeFormat());
		}
    }

    public void printout(String s)//s="SI" or "US"
    {
        System.out.print("displacement = ");
        if(magnitude == 0.0D)
	    {
		System.out.println(0);
	    } else
	    {
		printFull(s);
	    }
    }

    /*    public displacement contracted(Velocity velocity)
    {
        return new displacement(magnitude * velocity.gamma());
	}*/
}
