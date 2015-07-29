//Usage: java die (max)
//Generates a random number 1>= x <= max; or 1>=x<=6

public class dice {
    public static void main(String[] args) {
        MyOpts Args = new MyOpts(args);
        Die d1; 
	boolean ascii = false, verbose = false;

        if(Args.lengthMinusFlags() == 0) d1 = new Die();
        else d1 = new Die(Args.stripFlags().getAsInt(0));

        if(Args.detectShortOption('a')) ascii = true;
        if(Args.detectShortOption('v')) verbose = true;
        if(Args.detectShortOption('h')){
            //Change this so it reads the classname dynamically
            System.out.println("\nuse: ./dice.jar [-a] [-v]\n");
            System.exit(0);
        }

        if(verbose) d1.display();
        else        d1.printValue();
        if(ascii)   d1.drawFace();

        if(ascii && verbose) System.out.println();
        System.out.println();
    }
}
