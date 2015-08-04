import java.util.*;

public class SectionTest{
    public static void main(String[] args){
        ArrayList<Section> sections = new ArrayList<Section>();
	//	ArrayList<Paragraph> pList = new ArrayList<Paragraph>();
	ArrayList<String> lines = new ArrayList<String>();

        Paragraph p;
	final int WIDTH = 70;
	String lineBuf = "", paraBuf = "", heading = "";

	//	if(args.length == 0){
        

        // Get lines and store in ArrayList object
        while(lineBuf != null){
            lineBuf = null;
            lineBuf = Keyboard.readLine();
	    //            System.out.println();
            if(lineBuf != null){lines.add((lineBuf));}
        }

        

        for(int y = 0; y < lines.size(); y++){
            System.out.printf("%2d %s\n", y, lines.get(y));
	}

	for(int x = 0; x < lines.size(); x++){
	    lineBuf = lines.get(x);    
	    if(lineBuf.length() > 0){
	       if(lineBuf.charAt(0) == '*'){ 
	           heading = lineBuf.substring(1, lineBuf.length());
	            sections.add(new Section());
	            sections.get(sections.size() - 1).setHeading(heading); //.printHeading();
	       }
	       else paraBuf += lineBuf;
            }              
	    else{/*empty line encountered*/
                 
 		 //buffer = "";
		 //                System.err.println("newline detected");

	   	 p = new Paragraph(paraBuf, WIDTH);
                 p.setIndent(4);
                 paraBuf = "";

	    //            sections.get(section.size() - 1).add(.pList.add(p);)
            //sections.add(new Section());
                //p.print();
		// tgfgr}
	   }

	    for(x = 0; x < sections.size(); x++){
                sections.get(x).print();
                System.out.println();
            }


	/*

	String buffer =  Keyboard.readLine();
	if(args.length >= 1) width = Integer.parseInt(args[0]);
	Paragraph p = new Paragraph(buffer, width);



	p.setIndent(4);
	p.print();
	*/





	/*        TuiTeX.vspace(1);

        section1 = new Section("Firearms in the Middle East");
        section1.printHeading();
	TuiTeX.vspace();

        section2 = new Section("Cow and Horse");
        section2.printHeading();
        TuiTeX.vspace();

        section3 = new Section("Boots of the World");
        section3.printHeading();
        TuiTeX.vspace();

        System.out.println("The label is " + section3.str() + ".\n");*/
	}    }}

