public class Angle extends Scalar{
   //
   // DATA 
   //////////
   static int count = 0;
	
   protected void initialize(String someText){
       count++;
       setLabel(someText);
   }
	
   //
   // CONSTRUCTORS
   /////////////////
   public Angle() {
	initialize("ANGLE #" + count);
	   
        units = new Unit("radians", "rad");
        magnitude = 0;
    }
        
    public Angle(double d) {
        initialize("ANGLE #" + count);
        setByRadians(d);
     }

    public Angle(String system, double measure) {
        count++;
	setLabel("ANGLE #" + count);
	
        if(system.equals("rad")) { 
   	   units=new Unit("radians", "rad");
           setByRadians(measure);
        }

        else if(system.equals("deg")) {
	   units=new Unit("degrees", "°");
           setByDegrees(measure);
        }
    }  


    //
    // GET & SET
    //////////////
    public double radians() {
        if(units.label.equals("degrees")) return Math.toRadians(magnitude);
        else if (units.label.equals("radians")) return magnitude;
        else return 0.0D;
    }

    //This is a fix, not something that makes sense
    public double degrees() {
        if (units.label.equals("degrees")) return magnitude;
   	    else if (units.label.equals("radians")) return Math.toDegrees(magnitude);
	    else return  0;
    }

    public double radiansPi() {
        return radians()/MyMath.PI;
    }

    public double[] degsMinsSecs() {
        double dms[] = new double[3];
        dms[0] = (int)degrees();
        dms[1] = ((int)minutes()) % 60;
        dms[2] = ((int)seconds()) % 3600 - dms[1] *60;
        return dms;
    }

    public double minutes() {
        return degrees() * 60D;
    }

    public double seconds() {
        return degrees() * 3600D;
    }

    public void setByDegrees(double d) {
        magnitude = d;
        units = new Unit("degrees", "deg");
    }

    public void setByRadians(double d) {
       magnitude = d;
       units = new Unit("radians", "rad");
    }


    //
    // CALCULATE
    //////////////
    public double slope() {
        return Math.tan(radians());
    }
    
    public Angle compliment() {
        return new Angle("deg", 90.0 - degrees());
    }

    public Angle supplement() {
        return new Angle("deg", 180.0 - degrees());
    }


    //
    // I/O
    ////////
    public void PromptUser() {
        System.out.print("theta(°)?");
        setByDegrees(Keyboard.readDouble());
    }

    public String degreeFormat() {
        return TuiTeX.format(degrees()) + "°";
    }

    public String SIformat() {
        return TuiTeX.format(radians()) + " radians";
    }

    public String str(){
	return degreeFormat() + "/" + SIformat();
    }

    public void printout() {
        System.out.println(" th = " + degreeFormat());
    }

   //Print degrees, radians, pi radians
   public void print() { 
       System.out.printf("%7s° = ", TuiTeX.format(degrees()));
       System.out.printf("%6s (i.e., ", TuiTeX.format(radians()));
       System.out.printf("%6sπ) radian(s)\n", TuiTeX.format(radiansPi()));
   }

   public void printDegsMinsSecs(){
       System.out.println(DegsMinsSecsf());
   }   

   public String DegsMinsSecsf(){
       String s = "";
      for(int x = 0; x < 2; x++){
	  s += (int)degsMinsSecs()[x];    
	  if(x==0) s += ("° ");
	  else if (x==1) s += ("\' ");
      }
      s+=(degsMinsSecs()[2]+"\"");
      return s;
   }   

   public void printoutDegsMinsSecs(){
      double [] dms = degsMinsSecs().clone();
      System.out.print((int)dms[0] + " degree");
      if((int)dms[0] != 1) System.out.print("s");
      System.out.print(", " + (int)dms[1] + " minute");
      if((int)dms[1] != 1) System.out.print("s");
      System.out.print(", ");
      System.out.println("and " + dms[2] + " seconds");
   }

   public void printBrief() {
      this.printSlope();
   }

   public void printDetailed() {
      TuiTeX.hfill(19);
      this.printSlope();
      TuiTeX.hfill(17);
      System.out.println(TuiTeX.emph(this.DegsMinsSecsf()));
      TuiTeX.vspace();
      TuiTeX.hfill(6);
      this.print();
      TuiTeX.hrule(49);      
      System.out.print("comp: ");
      this.compliment().print();
      System.out.print("supp: ");
      this.supplement().print();
      TuiTeX.vspace(1);
   }
    
   public void printSlope() {      
      if(Math.abs(degrees() % 180)==90) System.out.println("no slope");
      else System.out.println("m = " + TuiTeX.format(this.slope()));
   }
}
