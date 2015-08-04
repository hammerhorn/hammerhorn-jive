public class Photon extends Wave
{
  public Photon( double kelvins)
  {
           speed = new Velocity( 3e8, new Angle() );
      wavelength = new displacement( 2.8977721E-3 / kelvins );       
      freq = new Scalar(speed.MperS() / wavelength.Meters(), new Unit("Hertz", "Hz"));
  }

  public String EMtype(){
          if(wavelength.Meters()<3E-7) return "x-rays or gamma rays";
     else if(wavelength.Meters()>=3E-7 && wavelength.Meters() < 4E-7) return "ultraviolet";
     else if(wavelength.Meters()>=4E-7 && wavelength.Meters() < 4.2E-7) return "violet light";
     else if(wavelength.Meters()>=4.2E-7  && wavelength.Meters() < 4.4E-7 ) return "indigo light";
     else if(wavelength.Meters()>=4.4E-7  && wavelength.Meters() < 5E-7 ) return "blue light"; 
     else if(wavelength.Meters()>=5E-7  && wavelength.Meters() < 5.2E-7 ) return "cyan light"; 
     else if(wavelength.Meters()>= 5.2E-7 && wavelength.Meters() < 5.65E-7 ) return "green light"; 
     else if(wavelength.Meters()>=5.65E-7  && wavelength.Meters() < 5.9E-7 ) return "yellow light"; 
     else if(wavelength.Meters()>=5.9E-7  && wavelength.Meters() <6.25E-7  ) return "orange light"; 
     else if(wavelength.Meters()>=6.25E-7  && wavelength.Meters() < 7E-7 ) return "red light"; 
     else if(wavelength.Meters()>=7E-7  && wavelength.Meters() < 1.4E-6 ) return "near-infrared"; 
     else return "radio waves or microwaves";
  }
}
