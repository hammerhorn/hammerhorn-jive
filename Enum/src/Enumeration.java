import java.util.*;

public class Enumeration extends Thing{
    static int count=0;
    ArrayList<String> list;

    public Enumeration(String[] data){
        count++;
        setLabel("Ordered List " + count);
	//#	list = data;
        list = new ArrayList<String>();
        int x = 0;
        while(x < data.length){
	    list.add(data[x]);
            x++;
        }
    }

    public Enumeration(ArrayList<String> data){
        count++;
        setLabel("Ordered List " + count);
		list = data;
	//        list = new ArrayList<String>();
		// int x = 0;
		// while(x < data.size()){
		//list.add(data.get([x]);
		//x++;
		//}
    }


    public void print(){TuiTeX.enumerate(str(), list);}

}
