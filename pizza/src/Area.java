public class Area extends Scalar
{
    public Area()
    {
        units = new Unit("square meters", "m^2");
        magnitude = 0.0D;
    }

    public Area(double d)
    {
        units = new Unit("square meters", "m^2");
        magnitude = d;
    }

    public Area(Circle circle)
    {
        units = new Unit("square meters", "m^2");
        magnitude = Math.pow(circle.radius.magnitude(), 2D) * 3.1415926535897931D;
    }

    public Area(Circle circle, String s)
    {
        if(s.equals("SI"))
	    {
		units = new Unit("square meters", "m^2");
		magnitude = Math.pow(circle.radius.Meters(), 2D) * 3.1415926535897931D;
	    } else
	    if(s.equals("US"))
		{
		    units = new Unit("square feet", "ft^2");
		    magnitude = Math.pow(circle.radius.Feet(), 2D) * 3.1415926535897931D;
		} else
		{
		    units = new Unit();
		}
    }

    public void printout()
    {
        System.out.print("area = ");
        println();
    }

 /*   public void printout(String s)
    {
        units = s;
        System.out.print("area = ");
        println();
    }*/
}
