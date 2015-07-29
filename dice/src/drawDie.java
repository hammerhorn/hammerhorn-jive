public class drawDie{
    public static void main(String[] args){
        Die cube = new Die();

        // reads from stdin if no args present
        MyOpts Args = new MyOpts(1, args);

        cube.setFace(Args.getAsInt(0));
        cube.drawFace();
    }
}
