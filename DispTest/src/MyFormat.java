//import java.io.*;
import java.text.DecimalFormat;

public class MyFormat
{
   static final int LeftOfCenter = 6;
	
   public MyFormat(){}

    /////////////////////////////////////////////
    // Print a double in a 6-space-wide column //
    /////////////////////////////////////////////
    public static String column(double d)
    {
       DecimalFormat decimalformat1 = new DecimalFormat("0.#E0");
       DecimalFormat decimalformat2 = new DecimalFormat("##0.###");
       Double double1 = new Double(d);
       DecimalFormat decimalformat;

       if(("" + (int)double1.doubleValue()).length() <= 5 && double1.doubleValue() >= 0.10000000000000001D || double1.doubleValue() <= 0.0D)
       {
          decimalformat = decimalformat2;
       } 
 
       else decimalformat = decimalformat1;
       return String.format("%1$" + 6 + "s",decimalformat.format(d));    
    }


    public static String column(double d, int i)
    {
       DecimalFormat decimalformat1 = new DecimalFormat("0.#E0");
       DecimalFormat decimalformat2 = new DecimalFormat("##0.###");
       Double double1 = new Double(d);
       DecimalFormat decimalformat;

       if(("" + (int)double1.doubleValue()).length() <= 5 && double1.doubleValue() >= 0.10000000000000001D || double1.doubleValue() <= 0.0D)
       {
          decimalformat = decimalformat2;
       } 
 
       else decimalformat = decimalformat1;
       return String.format("%1$" + i + "s",decimalformat.format(d));    
    }

 
    //////////////////////////////////////////////////////////////////////////
    // Format a double into either scientific notation or a 3-place decimal //
    //////////////////////////////////////////////////////////////////////////
    public static String format(double d)
    {
       DecimalFormat decimalformat1 = new DecimalFormat("0.###E0");
       DecimalFormat decimalformat2 = new DecimalFormat("##0.###");
       Double double1 = new Double(d);
       DecimalFormat decimalformat;

       if(("" + (int)double1.doubleValue()).length() <= 5 && double1.doubleValue() >= 0.10000000000000001D || double1.doubleValue() <= 0.0D)
       {
	  decimalformat = decimalformat2;
       } 

       else decimalformat = decimalformat1;
       return decimalformat.format(d);
    }




    //////////////////////////////////////////////////////////////////////////
    // Format a double into either scientific notation or a 3-place decimal //
    //////////////////////////////////////////////////////////////////////////
    public static String money(double d)
    {
       DecimalFormat decimalformat = new DecimalFormat("##0.00");
       return "$" + decimalformat.format(d);
    }


    ///////////////////////////////////////////////////////////
    // Format an int, using scientific notation if necessary //
    ///////////////////////////////////////////////////////////
    public static String format(int i)
    {
       DecimalFormat decimalformat = new DecimalFormat("#####0");
       return decimalformat.format(i);
    }


    public static String format(long i)
    {
       DecimalFormat decimalformat = new DecimalFormat("#####0");
       return decimalformat.format(i);
    }


    //////////////////
    // Skip 3 lines //
    //////////////////
    public static void whitespace()
    {
       System.out.println("\n\n");
    }

 
    ////////////////////////////////////
    // Skip a certain number of lines //
    ////////////////////////////////////
    public static void whitespace(int i)
    {
      for(int j = 0; j < i; j++)
      {
	System.out.println();
      }
    }
    

    //////////////////////////////////////////////////
    // Make a horizontal line by made of 80 hyphens //
    //////////////////////////////////////////////////
    public static void hr()
    {
	for(int count=0;count<80;count++)
        {
	    System.out.print('-');
        }
        System.out.println();
    }

    
    ////////////////////////////////////////////////////////////
    // Print a one-line string centered, with a border of *'s //
    ////////////////////////////////////////////////////////////
    public static String banner(String s)
    {
	int bannerWidth = s.length() + 4, 
            columnTotal = 80,
            i;

        double emptyColumns = columnTotal - bannerWidth,
               emptyColumnsOver2 = emptyColumns / 2D;

        String content="\n";

        i = (int)emptyColumnsOver2 - 6;

        for(int j = 0; j < i; j++)
        {
           content += ' ';
        }

        for(int k = 0; k < bannerWidth; k++)
        {
           content+='*';
        }

        content+='\n';

        for(int l = 0; l < i; l++)
        {
           content+=' ';
        }

        content+="* " + s + " *\n";

        for(int i1 = 0; i1 < i; i1++)
        {
	     content += ' ';
        }

        for(int j1 = 0; j1 < bannerWidth; j1++)
        {
	    content+='*';
        }

	content+="\n";

	return content;
    }

    
    ///////////////////////////////////////////////////////////////
    // Print a one-line string a specified number of spaces from //
    // the left edge, with a border of *'s                       //
    ///////////////////////////////////////////////////////////////
    public static String banner(String s, int fromLeft)
    {	int bannerWidth = s.length() + 4;
	//            columnTotal = 80;
	String content="\n";

        int j = fromLeft;

        bannerWidth = s.length() + 4;

        for(int k = 0; k < j; k++)
	{
	   content+=' ';
	}

        for(int l = 0; l < bannerWidth; l++)
	{
	   content+='*';
	}

	content+='\n';

        for(int i1 = 0; i1 < j; i1++)
	{
	   content+=' ';
	}

        content+="* " + s + " *\n";

        for(int j1 = 0; j1 < j; j1++)
	{
	   content+=' ';
	}

        for(int k1 = 0; k1 < bannerWidth; k1++)
	{
	   content+='*';
	}

	return content + '\n';
    }


