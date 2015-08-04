//import java.io.*;

public class PolyTest{
  public static void main(String[] args){
      Polynomial p = new Polynomial();
      String[] options = {"Add term", "Print polynomial", "Evaluate", "Exit"};

      NumMenu mainMenu = new NumMenu(options);
      while(true){
	  //      mainMenu.displayOptions();
          switch(mainMenu.getSelection(true)){
            case 1: 
              p.addTerm(new Term(Keyboard.readDouble("coef:"), Keyboard.readDouble("pow:")));
              System.out.println("\n" + p.getString());
              break;

            case 2:
	      System.out.println("\n" + p.getString());
	      break;

 	    case 3: 
              double d = Keyboard.readDouble("x: ");
              System.out.println("\nf(" + TuiTeX.format(d) + ") = " + TuiTeX.format(p.eval(d)));
	      break;

	    case 4:
 	      System.exit(0);

            default:
         }
      }
   }
}
