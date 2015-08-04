public class goban extends Thing
{
    int BoardSize = 19;
    Point board[][] = new Point[BoardSize][BoardSize];
 
    static int count = 0;

    public goban()
    {
	count++;
        setLabel("GOBAN #" + count);
	for(int rank = 0; rank < BoardSize; rank++){
	    for(int col = 0; col < BoardSize; col++)
		board[col][rank] = new Point(col - 9, rank - 9);
	}
    }

    public void ListPoints()
    {
    	for(int rank = 0; rank < BoardSize;rank++){
	    for(int col = 0; col < BoardSize; col++)
		//		board[col][rank].display();
		board[col][rank].println();
	}       
    }

    public void gobanPrint()
    {
	PrintLabel();

	System.out.println("\n    A B C D E F G H J K L M N O P Q R S T");       
	for(int rank = (BoardSize - 1); rank >= 0; rank--){
	    System.out.print(TuiTeX.rightAlign(rank + 1, 3) + " ");
	    for(int col = 0; col < BoardSize; col++){
		if(board[col][rank].marker.equals("black"))
                    System.out.print("X ");
                else if(board[col][rank].marker.equals("white"))
                    System.out.print("O ");
		else if(board[col][rank].marker.equals("star"))
                    System.out.print("* ");
                else if(board[col][rank].x_magnitude == 6  && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0) ||
                    board[col][rank].x_magnitude == 0  && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0) ||
		    board[col][rank].x_magnitude == -6 && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0)) System.out.print("+ ");
		else
                    System.out.print(". ");
            }
	    System.out.println(TuiTeX.rightAlign(rank + 1, 2));
	}
	System.out.println("    A B C D E F G H J K L M N O P Q R S T");       
	System.out.println();
    }

    public void artPrint()
    {
	PrintLabel();
	System.out.println();

	for(int rank = (BoardSize - 1); rank >= 0; rank--){
	    for(int col = 0; col < 19; col++){
		if(board[col][rank].marker.equals("black"))
                    System.out.print("X ");
                else if(board[col][rank].marker.equals("white"))
                    System.out.print("O ");
		else if(board[col][rank].marker.equals("star"))
                    System.out.print("* ");
                else if(board[col][rank].x_magnitude == 6  && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0) ||
                    board[col][rank].x_magnitude == 0  && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0) ||
          	    board[col][rank].x_magnitude == -6 && (board[col][rank].y_magnitude == 6  || 
                    board[col][rank].y_magnitude == -6 ||  board[col][rank].y_magnitude == 0)) 
                    System.out.print(". ");
		else
                    System.out.print("  ");
            }
	    System.out.println();
	}
	System.out.println();
    }

    public void numericPrint()
    {
      	for(int rank = 18; rank>= 0;rank--){
	    for(int col = 0; col < BoardSize; col++)
		board[col][rank].numericPrint();
            System.out.println();
	}       
    }

    public void markPointBlack(int x, int y)
    {
        board[x+9][y+9].marker = "black";    
    }


    public void markPointBlack(Point p)
    {
        board[(int)p.x_magnitude + 9][(int)p.y_magnitude + 9].marker = "black";    
    }


    public void markPointWhite(int x, int y)
    {
        board[x + 9][y + 9].marker = "white";    
    }



    public void markPointWhite(Point p)
    {
        board[(int)p.x_magnitude + 9][(int)p.y_magnitude + 9].marker = "white";    
    }


    /*    public void markUnmarkWhite(Point p)
    {
        if(board[(int)p.x_magnitude + 9][(int)p.y_magnitude + 9].marker=="white"){
	    erasePoint(p);}
	    else markPointWhite(p);
        
	    }*/


    public void markPointStar(int x, int y)
    {
        if(x <= 9 && x >= -9 && y <= 9 && y >= -9)
            board[x + 9][y + 9].marker = "star";    
    }



    public void markPointStar(Point p)
    {
        board[(int)p.x_magnitude + 9][(int)p.y_magnitude + 9].marker = "star";    
    }



    public void erasePoint(int x, int y)
    {
        board[x + 9][y + 9].marker = "none";    
    }


    public void erasePoint(Point p)
    {
        board[(int)p.x_magnitude + 9][(int)p.y_magnitude + 9].marker = "none";    
    }

    public void plotLine(Point p, Angle slope)
    {
        for(double domain = -9.0; domain <= 9.0; domain++) 
            //f(x) = m(x-x1) + y1
            markPointStar((int)domain, (int)(slope.slope() * (domain - p.x_magnitude) + p.y_magnitude));
    }
}
