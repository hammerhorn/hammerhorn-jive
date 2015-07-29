import java.util.*;

public class TwoD6
{
    //It would be nice to aabstract this out to larger sets of dice
    public Die left,
               right;

    // 
    // CONSTRUCTORS
    //////////////////

    public TwoD6()
    {
        left = new Die();
        right = new Die();
    }


    //
    // GET & SET
    ///////////////

    public void roll()
    {
        left.roll();
        right.roll();
    }

    //   public static void rollAll(){}?

    // 
    // I/O
    /////////
    public  int value()
    {
        return left.value() + right.value();
    }

    public void printValue()
    {
        System.out.print(value());
    }

    public void printlnValue()
    {
        System.out.println(value());
    }

    public void print()
    {
        Formatter fmt = new Formatter();
        fmt.format("%d = %d + %d", (left.value() + right.value()), left.value(), right.value());
        System.out.println(TuiTeX.box('.', fmt.toString(), 5));

        if(left.value() == 1 && right.value() == 1) {
           TuiTeX.hfill(3);
           TuiTeX.subheading("snake eyes");
        }
    }    

    public void drawFaces()
    {
	left.generateFace();
	right.generateFace();
	for(int x = 0; x < 5; x++){
	    System.out.print(' '+left.face[x] + "   ");
	    if(x==2 && left.value() == right.value())
                System.out.print('=');
	    else
                System.out.print(' ');
	    System.out.println("   " + right.face[x]);
        }
	System.out.println();
    }
}
