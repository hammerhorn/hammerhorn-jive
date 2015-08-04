
public class mybanner{
  public static void main(String[] args){
     String s = "";
     if(args.length > 0){
        s = "";
        for (String t: args){
           s += t;
           s += ' ';
        }
        s = s.substring(0, s.length() - 1);
     }

     else{
        System.out.print(">");
        s = Keyboard.readLine();
     }

     System.out.println("\n" + TuiTeX.box('#',s));
  }
}
