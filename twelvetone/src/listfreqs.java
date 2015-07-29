//import java.io.*;

public class listfreqs
{
    public static void main(String[] args)
    {
        // MyOpts Args = new MyOpts(args);
        // Note [] n = new Note[Args.length()];
        // Note [] n = new Note[args.length];

        String buffer = Keyboard.readLine();

        // //wtf...is it stdout or stderr?  why is it acting as both?
        System.err.println(buffer);

        String [] words = buffer.split(" ");

        Note [] n = new Note[words.length];

        for(int count = 0; count < words.length; count++){
	  //	    double num = Args.getAsDouble(count);
   	    double num = Double.parseDouble(words[count]);
            num--;
            int oct = 4;
            if(num >= 12)
                num = num - 12; oct++;
            if(num < 0)
                num += 12; oct--;
            if(num < 3)
                oct--;
				   
            n[count] = new Note(num, oct);
            n[count].niceprint();
            n[count].printfreq();
        }
        System.err.println("\n");

        /*System.out.print("note number");
        double d = Keyboard.readDouble();
        System.out.print("octave number");
        int i = Keyboard.readInt();
        System.out.println("Preparing to create note "+d+", octave "+i);
        n[0] = new Note(d, i);
        n[0].niceprint();*/
    }
}
