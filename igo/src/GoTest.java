public class GoTest {

    // DATA
    static boolean artMode = false,
                      quietMenu = false;
    static goban GB1 = new goban();
    static Point A = null;

    // MAIN METHOD
    public static void main(String[] args) {
        MyOpts Args = new MyOpts(args);

        

        if( Args.detectShortOption('a')) { 
	    System.out.println("[art mode]\n");
            artMode = true;
        }
        else { 
            System.out.println("[goban mode]\n");
        }

        if (Args.detectShortOption('q')){
            quietMenu = true;
        }


        compositePrint();
        TuiTeX.vspace(2);

        Point.resetCounter(-1); //This is a baffling workaround :-/

        String[] MenuOptions = {"Add/remove stones", "Change skin", "Exit"};
        int selection;

        NumMenu MainMenu = new NumMenu(MenuOptions);

        for(int i = 0; i < 100; i++){
            selection = MainMenu.getSelection(!quietMenu);

            switch(selection){
	      case 1 :
                String[] opts = {"Add black", "Add white", "star", "erase"};
                NumMenu StoneMenu = new NumMenu(opts);
		int sel = StoneMenu.getSelection(!quietMenu); 

		newPointPrompt();
                TuiTeX.vspace();               

                switch(sel){
		  case 1:
                    GB1.markPointBlack(A);
                    break;
                    
                  case 2:
                    GB1.markPointWhite(A);
                    break;

                  case 3:
                    GB1.markPointStar(A);
                    break;

                  case 4:
                    GB1.erasePoint(A);
                    break;
                  default:
		}

                break;

	      case 2 :
                artMode = !artMode;
		break;
                
 	      case 3 :
		System.exit(0);

      	      default :
            }
	    compositePrint();
	}
    }

	    /*
            switch (selection){
  	    case 1 : 
	        newPointPrompt();
                TuiTeX.vspace();
                if(!artMode){
	            GB1.markPointBlack(A);
 	            compositePrint();

                    selection = MainMenu.getSelection();

                    switch (selection){
		    case 1 : 
		        newPointPrompt();                            
			GB1.markUnmarkWhite(A);
			break;    
		    case 2 :
                        newPointPrompt();
                        GB1.erasePoint(A);
			break;
                    case 3 :
                        System.exit(0);
		    default :
		    }

		    //compositePrint();
                }

  	        else GB1.markPointStar(A);
	        break;

	    case 2 :
                newPointPrompt();
	        GB1.erasePoint(A);
                break;
            case 3 :
                System.exit(0);

  	    default:
	    }

            compositePrint();
        }
   }

	    */

    protected static void newPointPrompt(){
        A = new Point(); 
        A.PromptUser();
    }
   
    protected static void compositePrint(){
        if(artMode) GB1.artPrint();
        else GB1.gobanPrint();
        if(A != null) A.print();
        TuiTeX.hrule();
        TuiTeX.vspace();
    } 
}
