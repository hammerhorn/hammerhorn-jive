public class FormatTest
{
  public static void main(String[] args)
  {
      double d[] = {0,0,0};
      int x, i;
      String s;
      //      System.out.println(args[0]);

      for (x = 0; x < 3; x++){
         System.out.print("double: ");
         d[x] = Keyboard.readDouble();
      }
      System.out.println();

      for (x=0; x<3; x++) System.out.println(TuiTeX.format(d[x]));
      System.out.println();
      for (x=0; x<3; x++) System.out.println(TuiTeX.rightAlign(d[x]));
      System.out.println();
      for (x=0; x<3; x++) System.out.println(TuiTeX.money(d[x]));
      System.out.println();
      System.out.print("# of spaces to skip: ");
      i = Keyboard.readInt();
      TuiTeX.vspace(i);

      TuiTeX.hrule();

      System.out.print("String: ");
      s = Keyboard.readLine();
      System.out.print(TuiTeX.box(s));

      System.out.print("Spaces from the left: ");
      i = Keyboard.readInt();
      System.out.print(TuiTeX.box(s, i));

      System.out.print("Spaces from the center: ");
      i = Keyboard.readInt();
      System.out.print(TuiTeX.box(i, s));

      TuiTeX.hrule();
      System.out.print("Custom symbol: ");
      char c = Keyboard.readLine().charAt(0);
      System.out.print(TuiTeX.box(c,s));
      
      System.out.print("Spaces from the left: ");
      i = Keyboard.readInt();
      System.out.print(TuiTeX.box(c,s,i));

      System.out.print("Spaces from the center: ");
      i = Keyboard.readInt();
      System.out.print(TuiTeX.box(c,i,s));

      
  }
}
