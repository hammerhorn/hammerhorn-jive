import java.text.*;
//import java.io.*;

public class Note extends Wave{
    // 
    // DATA
    //////////
     String notename;

    double halfsteps,    //semitones compared to 440Hz. 
     local_semitones, //semitones compared to nearest A (-5.9 - 5.9) 
               cents, 
          note_float; //0.0 - 11.9

     int note_number,
              octave;

    static int count = 0;

                    // Make basefreq adjustable, eg, for Europe
                    // Let user optionally use german note names
    //
    // CONSTRUCTORS
    //////////////////
    public Note(double f){
	count++;
	setLabel("NOTE #" + count);

            freq = new Scalar(f,new Unit("Hertz", "Hz"));
           speed = new Velocity(340.29, new Angle());
      wavelength = new displacement(speed.MperS() / freq.magnitude());
      
       halfsteps = 12.0 * Math.log(freq.magnitude() / 440.0) / Math.log(2.0);
       local_semitones = halfsteps % 12; //HSs + or - A in this octave
       local_semitones = (double)Math.round(local_semitones * 100) / 100;

            // halfsteps = note_float + (octave - 4) * 12;
            /*       if(local_semitones<0) local_semitones-=.0000001;
		 else local_semitones+=.0000001;*/

       if(local_semitones < -6.0) local_semitones += 12.0;
       else if (local_semitones >= 6.0)
	   { local_semitones = -1 * (12.0 - local_semitones);}
       cents = 100 * (local_semitones - (int)local_semitones);
       note_float = local_semitones;
       while (note_float < 0) note_float += 12.0; 
       note_number = (int)note_float;

       setNotename();
       setOct();
             //octave = 1 + (int)(Math.log(freq / (440 * Math.pow(2, -3.75))) / Math.log(2));
    }

    public Note(String s, int oct, double c){       
	count++;
	setLabel("NOTE #" + count);

           freq = new Scalar(0, new Unit("Hertz", "Hz"));
           speed = new Velocity(340.29, new Angle());
      wavelength = new displacement();
	    
        cents = c;        
     if (s.equals("A#") || s.equals("a#") || s.equals("Bb") || s.equals("bb"))      {   note_float = 1; 
            notename = "A♯/B♭"; }

	else if (s.equals("B") || s.equals("b")){
           note_float = 2; 
           notename = "B"; }

	else if (s.equals("C") || s.equals("c")){
           note_float = 3; 
           notename = "C"; } 
 
	else if (s.equals("C#") || s.equals("c#") || s.equals("Db") || s.equals("db")) {  
           note_float = 4; 
           notename = "C♯/D♭"; 
        }

	else if (s.equals("D") || s.equals("d")){  
           note_float = 5; 
           notename = "D"; 
        }

	else if (s.equals("D#") || s.equals("d#") || s.equals("Eb")  || s.equals("eb")){  
           note_float = 6; 
           notename = "D♯/E♭"; }

	else if (s.equals("E") || s.equals("e") || s.equals("Fb") || s.equals("fb"))   {  
           note_float = 7; 
           notename = "E"; }

	else if (s.equals("E#") || s.equals("e#") || s.equals("F") || s.equals("f"))   {  
           note_float = 8; 
           notename ="F"; }

	else if (s.equals("F#") || s.equals("f#")  || s.equals("Gb")  || s.equals("gb")){
           note_float = 9; 
           notename = "F♯/G♭";
        }
	else if (s.equals("G") || s.equals("g")){
           note_float = 10; 
           notename = "G";
        }
	else if (s.equals("G#") || s.equals("g#") || s.equals("Ab") || s.equals("ab")) {
           note_float = 11; 
           notename = "G♯/A♭";
        }

	else if (s.equals("a") || s.equals("A")) {
           note_float = 0;  
           notename = "A"; }

	else {
           note_float = 0;
           notename = "??";
           System.err.println("Invalid note name.  Exiting.\n");
           System.exit(1); }

     //     System.out.println("if-then routine completed");

        octave = oct;

	while(cents > 50){
           note_float += 1; 
           cents -= 100; 	   
           if(note_float >= 12.0)  note_float -= 12.0;
           note_number = (int)note_float;
           setNotename();
	   if(notename.equals("C")) octave += 1;
	   //if(notename.equals("A")  || notename.equals("A#/Bb") || notename.equals("B")) freq *= 2;
	}  

        while(cents < -50){
           note_float -= 1; 
           cents += 100; 
           if(note_float < 0.0)  note_float += 12.0;
           note_number = (int)note_float;
           setNotename();
           if(notename.equals("B")) octave -= 1;
	   //	   if(notename.equals("A")  || notename.equals("A#/Bb") || notename.equals("B")) freq *= 2;	
        }

        setFreq();

	//freq = 32.703196 * Math.pow(2, (note_float - 3 + (cents / 100)) / 12.0) * Math.pow(2, octave - 1);
	if(notename.equals("A")  || notename.equals("A#/Bb") || notename.equals("B")){ 
	    double f = freq.magnitude();
          freq.set(f * 2);//perhaps this can be done more elegantly
      }// *= 2;	

        halfsteps = note_float + (octave - 4) * 12;
        speed = new Velocity(340.29, new Angle());
	wavelength = new displacement(speed.MperS() / freq.magnitude());
    }

