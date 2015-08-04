public class ScaleTest{
   public static void main(String[] args){
      Scale s = new Scale();
      s.printList();
      TuiTeX.vspace(3);
      s = new Scale(11);
      s.printList();
   }
}
