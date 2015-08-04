//import java.io.*;

public class NoteTest 
{
   public static void main(String[] args)
   {
      Note n1 = new Note(440),
	   n2 = new Note("A#", 3, 0.0),
	   n3 = new Note(2, 3);


       n1.print();
          TuiTeX.hrule();	   
       n1.niceprint();
       System.out.println();
          TuiTeX.hrule();	   
       n1.troubleshoot();
          TuiTeX.hrule();	   
       n1.printHalfsteps();
          TuiTeX.hrule();	   
       n1.printall();
          TuiTeX.hrule();	   
       n1.printfreq();
          System.out.println('\n');

       n2.print();

       n3.print();
   }
}
