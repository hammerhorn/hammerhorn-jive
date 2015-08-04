import java.util.*;

public class ParagraphTest
{
   public static void main(String[] args){
      final int width = 70;
      String lineBuf = "", paraBuf = "";
      Paragraph currentPara;
      ArrayList<String> lines = new ArrayList<String>();
      ArrayList<Paragraph> pList = new ArrayList<Paragraph>();
      //      System.out.print(">");
      while(lineBuf != null){
          lineBuf = null;
          lineBuf = Keyboard.readLine();
          if(lineBuf != null){ lines.add(lineBuf); }
      }

      for(int x = 0; x < lines.size(); x++){
          if (lines.get(x) != ""){
	      paraBuf += lines.get(x);
          }
          else{
              currentPara = new Paragraph(paraBuf, width);
              currentPara.setIndent(4);
              currentPara.print();
          }
      }

      //      if(args.length >= 1) width = Integer.parseInt(args[0]);
      //Paragraph p = new Paragraph(buffer, width);

   }
}
