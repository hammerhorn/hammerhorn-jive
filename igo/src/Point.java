public class Point extends MyVector
{	
   protected static int count=0;

   String marker; //"white", "black", or "none"

//This class has issues!!!	
   protected void initialize(){
      count++;
      units  = new Unit();
      marker = "none";
   }

   public Point(){
      initialize();
      label  = "POINT #" + count;	   
      theta  = new Angle();
      magnitude = 0.0D;
   }

   public Point(String s){
      initialize();
      label = s;
      theta = new Angle();
      magnitude = 0.0D;
   }

   public Point(double d){
      initialize();
      label = "POINT #" + count;	   
      theta = new Angle();
      magnitude = d;
      resolve();
   }
    
   public Point(double x, double y){
      initialize();
      label = "POINT #" + count;	     
      x_magnitude = x;
      y_magnitude = y;
      this.assign(new MyVector(Math.sqrt(Math.pow(x,2) + Math.pow(y,2)), Math.atan(y/x)));
      if(x < 0.0D) this.magnitude *= -1D;
      theta.units.set("radians", "rad");
   }
    
   public Point(double d, Angle angle){
      initialize();
      label = "POINT #" + count;	   
      theta = angle;
      magnitude = d;
      resolve();
   }
    
   public Point(MyVector myvector){
      initialize();
      magnitude = myvector.magnitude();
      theta = myvector.theta();
      x_magnitude = myvector.x_magnitude;
      y_magnitude = myvector.y_magnitude;
   }

   public void numericPrint(){
      System.out.print("(" + TuiTeX.format(x_magnitude) + ", " + TuiTeX.format(y_magnitude) + ")");  
   } 

    public static void resetCounter(int i){ count = i; //System.out.println("Resetting counter to "+count); 
	    }

   public void printXandY(){
      System.out.println(" (" + TuiTeX.format(x_magnitude) + ", " + TuiTeX.format(y_magnitude) + ")");
   } 

   public void PromptUser(){
      // System.out.println("PromptUser");
      System.out.print("x: ");
      x_magnitude = Keyboard.readDouble();
      System.out.print("y: ");
      y_magnitude = Keyboard.readDouble();
      this.assign(new MyVector(Math.sqrt(Math.pow(x_magnitude,2) + Math.pow(y_magnitude,2)), Math.atan(y_magnitude/x_magnitude)));
      count--;
      //      resetCounter(0);
      if(x_magnitude < 0.0D) this.magnitude *= -1D;
      theta.units.set("radians", "rad");
   }

   public void print_mag(){
      System.out.print(magnitude);
   }

   public void print(){
      PrintLabel();
      printXandY(); 
      System.out.print("\nDistance from origin = ");
      println();
   }
}
