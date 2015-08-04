public class MyVector extends Scalar{
    // 
    // DATA
    //////////
    static int count = 0;
    protected double x_magnitude, 
                     y_magnitude;
    protected Angle theta;

    protected void initialize(){
	//count++;
	setLabel("VECTOR #" + count);
	//        units = new Unit("magnitude");
	units = new Unit();
	//        System.err.println("Units = " + this.units.str());
    }

    protected void resolve(){
        x_magnitude = magnitude * Math.cos(theta.radians());
        y_magnitude = magnitude * Math.sin(theta.radians());
    }


    //
    // CONSTRUCTORS
    //////////////////

    // Constructor: universal
    public MyVector(){
        magnitude = 0.0D;
        theta = new Angle();
        count++;
	initialize();
        //System.err.println("Units = " + this.units.str());
        resolve();
	//        System.out.print("=> ");
        //this.println();
    }

    //Constructor: accepts two doubles, magnitude and degrees, as arguments
    public MyVector(double d, double degrees) {
	//        units = new Unit("magnitude");
        magnitude = d;
        if(d == 0.0D){ theta = new Angle("deg", 0.0D); } 
        else { theta = new Angle("deg", degrees); }
        count++;
	initialize();
        resolve();
        //System.out.print("=> ");
        //this.println();
    }

    //Constructor: takes a double for the magnitude and an Angle object 
    public MyVector(double d, Angle angle){
        magnitude = d;
        if(d == 0.0D){ theta = new Angle(); }
        else{ theta = angle; }
        count++;
	initialize();
        resolve();
        //System.out.print("=> ");
        //this.println();
    }


    //
    // GET & SET
    ///////////////

    //returns the magnitude
    public void assign(MyVector v){
        units = v.units;
	magnitude = v.magnitude;
	theta = v.theta; 
    }

    public double magnitude(){ 
       return magnitude; 
    }

    //return theta as an Angle object
    public Angle theta(){ 
        return theta; 
    }

    //Return slope as a double
    public double slope(){ 
        return theta.slope(); 
    }

    //Return the magnitude of the x component
    public double x_magnitude(){
        return x_magnitude;
    }

    //Return the x component as a MyVector object
    public MyVector xVector(){
        MyVector myvector = new MyVector();
        myvector.setMag(x_magnitude);
        myvector.setAngle(0.0D);
        return myvector;
    }

    //Return the magnitude of the y component
    public double y_magnitude(){
        return y_magnitude;
    }

    //Return the y component as a MyVector object
    public MyVector yVector(){
        MyVector myvector = new MyVector();
        myvector.setMag(y_magnitude);
        myvector.setAngle(MyMath.PI/2);
        return myvector;
    }

    //Set the magnitude with a double
    public void setMag(double d){
        magnitude = d;
    }

    //Set the angle in radians with a double
    public void setAngle(double d){
        theta = new Angle(d);
    }

    //Set the angle using the Angle object
    public void setAngle(Angle angle){
        theta = angle;
    }

    //Set the units label to the provided String
    public void setUnits(String s){
        units.set(s);
    }


    //
    // CALCULATE
    ///////////////

    //Add this vector to another and return the sum as an object
    public MyVector vplus(MyVector myvector){

	System.out.println(TuiTeX.box('#', this.label + " + " + myvector.label, 3));
	TuiTeX.vspace(1);
        this.print();
	//TuiTeX.vspace(1);
	//System.out.println(TuiTeX.box('+', "PLUS", 4));
        System.out.println(TuiTeX.box(' ', "+", 5));
	  //  TuiTeX.vspace(1);	
        myvector.print();
//	TuiTeX.vspace(1);
	System.out.println(TuiTeX.box(' ',"=", 5));
//TuiTeX.hrule(20);
	MyVector myvector1 = this.plus(myvector);

        TuiTeX.vspace(1);	
        myvector1.print();
	TuiTeX.vspace();

        return myvector1;
    }

    public MyVector vminus(MyVector myvector){
	System.out.println(TuiTeX.box('#', this.label + " - " + myvector.label, 3));
	TuiTeX.vspace(1);
        this.print();
	TuiTeX.vspace(1);
	System.out.println(TuiTeX.box('-', "minus", 4));
        TuiTeX.vspace(1);
        myvector.print();
	TuiTeX.vspace(1);
        System.out.println(TuiTeX.box('=',"equals", 4));
//TuiTeX.hrule(20);
	MyVector myvector1 = this.minus(myvector);

	TuiTeX.vspace(1);
	myvector1.print();
	TuiTeX.vspace();

        return myvector1;
    }

    public MyVector plus(MyVector myvector){
	//	System.out.println("Angle 1 is in " + theta.units.label + ", and Angle 2 is in " + myvector.theta.units.label + ".");
        if(theta.units.abbrev.equals(myvector.theta.units.abbrev)){
	    //        resolve();
           double d = x_magnitude + myvector.x_magnitude();
           double d1 = y_magnitude + myvector.y_magnitude();
           MyVector myvector1 = new MyVector(Math.sqrt(Math.pow(d, 2D) + Math.pow(d1, 2D)), Math.toDegrees(Math.atan(d1 / d)));

           if(d < 0.0D){
   	      myvector1.magnitude *= -1D;
	   }

 	   myvector1.theta.units.set(myvector.theta.units.label, myvector.theta.units.abbrev);
           return myvector1;
	}
        else{
	    System.err.println("ERROR: Unlike units -- Feature not yet implemented.");
            return null;
	}
    }

    //Subtract another vector from this one and return the difference
    // as an object
    public MyVector minus(MyVector myvector){
       myvector.set(myvector.magnitude() * -1D);
       myvector.resolve();
       return this.plus(myvector);
    }




    //
    // I/O
    /////////

    //Prompts user for data and sets current object accordingly
    public void PromptUser(){
        System.out.print("magnitude?");
        setMag(Keyboard.readDouble());
        if(magnitude != 0.0D){
	    theta.PromptUser();
	}
        resolve();
    }

    //Returns magnitude with units as a String
    public String format(){
        return TuiTeX.format(magnitude) + ' ' + units.abbrev;
    }

    //Returns magnitude and angle as a String
    public String str(){
       return TuiTeX.format(magnitude) + " " + units.str() + ", at " + theta.degreeFormat();
	//return MyFormat.column(magnitude,3) + " " + units.GiveString() + " at " + theta.degreeFormat();
    }

    //Print the x and y components to stdout
    public void printXandY(){
        System.out.println("  X Component = " + xVector().format());
        System.out.println("  Y Component = " + yVector().format());
        System.out.println("    m (slope) = " + TuiTeX.format(slope()));
    }

    //Print magnitude to stdout
    public void printMag(){
        System.out.print(TuiTeX.format(magnitude));

    }

    //Print magnitude and angle to stdout
    public void print(){
        PrintLabel();
	/*        System.out.println(" magnitude = " + TuiTeX.format(magnitude));
		  System.out.println("     theta = " + theta.degreeFormat());*/
        System.out.println("  " + str());
    }

    //Prints magnitude and angle to stdout
    public void println(){
        System.out.println(str());
    }

    //Print magnituded and angle along with x and y components
    public void printFull(){
        print();
        printXandY();
    }

    public void quickview(){
	System.out.println("\n" + label + "(" + str() + ")");
    }
}
