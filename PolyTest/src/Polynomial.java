import java.util.*;

public class Polynomial extends Thing{
    static int count=0;
    ArrayList<Term> list;

    public Polynomial(){
        list = new ArrayList<Term>();
        count++;
        setLabel("Polynomial" + count);
    }


    public void addTerm(Term t){
        list.add(t);
    }

    public void print(){
	for(int i = 0; i < list.size(); i++){
            if(i != 0) System.out.print(" + ");
	    System.out.print(list.get(i).getString());
        }
    }


    public String getString(){
	String s = "f(x) = ";
	for(int i = 0; i < list.size(); i++){
            if(i != 0) s += (" + ");
	    s += list.get(i).getString();
        }
        return s;
    }

    public double eval(double d){
        double sum = 0.0;
	for(int i = 0; i < list.size(); i++){
	    sum += list.get(i).eval(d);
        }
        return sum;
    }

}
