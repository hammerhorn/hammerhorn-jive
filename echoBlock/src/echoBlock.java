import java.util.*;

public class echoBlock
{
    public static void main(String[] args){
	ArrayList<String> lines = new ArrayList<String>();
	Scanner in = new Scanner(System.in);

	while(in.hasNext()){
            String input = in.nextLine();
	    lines.add(input);
        }

	for(int count = 0; count < lines.size(); count++) System.out.println(lines.get(count));
    }
}