    ////////////////////////////////////////////////////////////////////////
    // Print a one-line string indented a specified number of spaces from //
    // the center point edge, with a border of *'s                        //
    ////////////////////////////////////////////////////////////////////////
    public static String banner(int i, String s)
    {
        int columnTotal = 80,
        bannerWidth = s.length() + 4;
        double d = columnTotal - bannerWidth;
        double d1 = d / 2D;
        int j;
	String content="\n";

        if(d / 2D != 0.0D)
        {
           j = (int)d1 - (i * -1 + 1);
        }
        j = (int)d1 - i * -1;

        for(int k = 0; k < j; k++)
        {
           content+=' ';
        }

        for(int l = 0; l < bannerWidth; l++)
        {
           content+='*';
        }

        content+='\n';

        for(int i1 = 0; i1 < j; i1++)
        {
           content+=' ';
        }

        content+="* " + s + " *\n";

        for(int j1 = 0; j1 < j; j1++)
        {
           content+=' ';
        }

        for(int k1 = 0; k1 < bannerWidth; k1++)
        {
           content+='*';
        }

	content+="\n";
	return content;
    }


    ////////////////////////////////////////////////////////////
    // Print a one-line string centered, with a custom symbol //
    ////////////////////////////////////////////////////////////
    public static String banner(char c, String s)
    {
        int columnTotal = 80;
        int bannerWidth = s.length() + 4;
        double d = columnTotal - bannerWidth;
        double d1 = d / 2D;
        int i;
	String content="\n";
        if(d / 2D != 0.0D)
            {
                i = (int)d1 - 7;
            }
        i = (int)d1 - 6;

        for(int j = 0; j < i; j++)
            {
		content+=' ';
            }

        for(int k = 0; k < bannerWidth; k++)
            {
                content+=c;
            }

	content+='\n';
        for(int l = 0; l < i; l++)
            {
                content+=' ';
            }

        content+=c + " " + s + " " + c + "\n";
        for(int i1 = 0; i1 < i; i1++)
            {
                content+=' ';
            }

        for(int j1 = 0; j1 < bannerWidth; j1++)
            {
                content+=c;
            }

	content+="\n";
	return content;
    }


    //////////////////////////////////////////////////////////////////////////////////
    // Print a one-line string indented from the center point, with a custom symbol //
    //////////////////////////////////////////////////////////////////////////////////
    public static String banner(char c, int i, String s)
    {
        int columnTotal = 80;
        int bannerWidth = s.length() + 4;
        double d = columnTotal - bannerWidth;
        double d1 = d / 2D;
        int j;
	String content="\n";

        if(d / 2D != 0.0D)
            {
                j = (int)d1 - (i * -1 + 1);
            }

        j = (int)d1 - i * -1;
	//content+="\n";

        for(int k = 0; k < j; k++)
            {
                content+=' ';
            }

        for(int l = 0; l < bannerWidth; l++)
            {
                content+=c;
            }

	content+='\n';

        for(int i1 = 0; i1 < j; i1++)
            {
                content+=' ';
            }

        content+=c + " " + s + " " + c + "\n";

        for(int j1 = 0; j1 < j; j1++)
            {
                content+=' ';
            }

        for(int k1 = 0; k1 < bannerWidth; k1++)
            {
                content+=c;
            }

	content+="\n";
	return content;
    }



    ///////////////////////////////////////////////////////////////////////////////
    // Print a one-line string indented from the left edge, with a custom symbol //
    ///////////////////////////////////////////////////////////////////////////////
    public static String banner(char c, String s, int i)
    {
	String str="\n";
        //int columnTotal = 80;
        int j = i;
	//        str+="\n\n\n";
        int bannerWidth = s.length() + 4;
        for(int k = 0; k < j; k++)
            {
                str+=' ';
            }

        for(int l = 0; l < bannerWidth; l++)
            {
                str+=c;
            }

	str+='\n';
	for(int i1 = 0; i1 < j; i1++)
            {
                str+=' ';
            }

        str+=c + " " + s + " " + c + "\n";
        for(int j1 = 0; j1 < j; j1++)
            {
                str+=' ';
            }
	for(int k1 = 0; k1 < bannerWidth; k1++)
            {
                str+=c;
            }

        str+="\n";
	return str;
    }



    public static void ul(String s)
    {
	System.out.println(' ' + s);
	for(int x = -2; x < s.length(); x++) System.out.print('=');
	//        System.out.println();

    }


    /////////////////////////////
    // cast a double as an int //
    /////////////////////////////
   public static int truncate(double d)
   {
      return (int)d;
   }
}
