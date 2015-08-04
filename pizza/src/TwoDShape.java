public class TwoDShape extends Thing
{
    protected Area a;
    protected displacement perimeter;

    public TwoDShape()
    {
        a = new Area();
        perimeter = new displacement();
    }

    public void askUser()
    {
        System.out.print("Area?");
        a = new Area(Keyboard.readDouble());
        System.out.print("Perimeter?");
        perimeter = new displacement(Keyboard.readDouble());
    }
}
