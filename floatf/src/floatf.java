public class floatf
{
  public static void main(String[] args)
  {
      //      String [] prompts = {"Please type a number"};
      //String [] prompts = {""};
      //      MyOpts argz = new MyOpts(1,args,prompts,"Usage: java FormatFloat <float>");
      //      MyOpts argz = new MyOpts(1,args,prompts,"");
      MyOpts argz = new MyOpts(1,args);
      //      if(args.length!=1){System.err.println("\n\tUsage: java FormatFloat <float>\n");}
      //      else{      
      double d = Double.parseDouble(argz.getElement(0));
      System.out.println(TuiTeX.format(d));
      // }
  }
}
