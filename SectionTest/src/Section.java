import java.util.*;

public class Section extends Thing
{
    // ATTRIBUTES
    ////////////////
    //    protected Unit units;
    //protected double magnitude;

    static int count = 0;
    ArrayList<Paragraph> body;

    // CONSTRUCTORS
    //////////////////
    public Section(){
        body = new ArrayList<Paragraph>();	
	count++;
	setLabel(count + ".");
        System.out.println("=> " + this.str());
	//	print();
    }

    public Section(String title, ArrayList<Paragraph> pList){
        body = pList;	
	count++;
	setLabel(count + ". " + title);
        System.out.println("=> " + this.str());
	//	print();
    }

    public void printHeading(){TuiTeX.heading(label);}

    public String str(){return "[ Section " + count + " ]{" + label + "}";}

    public void print(){
        printHeading(); 
        for(int x = 0; x < body.size(); x++){
            body.get(x).setIndent(4);
            body.get(x).print();
            System.out.println();
        }
    }

    public void setHeading(String heading){
        label = heading;
    }

    public void addParagraph(Paragraph p){
        body.add(p);
    }
   
}
