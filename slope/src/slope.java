public class slope{
  public static void main(String[] args){
      //////////////////////////////////
      // DECLARATION & INITIALIZATION //
      //////////////////////////////////
      Angle a = null;
      String[] prompts = new String[1];
      // String errorMessage="Usage: java angle <degrees>    or    java angle -r <radians>";
      prompts[0] = "degrees";
      boolean inRadians = false;
	  
      MyOpts Argz = new MyOpts(1,args,prompts);

      ////////////////////////////////////////////////////////////////////////////
      // IF THE FIRST ARGUMENT IS -r , THROW IT AWAY AND GET DATA INTERACTIVELY //
      ////////////////////////////////////////////////////////////////////////////
      if(Argz.detectShortOption('r')){
         inRadians = true;
         prompts[0] = "radians";	
         if(Argz.length() == 1) Argz = new MyOpts(1, new String[0], prompts);	      
      }
   

      ///////////////////////////////////
      // STRIP FLAGS OUT FROM THE DATA //
      ///////////////////////////////////
      Argz = Argz.stripFlags();


      /////////////////////
      // MAKE AN Angle() //
      /////////////////////
      String system = "deg";
      if(inRadians) system = "rad";
      a = new Angle(system, Argz.getAsDouble(0));
      

      /////////////////////
      // PRINT THE SLOPE //
      /////////////////////
      System.out.println();
      a.printSlope();
      System.out.println();
   }
}
