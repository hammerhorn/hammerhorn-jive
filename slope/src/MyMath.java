//import java.util.*;
//import java.io.PrintStream;
//import java.text.DecimalFormat;

public class MyMath{
    //    static final Mass Earth_mass = new Mass(5.9800000000000005E+024D);
    //static final displacement Earth_radius = new displacement(6370000D);
    //static final Accel g = new Accel(9.8000000000000007D);

    static final double G = 6.6729999999999999E-011D;
    static final double c = 299792458D;
    public static final double PI = 3.14159265358979323846;
 
    public MyMath(){}

    public static double log10(double d){
        return Math.log(d) / Math.log(10D);
    }

    public static double log(double d, double d1){
        return Math.log(d1) / Math.log(d);
    }

    public static double square(double d){
        return d * d;
    }

    public static double root(double d, double d1){
        return Math.pow(d1, recip(d));
    }

    public static double recip(double d){
        return Math.pow(d, -1D);
    }

    public static String toHex(int n){
        return Integer.toHexString(n);
        /*Formatter fmt = new Formatter();
        String s = "";
        fmt.format("%x", d);
        s = fmt.toString().toUpperCase();
        fmt.close();
	return s;*/
    }

    /*  public static String toBinary(double d)
    {
        String s = "";
        int i = (int)log(2D, d);
        s = s + 1;
        return s;
    }*/

    public static int truncate(double d){
        return (int)d;
    }
}
