//import java.io.PrintStream;

public class Scalar extends Thing
{

    // ATTRIBUTES
    ////////////////

    // protected Unit units;
    // protected double magnitude;

    public Unit units;
    public double magnitude;

    static int ScalarCount = 0;

    protected void initialize()
    {
	ScalarCount++;
	setLabel("SCALAR #" + ScalarCount);
    }


    // CONSTRUCTORS
    //////////////////
    public Scalar()
    {
       	initialize();
        units = new Unit();
        magnitude = 0;
    }

    public Scalar(double d, Unit u)
    {
       	initialize();
        units = u;
        magnitude = d;
    }


    // GET AND SET
    /////////////////
    public double magnitude()
    {
        return magnitude;
    }

    public void set(double d)
    {
        magnitude = d;
    }

    public void assign(Scalar s)
    {
	units = s.units;
	magnitude = s.magnitude;
    }


    // I/O
    /////////
    public void PromptUser()
    {
	System.out.print("units (full name): ");
	units.setLabel(Keyboard.readLine());
	System.out.print("abbreviation: ");
	units.abbrev = Keyboard.readLine();
	units.print();
        System.out.print(": ");
        magnitude = Keyboard.readDouble();
    }

    public String longform()
    {
        return TuiTeX.format(magnitude) + " " + units.str();
    }

    public String str()
    {
        return TuiTeX.format(magnitude) + " " + units.abbrev;
    }

    public void print()
    {
        System.out.print(str());
    }

    public void println()
    {
        System.out.print(str());
    }
}
