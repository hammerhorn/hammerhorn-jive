public class Parabola extends Thing
{
  double vertex_x, 
         vertex_y, 
      x_intercept;

  public Parabola(double vx, double vy, double xi ){
     vertex_x = vx;
     vertex_y = vy;
     x_intercept = xi;
  }

  public double f_of_x1(double x){
     return vertex_y * (1 + Math.pow(((x - vertex_x)/(x_intercept - vertex_x)),2));
  }

  public double f_of_x2(double x){
     return vertex_y * (1 - Math.pow(((x - vertex_x)/(x_intercept - vertex_x)),2));
  }
}
