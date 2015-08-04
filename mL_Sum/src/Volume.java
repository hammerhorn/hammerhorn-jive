public class Volume extends Scalar {
    //
    // CONSTRUCTORS
    //////////////////

    public Volume( ){
       magnitude = 0.0D;
       units = new Unit("liters", "L");
    }

    public Volume(double d){
        magnitude = d;
        units = new Unit("milliliters", "mL");
    }
 

    //
    // GET & SET
    ///////////////

    public double liters(){
        return magnitude/1000;
    }

    public double ml(){
        return magnitude;
    }



    //
    // CALCULATE
    ///////////////

    public Volume plus(Volume l){
	return new Volume(magnitude += l.ml());
    }
	

    //
    // I/O
    /////////

    public void printout(){
        System.out.println("volume = " + TuiTeX.format(magnitude) + " " + units);
    }
}
