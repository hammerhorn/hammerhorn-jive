import java.util.*;

public class ItemList extends Thing
{
    //
    // DATA
    //////////

    //String[] list;
    
    //
    // CONSTRUCTORS
    //////////////////
    //ItemList(String[] items){
    //    list = items;
    // }
	

    //
    // I/O
    /////////
    //public void print(){
    //	TuiTeX.itemize(list);
    //}

    static int count = 0;
    ArrayList<String> list;

    public ItemList(String[] data)
    {
        count++;
        setLabel("Ordered List " + count);
        //#     list = data;                                                                                                              
        list = new ArrayList<String>();
        int x = 0;
        while(x < data.length){
            list.add(data[x]);
            x++;
        }
    }

    public ItemList(ArrayList<String> data)
    {
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


    public void print()
    {
        TuiTeX.itemize(str(), list);
    }




}
