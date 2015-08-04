public class newchord{
   public static void main(String[] args){
      boolean exists;
      int [] newchord = new int[4];
      int number;
      int notecount = 4;
 
      //Populates the array with 12 unique numbers
      newchord[0] = 1 + (int)(Math.random() * 12);

      for(int count = 1; count < notecount; count++){
         exists = false;
         number = 1 + (int)(Math.random() * 12);
         for(int j = 0; j < notecount; j++){
	    if(number == newchord[j]){ 
               exists = true;
               count--;
            }
         }
	 if(! exists) newchord[count] = number;
      } 

      //Prints the array out as a nicely formatted list
      //      System.out.print("{");
      for(int count = 0; count < notecount; count++){
	 System.out.print(newchord[count] + " ");
      }
      System.out.println();
  }
}
