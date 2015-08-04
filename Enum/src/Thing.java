public class Thing{
	
   // FIELDS
   String label;
   static int ThingCount = 0;

   //CONSTRUCTORS
   public Thing(){
      initialize("THING #" + ThingCount);
   }

   public Thing(String s){
      initialize(s);
   }
    	    
   //GET & SET
   public void setLabel(String s){
      label = s;
   }

   public String str(){
   //  return '[' + label + ']';
      return "'" + label + "'";
   }
    
   //I/O
   public void PrintOldLabel(){
      TuiTeX.subheading(label);
   }

   public void PrintLabel(){
      TuiTeX.ul(label, 2, '=');
   }
   
   //Protected methods
   protected void initialize(String someText){
      ThingCount++;
      setLabel(someText);       
   }
}
