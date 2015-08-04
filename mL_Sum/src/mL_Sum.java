public class mL_Sum{
    public static void main(String[] args){
        Volume v1 = new Volume(Double.parseDouble(args[0])),
  	       v2 = new Volume(Double.parseDouble(args[1]));
        v1.plus(v2).printout();
    }
}
