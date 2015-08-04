import java.text.DecimalFormat;


public class Time extends Scalar
{
    // 
    // CONSTRUCTORS
    //////////////////
    public Time( )
    {
    }

    public Time(double t)
    {
       units = new Unit("seconds", "s");
       magnitude = t;
    }

    public Time(String MmSs)
    {
        units=new Unit("seconds", "s");
	//int minutes, bareSeconds;
	String [] splitString = MmSs.split(":");
	if(splitString.length==1) magnitude = Integer.parseInt(splitString[0])*60;
        else magnitude = Integer.parseInt(splitString[1]) + Integer.parseInt(splitString[0])*60;        
    }


    //
    // GET & SET
    ///////////////
    public void set(double d){magnitude = d;}
    public double Seconds(){return magnitude;}
    public double Minutes(){return magnitude/60.0;}
    public int bareMinutes(){return (int)Minutes();}
    public double bareSeconds(){return Seconds() - 60 * bareMinutes();}



    // 
    // I/O
    /////////
    public void print()
    {
       DecimalFormat secondsformat = new DecimalFormat("00.####");
       System.out.print(bareMinutes() + ":" + secondsformat.format(bareSeconds()));
    }
}
