
public class ParabolaTest
{
  public static void main(String[] args)
  {
     System.out.print("Vertex x:");
     double vx = Keyboard.readDouble();

     System.out.print("Vertex y:");
     double vy = Keyboard.readDouble();    
 
     System.out.print("x-intercept:");
     double xi = Keyboard.readDouble();     

     Parabola p = new Parabola(vx,vy,xi);
     
     while(true){
        System.out.print("x = ");
        double x = Keyboard.readDouble();
        System.out.println("  Upward:("+x + ", "+p.f_of_x1(x)+")");
        System.out.println("Downward:("+x + ", "+p.f_of_x2(x)+")");
     }




  }
}
