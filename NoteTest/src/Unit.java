public class Unit extends Thing{
    //
    // DATA
    //////////

    String abbrev="";
    
    //
    // CONSTRUCTORS
    //////////////////

    public Unit(){
	//	System.out.println("Unit()");
	//        setLabel("<unknown unit>");
	set();
    }

    public Unit(String s){
        set(s, s);
    }
    
    public Unit(String s, String a){
        set(s,a);
    }

    //
    // I/O
    /////////

    public void set(){
	//	setLabel("<unknown units>");
	label = "unit(s)";
        abbrev = "unit(s)";
    }


    public void set(String s, String a){
	label = s;
       abbrev = a;
    }
    
    public void set(String s){
	label = s;
       abbrev = s;
    }
    
    public void print(){
        System.out.print(label + " (" + abbrev + ")");
    }
    
    public String str(){
	if(abbrev.length() == 0 || label.equals(abbrev)) return label;
	else return (label + " (" + abbrev + ")");
    }
}
