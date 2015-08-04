import java.io.*;

public class myCat
{
    public static void main(String[] args){
	FileInputStream fin;

	if(args.length== 0){  
	    String s = "";
            while(s != null){
                s = null;
                s = Keyboard.readLine();
		if(s != null) System.out.println(s);
	    }
        }

	else {
            for(int count=0; count < args.length; count++) {
	        try {
		    fin = new FileInputStream(args[count]); 
                }

 	        catch(FileNotFoundException exc) {
		    StackTraceElement[] stack = Thread.currentThread ().getStackTrace ();
		    StackTraceElement main = stack[stack.length - 1];
		    String mainClass = main.getClassName ();
		    System.err.println(mainClass + ": " + args[count] + ": No such file or directory");
		    continue; 
                }

	        try {
                    int i;
                    do {
                        i = fin.read();
                        if(i != -1) System.out.print((char)i);
                    } while(i != -1);
	        }catch(IOException exc){}

                try {
                    fin.close();
	        }catch(IOException exc){}
	    }
        }
    }
}
