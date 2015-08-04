public class Scale extends Thing
{
    Note [] seq = null;
    static int count = 0;
	
    // Create a 12-note chromatic scale starting on middle C
    public Scale() {
	    count++;
	    setLabel("SCALE #" + count);
       seq = new Note[12];

       for(int c = 0; c < seq.length; c++) {
 	  int n = c + 3;
	  if(n >= 12) n-=12;
 	  seq[c]=new Note(n,4);
       }
    }


  public Scale(int no_of_notes)
  {
	  count++;
	  setLabel("SCALE #" + count);
     seq = new Note[no_of_notes];

     for(int c=0; c < seq.length; c++)
     {
	 //	 int n = count+3;

	 //	 if(n>=12)n-=12;

 	 seq[c]=new Note((c * 12 / no_of_notes),4);
     }
//(((index_of_7 + 1) /7) * 12)-1=index_of_12
  }

   public void printList(){     
      PrintLabel();
      for(int c = 0; c < seq.length; c++){
         seq[c].niceprint();
      }
   }
}