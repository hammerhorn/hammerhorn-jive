public class goBoard extends Thing{
    char board[][] = new char[19][19];
 
    static int count = 0;


    public goBoard(){
	count++;
        setLabel("GOBAN #" + count);
	for(int rank = 0; rank < 19; rank++){
	    for(int col = 0; col < 19  ; col++){
		board[col][rank] = ' ';
            }
	}
	//	Point.setCounter(0);
    }

    public void ListPoints()
    {
	for(int rank = 0; rank < 19; rank++)
        {
	    for(int col = 0; col < 19; col++)
	    {
		//		board[col][rank].display();
		System.out.print(board[col][rank]);
            }
            System.out.println();
	}       
    }




    public void gobanPrint()
    {
	PrintLabel();
		System.out.println();

	System.out.println("    A B C D E F G H J K L M N O P Q R S T");       
	for(int rank = 18; rank >= 0;rank--)
        {
	    System.out.print(TuiTeX.rightAlign(rank+1, 3)+' ');
	    for(int col=0; col < 19; col++)
	    {
		if(board[col][rank]=='b')System.out.print("X ");
                else if(board[col][rank]=='w')System.out.print("O ");

		else if(board[col][rank]=='*')System.out.print("* ");
		//                System.out.print('-');
                //else if(board[col][rank].x_magnitude==0||board[col][rank].y_magnitude==0)System.out.print(", ");
                else if ( col ==  6 && (rank == 6 || rank == -6 || rank == 0) ||
                          col ==  0 && (rank == 6 || rank == -6 || rank == 0) ||
			  col == -6 && (rank == 6 ||  col == -6 || rank == 0)) System.out.print("+ ");
		else System.out.print(". ");
		//                System.out.print('-');
            }
	    //            System.out.println();
	    System.out.println(TuiTeX.rightAlign(rank+1, 2));
	}
	System.out.println("    A B C D E F G H J K L M N O P Q R S T");       
	System.out.println();
    }



    public void artPrint()
    {
	PrintLabel();
		System.out.println();

		//	System.out.println("    A B C D E F G H J K L M N O P Q R S T");       
	for(int rank=18; rank>= 0;rank--)
        {
	    // System.out.print(MyFormat.column(rank+1, 3)+' ');
	    for(int col=0; col < 19; col++)
	    {
		if     (board[col][rank] == 'b') System.out.print("X ");
                else if(board[col][rank] == 'w') System.out.print("O ");
		else if(board[col][rank] == '*') System.out.print("* ");
		//                System.out.print('-');
                //else if(board[col][rank].x_magnitude==0||board[col][rank].y_magnitude==0)System.out.print(", ");
                else if ( col ==  6  && (rank == 6 || rank == -6 || rank == 0) ||
                          col ==  0  && (rank == 6 || rank == -6 || rank == 0) ||
			  col == -6  && (rank == 6 || rank == -6 || rank == 0)) System.out.print(". ");
		else System.out.print("  ");
		//                System.out.print('-');
            }
	    //            System.out.println();
	    //  System.out.println(MyFormat.column(rank+1, 2));
	    System.out.println();
	}
	//	System.out.println("    A B C D E F G H J K L M N O P Q R S T");       
	System.out.println();
    }




    public void numericPrint(){
      	for(int rank = 18; rank >= 0;rank--){
	    for(int col = 0; col < 19; col++){
		//board[col][rank].numericPrint();
                System.out.print("(" + (col - 9) + ", " + (rank + 9) + ") ");
            }
            System.out.println();
	}       
    }

    public void markPointBlack(int x, int y){
        board[x + 9][y + 9] = 'b';    
    }

    public void markPointWhite(int x, int y){
        board[x + 9][y + 9] = 'w';    
    }

    public void markPointStar(int x, int y){
        board[x + 9][y + 9] = '*';    
    }

    public void erasePoint(int x, int y){
        board[x + 9][y + 9] = ' ';    
    }

}
