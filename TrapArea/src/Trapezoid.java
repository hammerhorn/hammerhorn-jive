public class Trapezoid extends TwoDShape {

    double width, 
            base, 
          height;

    public Trapezoid() {
        do{
            System.out.print("width: ");
            width = Keyboard.readDouble();  
	}while (width < 0.0D);

        do{
            System.out.print("base: "); 
            base = Keyboard.readDouble();    
	}while(base < 0.0D);

        do{
            System.out.print("height: ");
            height = Keyboard.readDouble();
	}while(height < 0.0D);
        System.out.println();
        a = new Area(height * (width + base) / 2.0);
        //       perimeter= new displacement(2 * height + width + base);     
    }
   

    public Trapezoid(double w, double b, double h){
        if(w < 0.0 || b < 0.0 || h < 0.0){
	    System.err.println("Distances must be positive.");
            System.exit(-1);
        }
        width = w;
        base = b; 
        height = h;
        a = new Area(height * (width + base) / 2.0);
    }


    public void printArea(){
        a.printout();
    }

    //       perimeter.printFull();


    public void printout(){
	//PrintLabel();
	printArea();
	System.out.println();
    }

    public String classify(){
        if ((width == 0.0D && base != 0.0D) || (width != 0.0D && base == 0.0D)){
	    return "triangle";
        }
        else if (width== 0.0D && base == 0.0D){
            if(height == 0.0D) return "point";
            else return "line segment";
        }
	else if (width == base){
            if(height == 0) return "line segment";
	    if (width == height) return "square";
	    else return "rectangle";
	}
	else {
            if( height == 0.0D)return "not a figure";
	    else  return "trapezoid"; 
       }
   }
}


