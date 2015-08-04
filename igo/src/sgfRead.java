import java.io.*;

public class sgfRead
{
    public sgfRead()
    {
    }

    public static void main(String args[])
    {
        FileReader filereader = null;
        FileWriter filewriter = null;

        int ai[] = new int[10];
        int prevByte = 0,
	    gameCount = 0,
            i2 = 0,
            moveNumber = 0,
            boardSize = 19;
        boolean flag2 = false,
                inBrackets = false,
                displayComments = true;

        ///////////////////////////////////////////////////////////////////////
        // If there are not 1 or 2 arguments, end program and display usage. //
        ///////////////////////////////////////////////////////////////////////
        if(args.length < 1 || args.length > 2) {
            System.err.println("\nUsage: java sgfRead <readFile>[.sgf] (<writeFile>)");
	    System.exit(1);
	}


        ////////////////////////////////////////////////////////////////////////////////////////
        // Code to allow disabling comments.  Needs to be incorporated into interface design. //
        ////////////////////////////////////////////////////////////////////////////////////////
	/*        for(; c != 'y' && c != 'Y' && c != 'N' && c != 'n'; c = Keyboard.readLine().charAt(0))
	    {
		System.out.print("\nShall I display comments?(y/n)");
	    }
	*/
	//c='y';
        //if(c == 'y' || c == 'Y')
	//{
	 //  displayComments = true;//display comments
	//}

       

        /////////////////////////////////////////////////////////////
        // This TRY block should probably broken down into several //
        /////////////////////////////////////////////////////////////
        try {
	   // Open the designated file for reading.
	    filereader = new FileReader(args[0]); // + ".sgf");

           // If output is going to a file, open a file for writing.           
	    if(args.length == 2) {
	        filewriter = new FileWriter(args[1]);
	        System.out.println("\nWriting to " + args[1] + ":");
            }

	    int readByte; //The byte being read

            ////////////////////////////////////////////////////////////////
            // Read in bytes one at a time from the input file until EOF. //
            ////////////////////////////////////////////////////////////////
            while((readByte = filereader.read()) != -1) {
	        switch(readByte) {

	        // Left parenthesis: marks the start of a new game.
	        case 40: // '('
		    if(!inBrackets) {

                       //uncomment these lines to enable built-in pager:
		       //if(gameCount > 0) {
   		       //	   Keyboard.readLine(); 
		       //}
					
                        gameCount++;
		        i2 = 0;
		        moveNumber = 0;
		        flag2 = true;

                        // Write to a file
		        if(args.length == 2) {
		            filewriter.write("\nGame " + gameCount);
		            filewriter.write("\n=======");
		        } 

                        // Or to stdout
                        else {
                            TuiTeX.vspace(1);
                            TuiTeX.ul("Game " + gameCount);
		        }
		    // boolean flag6 = true;
		    }
		    break;

	        // Right parenthesis: marks the end of a game
	        case 41: // ')'
		    if(!inBrackets) {
		        if(flag2) flag2 = false;
		        
                        //Skip a line in the file (?)
 		        if(args.length == 2) {
		            System.out.println("Writing Game " + gameCount);
		            filewriter.write(10);
		        } 

                        //Skip a line of stdout
                        else System.out.println();
		    }
		    break;

	        // C: marks a comment
                case 67: // 'C'
		    if(prevByte != 80 && prevByte != 83 && !inBrackets) {
		        readByte = filereader.read();

		        if(displayComments) {
  		            //add some newlines to the file
		            if(args.length == 2) filewriter.write("\n\n");
		            
                            //or to stdout 
                            else System.out.print("\n\n");
		        }

                        // Read in the comment until you get to a Right bracket (']')
	                // and write to appropriate destination (file/stdout).                    
     		        while((readByte = filereader.read()) != 93) {
		            if(displayComments) {
			        if(args.length == 2) filewriter.write((char)readByte);
                                else System.out.print((char)readByte);			        
		            }
		        }

		        if(displayComments) {
		            if(args.length == 2) filewriter.write(10);
		            else   System.out.println();
		       	}
		    }
		    break;


                // In SGF format, information is stored like this: (;;B[pp];W[pd])
                // Data is inside of brackets, with labels in capital letters.
		case 91: // '['
		    inBrackets = true;
		    break;

		case 93: // ']'
		    inBrackets = false;
		    break;


	        // If prevByte is 'S', then this is the "SZ" tag -- board size
		case 90: // 'Z'
		    if(prevByte == 83) { //'S'
		        filereader.read();
                       
                        // Read in and set boardSize attribute
		        String s2;
		        for(s2 = ""; (readByte = filereader.read()) != 93; s2 = s2 + (char)readByte) { }
		        boardSize = Integer.parseInt(s2);

                        // Print the board size to the output
 		        if(args.length == 2) filewriter.write("        Size: " + boardSize + '\n');
		        else System.out.println("\n        Size: " + boardSize);
		    }
		    break;

		case 59: // ';'
		    if(i2 == 0) {
			if(args.length == 2) filewriter.write(10);
		        else System.out.println();
		    } 

	            /////////////////////////////////////////
                    // uncomment to restore built-in pager //
	            ///////////////////////////////////////// 

                    ////////////////////////////////////////////////////////////////////
                    //          
		    // else if(i2 == 1) {
		    //    Keyboard.readLine(); 
		    // }
                    // 
                    // else if(i2 % 25 == 0) {
		    //	  Keyboard.readLine();  //uncomment to restore built-in pager
		    // }
                    //
                    ////////////////////////////////////////////////////////////////////

	            i2++;
		    break;

		case 66: // 'B'
                    // PB[Name of Black Player]
		    if(i2 == 1 && prevByte == 80 && flag2) { //80=='P'
			readByte = filereader.read();

			if(args.length == 2) filewriter.write("Black Player: ");
			else System.out.print("Black Player: ");
			  
			while((readByte = filereader.read()) != 93) {
			    if(args.length == 2) filewriter.write((char)readByte);
			    else System.out.print((char)readByte);
			}

			if(args.length == 2) filewriter.write(10);
			else System.out.println();
		    } 

		    // B[black move]
                    else if(i2 > 1 && flag2 && !inBrackets) {
			int l2 = 0;
			readByte = filereader.read();
			if(readByte != 91) filereader.read(); // '['
			moveNumber++;
			while((readByte = filereader.read()) != 93) {
			    ai[l2] = readByte;
			    l2++;
			}
					   // int l = ai[0] - 97;
			int blackMove = ai[1] - 97;
			if(ai[0] >= 97 && ai[0] <= 104) ai[0] -= 32;
                        else if(ai[0] >= 105 && ai[0] <= 115) ai[0] -= 31;
			if(args.length == 2) filewriter.write("\n" + TuiTeX.rightAlign(moveNumber, 3) + ". " + "" + (char)ai[0] + (boardSize - blackMove));  
                        else System.out.print("\n" + TuiTeX.rightAlign(moveNumber, 3) + ". " + "" + (char)ai[0] + (boardSize - blackMove));
		    }
		    break;

		case 87: // 'W'
		   if(i2 == 1 && prevByte == 80 && flag2) {
		       readByte = filereader.read();

		       if(args.length == 2) filewriter.write("White Player: ");
		       else System.out.print("White Player: ");
					    
		       while((readByte = filereader.read()) != 93) {
			   if(args.length == 2) filewriter.write((char)readByte);
			   else System.out.print((char)readByte);
		       }

		       if(args.length == 2) filewriter.write(10);
                       else System.out.println();
                   } 
                   else if(flag2 && i2 > 1 && !inBrackets) {
		       int i3 = 0;
		       readByte = filereader.read();
		       if(readByte != 91) filereader.read();
		       moveNumber++;
		       while((readByte = filereader.read()) != 93) {
			   ai[i3] = readByte;
			   i3++;
		       }
					    //int i1 = ai[0] - 97;
		       int whiteMove = ai[1] - 97;
		       if(ai[0] >= 97 && ai[0] <= 104) ai[0] -= 32;
                       else if(ai[0] >= 105 && ai[0] <= 115) ai[0] -= 31;
	
		       if(args.length == 2) filewriter.write("\n" + TuiTeX.rightAlign(moveNumber, 3) + ". " + "" + (char)ai[0] + (boardSize - whiteMove));
                       else System.out.print("\n" + TuiTeX.rightAlign(moveNumber, 3) + ". " + "" + (char)ai[0] + (boardSize - whiteMove));
		   }
		   break;
		}
		if(readByte != 32 && readByte != 10) prevByte = readByte;
		       	//int k = prevByte;
	    }
	}

        catch(Exception exception) {
	    exception.printStackTrace();
	}

        finally {
	    if(args.length == 2) {
                try {
		    System.out.println(args[1] + " has been written.  Thanks.");
		    if(filereader != null) filereader.close();
		    //if(filewriter != null) filewriter.close();
		}
                catch(Exception exception2) {
		    exception2.printStackTrace();
		}
	    }
        }
    }
}
