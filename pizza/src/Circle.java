//import java.io.PrintStream;

public class Circle extends TwoDShape{
    //
    // STATIC METHODS
    ///////////////////
    public static double area(double d){
        return 3.1415926535897931D * d * d;
    }

    static int count = 0;
    
    //
    // ATTRIBUTES
    ///////////////
    displacement radius;
    Point center;

    //
    // CONSTRUCTORS
    /////////////////
    public Circle(){
	count++;
        setLabel("CIRCLE #" + count);
	    center = new Point(0.0D, 0.0D);
        radius = new displacement();
        perimeter = new displacement();
        a = new Area();
    }

    public Circle(double r)
    {
	count++;
	    setLabel("CIRCLE #" + count);
        center = new Point(0.0D, 0.0D);
        radius = new displacement(r);
        perimeter = new displacement(r * 2D * 3.1415926535897931D);
        a = findArea();
    }
    
    public Circle(double r,String SIorUS)
    {
	count++;
	    setLabel("CIRCLE #" + count);
        center = new Point(0.0D, 0.0D);
        radius = new displacement(r);
        perimeter = new displacement(r * 2D * 3.1415926535897931D);
        a = findArea(SIorUS);
    }
      
    
    public Circle(displacement r, Point c)
    {
	count++;
	    setLabel("CIRCLE #" + count);
        radius = r;
        center = c;
        perimeter = radius.times(2D).times(3.1415926535897931D);
        a = findArea();
    }

    public Circle(displacement r, Point c, String SIorUS)
    {
        radius = r;
        center = c;
        perimeter = radius.times(2D).times(3.1415926535897931D);
        a = findArea(SIorUS);
    }
    
    

    //
    // GET & SET
    //////////////
    public double AreaDouble()
    {
        return a.magnitude;
    }



    //
    // CALCULATE
    //////////////
    public boolean onTest(Point point)
    {
        return point.y_magnitude() < 0.001D + center.y_magnitude() + Math.sqrt(MyMath.square(radius.magnitude()) - MyMath.square(point.x_magnitude() - center.x_magnitude())) && point.y_magnitude() > -0.001D + center.y_magnitude() + Math.sqrt(MyMath.square(radius.magnitude()) - MyMath.square(point.x_magnitude() - center.x_magnitude()));
    }

    public double eval(double d){
        return center.y_magnitude() + Math.sqrt(MyMath.square(radius.magnitude()) - MyMath.square(d - center.x_magnitude()));
    }

    protected Area findArea()
    {
        return new Area(this);
    }
    
    protected Area findArea(String s)
    {
        return new Area(this,s);
    }



    //
    // I/O
    ////////
    public void radiusPrompt()
    {
        System.out.print("\nradius in " + (new displacement()).units + "?");
        double d = Keyboard.readDouble();
        radius = new displacement(d);
        perimeter = new displacement(d * 2D * 3.1415926535897931D);
        a = findArea();
    }

    public void print()
    {
        System.out.println("\n           CIRCLE");
        System.out.println("       diameter = " + radius.times(2D).format());
        System.out.print("           ");
        a.printout();
        System.out.println("  circumference = " + perimeter.format() + "\n");
    }

    public void print(String u)
    {
	/*String w;
	if(u.equals("SI")) w="m^2";
	else if(u.equals("US"))w="ft^2";
	else w = "??";*/

        System.out.println("\n           CIRCLE");
        System.out.println("       diameter = " + radius.times(2D).format(u));
        System.out.print("           ");
        //a.printout(w);
	    a.printout();
        System.out.println("  circumference = " + perimeter.format(u) + "\n");
    }
}

