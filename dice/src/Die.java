public class Die extends Thing
{
    static int count = 0;
    public int sides,
               value;
    String face[];

    // 
    // CONSTRUCTORS
    //////////////////

    protected void initialize(int x)
    {
        sides = x;	
        count++;
        setLabel("DIE #" + count + " (d" + sides + ")");
        roll();
        face = new String[5];
    }

    public Die()
    {
       initialize(6);
    }

    public Die(int n)
    {
        initialize(n);
    }

    protected void clearFace()
    {
        face[0] = " ----- ";
        face[1] = "|     |";
        face[2] = "|     |";
        face[3] = "|     |";
        face[4] = " ----- ";
    }


    //
    // GET & SET
    ///////////////

    public void roll()
    {
        value = (int)(Math.random() * sides + 1);
    }

    public void setFace(int face)
    {
        value = face;
    }

    //   public static void rollAll(){}?

    // 
    // I/O
    /////////
    public  int value()
    {
        return value;
    }

    public void printValue()
    {
        System.out.print(value);
    }

    public void printlnValue()
    {
        System.out.println(value);
    }

    public void display()
    {
        System.out.println();
        PrintLabel(); 
        System.out.printf("%12d\n", value);
    }    

    public void generateFace()
    {
        clearFace();
        if(value() == 1)
            face[2] = "|  *  |";
        else if(value() == 2){
            face[1] = "|    *|";
            face[3] = "|*    |";
        }
        else if(value() == 3){
            face[1] = "|    *|";
            face[2] = "|  *  |";
            face[3] = "|*    |";
        }
        else if(value() == 4){
            face[1] = "|*   *|";
            face[3] = "|*   *|";
        }
        else if(value() == 5){
            face[1] = "|*   *|";
            face[2] = "|  *  |";
            face[3] = "|*   *|";
        }
        else if(value() == 6){
            face[1] = "|*   *|";
            face[2] = "|*   *|";
            face[3] = "|*   *|";
        }
    }

    public void drawFace()
    {
	generateFace();
        /*else if(value==2)face = " -----\n|    *|\n|     |\n|*    |\n -----\n";
        else if(value==3)face = " -----\n|    *|\n|  *  |\n|*    |\n -----\n";
        else if(value==4)face = " -----\n|*   *|\n|     |\n|*   *|\n -----\n";
        else if(value==5)face = " -----\n|*   *|\n|  *  |\n|*   *|\n -----\n";
        else if(value==6)face = " -----\n|*   *|\n|*   *|\n|*   *|\n -----\n";
        else face = "[No image available]\n";*/

	for(int x = 0; x < 5; x++)   System.out.print("\n" + face[x]);

    }

    public void PrintLabel()
    {
        TuiTeX.ul(label, 5, '=');
    }
}
