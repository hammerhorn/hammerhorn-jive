import java.util.*;

public class NumMenTest{
    public static void main(String[] args){
        ArrayList<String> list = new ArrayList<String>();
	if(args.length == 0){
            String s = "";
            while(s != null){
                s = null;
                s = Keyboard.readLine();
		if(s != null) list.add(s);
            }
        }
	else{
            for( int i = 0; i < args.length; i ++ ){
 	        list.add(args[i]);
            }
	}

	NumMenu menu = new NumMenu(list);

        int number = 1;

        while(number >= 1 && number <= list.size()){
            number = menu.getSelection(true);
	    System.out.println("You chose selection #" + number + " -- " 
                              + TuiTeX.emph(menu.options.get(number - 1)));
        }
    }
}
