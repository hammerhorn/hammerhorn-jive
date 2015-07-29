public class sum{
   public static void main(String[] args){
       double sum = 0.0D;
       for(int x = 0; x < args.length; x++){
           sum += Double.parseDouble(args[x]);
       }
       System.out.println(sum);
   }
}