    public Note(double nnum, int oct){
	count++;
	setLabel("NOTE #" + count);

	freq = new Scalar(0, new Unit("Hertz", "Hz"));
        wavelength = new displacement();

        cents = 0;
        speed = new Velocity(340.29, new Angle()); 
        note_number = (int)nnum;
        note_float = nnum;
        octave = oct; 
	    
	//        System.out.println("note_number = "+note_number);
        setNotename();
        setFreq();
        setOct();
        setFreq();
	    
       halfsteps = 12.0 * Math.log(freq.magnitude() / 440.0) / Math.log(2.0);
       local_semitones = halfsteps % 12; //HSs + or - A in this octave
       local_semitones=(double)Math.round(local_semitones * 100) / 100;
       if(local_semitones < -6.0) local_semitones += 12.0;
       else if (local_semitones >= 6.0)
           { local_semitones = -1 * (12.0 - local_semitones);}
       cents = 100 * (local_semitones - (int)local_semitones);
       note_float = local_semitones;
       while (note_float < 0) note_float += 12.0; 
       note_number = (int)note_float;	    
	    // halfsteps = note_float + (octave - 4) * 12;
	    //freq = 32.703196 * Math.pow(2, (note_float - 3 + (cents / 100)) / 12.0) * Math.pow(2, octave - 1);
       //Lets see if this weird fix fixes it
       //       if notename.equals('A♯/B♭'){freq.set}

    }


    //
    // CALCULATE
    ///////////////
    private void setOct(){
	octave = 1 + (int)(Math.log(freq.magnitude() / (440 * Math.pow(2, -3.75))) / Math.log(2));
    }
    
    
    private void setFreq(){
       freq.set(32.703196 * Math.pow(2, (note_float - 3 + (cents / 100)) / 12.0) * Math.pow(2, octave - 1));
       if(notename.equals("A")  || notename.equals("A♯/B♭") || notename.equals("B"))  {
	   //freq *= 2;
	   double f=freq.magnitude();
	   //          freq.set(freq.magnitude() * 2);	
	            freq.set(f * 2);
       }
    } 
    
    private void setNotename(){
      switch(note_number){
      case 0:
	  notename="A";
          break;
      case 1:
          notename="A♯/B♭";
          break;
      case 2:
          notename="B";
          break;
      case 3:   
          notename="C";
          break;   
      case 4:
          notename="C♯/D♭";
          break;
      case 5:
          notename="D";
          break;
      case 6:
          notename="D♯/E♭";
          break;
      case 7:
          notename="E";
          break;
      case 8:
          notename="F";
          break;
      case 9:
          notename="F♯/G♭";
          break;
      case 10:
          notename="G";
          break;
      case 11:
          notename="G♯/A♭";
          break;
      default:
	  notename="unknown";
	  break;
      }
   }


    //
    // I/O
    /////////
    public void troubleshoot()
    {
	System.out.println("halfsteps = " + halfsteps);
	System.out.println("local_semitones = " + local_semitones);
	System.out.println("note_number = " + note_number);
	System.out.println(cents + " cents");
	System.out.println("Note name: " + notename);
	System.out.println("Octave:" + octave);
    }   
    
    public void printHalfsteps()
    {
	System.out.println (halfsteps + " half-steps above A440");      
        System.out.println (local_semitones + " half-steps above the nearest A");
    }
    
    public void printall(){
        printfreq();
        printHalfsteps();
        System.out.println(notename);
        System.out.println(cents);
      	    //        System.out.println(note_number);
	    //        System.out.println("Octave " + octave);
    }

    public void niceprint(){
        NumberFormat centsFormat = new DecimalFormat("+#,###.00;-#");
	        //   numberFormat = new DecimalFormat("#0.00#");
        System.err.print(TuiTeX.rightAlign(notename + "[" +octave + "]" + centsFormat.format(cents / 100.0), 12));
        System.err.print("\t(" + freq.str() + ")");
	    //	System.out.println("local_semitones="+local_semitones);
    //System.err.print("\n");
        System.err.print("\n");
    }

    public void printfreq(){
	NumberFormat numberFormat = new DecimalFormat("#0.00#");
        System.out.print(numberFormat.format(freq.magnitude()) + " ");
    }
}
