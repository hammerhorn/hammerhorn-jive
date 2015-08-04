//import java.text.DecimalFormat;


public class Paragraph extends Thing
{
    String[] lines;
    String buffer;
    static int count = 0,
              indent = 0;
	
    // 
    // CONSTRUCTORS
    //////////////////
    public Paragraph(String s, int width){
	count++;
	setLabel("Paragraph #" + count);
	buffer = "     " + s;
	fold(width);
        System.out.println("=> " + this.str());
    }


    public void setIndent(int fill){
        indent = fill;
    }

    public void fold(int width){	    
	lines = new String[(buffer.length() / width) + 1];
	  
        for(int lineNum = 0; lineNum < lines.length; lineNum++){
            if(buffer.length() >= width) {
		lines[lineNum] = buffer.substring(0, width);
	        buffer = buffer.substring(width);
	    }
	    else lines[lineNum] = buffer;
        }
    }
    

    public void print(){
	//	PrintLabel();
	TuiTeX.vspace(1);
	for(int x = 0; x < lines.length; x++){
	   TuiTeX.hfill(indent);

	   System.out.println(lines[x]);
	}
	TuiTeX.vspace(1);
    }
    public String str(){
	return "[ Paragraph " + count + " ]";
    }

}


