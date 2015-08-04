
 //////////////////////////////////////
 // Class: Term                      //
 // <Term> is a monomial expression. //
 //////////////////////////////////////

public class Term extends Thing{
    double coef, exp;


    // 
    // CONSTRUCTORS
    //////////////////
    public Term( ){
	set(1, 1);
    }


    public Term(double n1, double n2){
	set(n1, n2);
    }


    //
    // GET & SET
    ///////////////
    public void set(double n1, double n2){
	coef = n1;
	exp = n2;
    }


    public double eval(double x){
	return coef * Math.pow(x, exp);
    }


    // 
    // I/O
    /////////
    public void println(){
	System.out.println(getString());
    }


    //There is probably a more elegant way....
    public String getString(){
        String s = "";

        //Add coef to string if necessary
        if(coef != 1.0 || exp == 0.0) s += TuiTeX.format(coef);

        if(coef != 0.0 && exp != 0.0){ 
            //Add variable 'x'
            s += "x";

            //Add exponent           
            if(exp != 1.0) s+= "^" + TuiTeX.format(exp);
	}
        return s;
    }
}




