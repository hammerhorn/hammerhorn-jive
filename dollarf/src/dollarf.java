public class dollarf{
    public static void main(String[] args){
        MyOpts Args = new MyOpts(args);
        boolean trailingNewline = true;
        if(Args.detectShortOption('n')) trailingNewline = false;
	Args = Args.stripFlags();
        System.out.print(TuiTeX.money(Args.getAsDouble(0)));
        if(trailingNewline) System.out.println();
        /*try{
		
	}

	catch(Exception exception){
	    exception.printStackTrace();
	}

	finally{

	}*/
    }
}
