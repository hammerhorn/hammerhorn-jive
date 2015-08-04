public class Pizza{
   public static void main(String[] args){
        //VARIABLES
        String [] prompts = {"diameter(in.)?", "price($)?"};
        MyOpts i = new MyOpts(2, args, prompts);
	double dollars = i.getAsDouble(1);
	displacement d = new displacement(i.getAsDouble(0)/24, "US");
	Circle circle = new Circle(d, new Point(),"US");
     
	//CALCULATE & WRITE TO SCREEN  
        System.out.println(TuiTeX.money(dollars / (circle.AreaDouble() * 144)) + "/sq in");  //144 sq in = 1 sq ft
  }
}
