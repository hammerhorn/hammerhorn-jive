import java.text.*;

public class CallNum
{

    String dewey = "";
    String [] desc = {"unkown", "unknown", "unknown"};
    boolean deprecated = false;

    public CallNum(double dd)
    { 
        dewey =dd+"";
        describe();
    }
 
    public void describe()
    {
        int field1 =(int)(Double.parseDouble(dewey) / 100);
        int field2 =(int)((Double.parseDouble(dewey) % 100) / 10);
        int field3 =(int)(Double.parseDouble(dewey) % 10);
 
        switch(field1)
        {
 	    //0xx
   	    case 0:
	        desc[0] = "Computer science, information & general works";
	        switch(field2)
                {
		    //00x
	            case 0:
	                desc[1] = "Computer science, knowledge & systems";
 	            switch(field3)
                    {
	                case 0:
		            desc[2] = "Computer Science, knowledge & general works";
		            break;
		        case 1:
  		            desc[2] = "Knowledge";
		            break;
		        case 2:
		            desc[2] = "The book (i.e., Meta writings about books)";
		            break;
		        case 3:
		            desc[2] = "Systems";
		            break;
                        case 4:
		            desc[2] = "Data processing & computer science";		   
                            break;
		        case 5:
		            desc[2] = "Computer programming, programs & data";
		            break;
		        case 6:
		            desc[2] = "Special computer methods";
		            break;
		        case 7:
		            desc[2] = "[unassigned]";
		            break;
		        case 8:
		            desc[2] = "[unassigned]";
		            break;
		        case 9:
		            desc[2] = "[unassigned]";
		            break;
                        default:
		            desc[2] = "unknown";
                   }  
                   break;
	           //01x
               case 1:
		   desc[1] = "Bibliographies";
		   switch(field3)
                   {
		       case 0:
	  	           desc[2] = "Modern electronics";
                           break;
		       case 1:
		           desc[2] = "Bibliographies";
   		           break;
		       case 2:
  		           desc[2] = "Bibliographies of individuals";
		           break;
		       case 3:
		           desc[2] = "[unassigned]";
		           break;
		       case 4:
		           desc[2] = "Bibliographies of anonymous & pseudonymous works";
		           break;
		       case 5:
		           desc[2] = "Bibliographies of works from specific places";
		           break;
		       case 6:
		           desc[2] = "Bibliographies of works on specific subjects";
		           break;
		       case 7:
		           desc[2] = "General subject catalogs";
		           break;
		       case 8:
		           desc[2] = "Catalogs arranged by author, date, etc.";
		           break;
		       case 9:
		           desc[2] = "Dictionary catalogs";
		           break;
		       default:
		           desc[2] = "unknown";
                   }
		   break;

		   //02x
	       case 2:
	           desc[1] = "Library & information sciences";
		   switch(field3)
                   {
		       case 0:
		           desc[2] = "Library & information sciences";
                           break;
		       case 1:
		           desc[2] = "Library relationships";
		           break;
		       case 2:
		           desc[2] = "Administration of a physical plant";
		           break;
		       case 3:
		           desc[2] = "Personnel management";
   		           break;
		       case 4:
		           desc[2] = "Regulations for Readers*";
		           deprecated = true;
		           break;
 		       case 5:
               	           desc[2] = "Library operations";
		           break;
		       case 6:
		           desc[2] = "Libraries for specific subjects";
		           break;
		       case 7:
		           desc[2] = "General libraries";
		           break;
		       case 8:
		           desc[2] = "Reading & use of other informational media";
		           break;
		       case 9:
		           desc[2] = "Literary methods*";
		           deprecated = true;
		           break;
		       default:
		           desc[2] = "unknown";
                   }
		   break;

               //03x
	       case 3:
	           desc[1] = "Encyclopdias & books of facts";
	           switch(field3)
                   { 
	               case 0:
	                   desc[2] = "General encyclopedic works";
                           break;
	               case 1:
	                   desc[2] = "Encyclopedias in American English";
	                   break;
	               case 2:
	                   desc[2] = "Encyclopedias in English";
	                   break;
	               case 3:
	                   desc[2] = "Encyclopedias in German";
	                   break;
	               case 4:
	                   desc[2] = "Encyclopedias in French, Occitan & Catalan";
	                   break;
	               case 5:
	                   desc[2] = "Encyclopedias in Italian, Romanian & related languages";
	                   break;
	               case 6:
	                   desc[2] = "Encyclopedias in Spanish & Portuguese";
	                   break;
		       case 7:
		           desc[2] = "Encyclopedias in Slavic languages";
		           break;
		       case 8:
		           desc[2] = "Encyclopedias in Scandinavian languages";
		           break;
		       case 9:
		           desc[2] = "Encyclopedias in \"other\" languages";
		           break;
		       default:
		           desc[2] = "unknown";
                   }               
		   break;

                  // 04x 
	           case 4:
		       desc[1] = "Biographies";
 		       switch(field3)
                       {
                           case 0:
		               desc[2] = "Biographies";
                               break;
		           case 1:
		               desc[2] = "Biographies in American English";
		               break;
		           case 2:
		               desc[2] = "Biographies in English";
		               break;
		           case 3:
		               desc[2] = "Biographies in German";
		               break;
		           case 4:
		               desc[2] = "Biographies in French, Occitan & Catalan";
		               break;
		           case 5:
		               desc[2] = "Biographies in Italian, Romanian & related languages";
		               break;
		           case 6:
		               desc[2] = "Biographies in Spanish & Portuguese";
		               break;
		           case 7:
		               desc[2] = "Biographies in Slavic languages";
		               break;
		           case 8:
		               desc[2] = "Biographiess in Scandinavian languages";
		               break;
		           case 9:
		               desc[2] = "Biographies in \"other\" languages";
		               break;
		           default:
		               desc[2] = "unknown";
                      }
		      break;
                  // 05x
	          case 5:
		      desc[1] = "Magazines, journals & serials";
		      switch(field3)
                      {
		          case 0:
		              desc[2] = "General serial publications";
                              break;
		          case 1:
		              desc[2] = "Serials in American English";
		              break;
		          case 2:
		              desc[2] = "Serials in English";
		              break;
		          case 3:
		              desc[2] = "Serials in other Germanic languages";
		              break;
		          case 4:
		              desc[2] = "Serials in French, Occitan & Catalan";
		              break;
		          case 5:
		              desc[2] = "In Italian, Romanian & related languages";
		              break; 
		          case 6:
		              desc[2] = "Serials in Spanish & Portuguese";
		              break;
		          case 7:
		              desc[2] = "Serials in Slavic languages";
		              break;
		          case 8:
                              desc[2] = "Serials in Scandinavian languages";
		              break;
		          case 9:
		              desc[2] = "";
		              break;
		          default:
		              desc[2] = "unknown";
                      }
		      break;

                      // 06x
  	              case 6:
		          switch(field3)
                          {
		              case 0:
		                  desc[2] = "";
                                  break;
		              case 1:
		                  desc[2] = "";
		                  break;
		              case 2:
		                  desc[2] = "";
		                  break;
		              case 3:
		                  desc[2] = "";
		                  break;
		              case 4:
		                  desc[2] = "";
		                  break;
		              case 5:
		                  desc[2] = "";
		                  break;
		              case 6:
		                  desc[2] = "";
		                  break;
		              case 7:
		                  desc[2] = "";
		                  break;
		              case 8:
		                  desc[2] = "";
		                  break;
		              case 9:
		                  desc[2] = "";
		                  break;
		              default:
		                  desc[2] = "unknown";
                          }
		          desc[1] = "Associations, organizations & museums";
		          break;

                   // 07x
 	           case 7:
		       desc[1] = "News media, journalism & publishing";

		       switch(field3)
                       {
		           case 0:
		               desc[2] = "";
                               break;
		           case 1:
		               desc[2] = "";
		               break;
		           case 2:
		               desc[2] = "";
		               break;
		           case 3:
		               desc[2] = "";
		               break;
		           case 4:
		               desc[2] = "";
		               break;
		           case 5:
		               desc[2] = "";
		               break;
		           case 6:
		               desc[2] = "";
		               break;
		           case 7:
		               desc[2] = "";
		               break;
		           case 8:
		               desc[2] = "";
		               break;
		           case 9:
		               desc[2] = "";
		               break;
		           default:
		               desc[2] = "unknown";
                       }
		       break;

                   // 08x
	           case 8:
		       desc[1] = "General collections";
		       switch(field3)
                       {
		           case 0:
		               desc[2] = "";
                               break;
		           case 1:
		               desc[2] = "";
		               break;
		           case 2:
		               desc[2] = "";
                               break;
		           case 3:
		               desc[2] = "";
		               break;
		           case 4:
		               desc[2] = "";
		               break;
		           case 5:
		               desc[2] = "";
		               break;
		           case 6:
		               desc[2] = "";
		               break;
		           case 7:
		               desc[2] = "";
		               break;
		           case 8:
		               desc[2] = "";
		               break;
		           case 9:
		               desc[2] = "";
		               break;
		           default:
		               desc[2] = "unknown";
                       }
		       break;

                   //09x
	           case 9:
		       desc[1] = "Manuscripts & rare books";
		       switch(field3)
                       {
		           case 0:
		               desc[2] = "";
                               break;
		           case 1:
		               desc[2] = "";
		               break;
		           case 2:
		               desc[2] = "";
		               break;
		           case 3:
		               desc[2] = "";
		               break;
		           case 4:
		               desc[2] = "";
		               break;
		           case 5:
		               desc[2] = "";
		               break;
		           case 6:
		               desc[2] = "";
		               break;
		           case 7:
		               desc[2] = "";
		               break;
		           case 8:
		               desc[2] = "";
		               break;
		           case 9:
		               desc[2] = "";
		               break;
		           default:
		               desc[2] = "unknown";
                       }
	               break;
	           default:
                       desc[1] = "unknown";
               }
            
               break;

          //1xx
          case 1:
	     desc[0] = "Philosophy and psychology";

	     switch(field2)
	     {
	         case 0:
                     desc[1] = "Philosophy";

 	             switch(field3)
		     { 
	                 case 0:
		             desc[2] = "Philosophy and psychology";
		             break;
	                 case 1:
		             desc[2] = "Theory of philosophy";
		             break;
		         case 2:
		             desc[2] = "Miscellany of philosophy";
		             break;
	                 case 3:
		             desc[2] = "Dictionaries and encyclopedias of philosophy";
                             break;
                         case 4:
		             desc[2] = "Essays*";
		             deprecated = true;
		             break;			    
                         case 5:
		             desc[2] = "Serial publications of philosophy";
		             break;
		         case 6: 
		              desc[2] = "Organizations and management of philosophy";
		              break;
	                  case 7:
		              desc[2] = "Education, research, and related topics of philosophy";
		              break;
	                  case 8:
		              desc[2] = "Kinds of persons treatment of philosophy";
                              break;
	                  case 9:
		              desc[2] = "Historical and collected persons treatment of philosophy";
		              break;
		          default:
		              desc[2] = "unknown";
                      }
		      break;
                  case 1:
                      desc[1]="Metaphyisics";
		      break;
                  case 2:
	              desc[1]="Epistemology";
		      break;
	          case 3:
		      desc[1]="Parapsychology & occultism";
		      break;
	          case 4:
		      desc[1]="Philosophical schools of thought";
		      break;
	          case 5:
		      desc[1]="Psychology";
		      break;
	          case 6:
		      desc[1]="Logic";
		      break;
	          case 7:
		      desc[1]="Ethics (Moral philosophy)";
		      break;
	          case 8:
		      desc[1]="Ancient, medieval and Eastern philosophy";
		      break;
	          case 9:
		      desc[1]="Modern Western philosophy";
		      break;
	          default:
		      desc[1]="unknown";
                }
	        break;

            case 2:
	        desc[0]="Religion";
	        break;
            case 3:
                desc[0]="Social sciences";
                break;
            case 4:
	        desc[0]="Language";
	        break;
            case 5:
	        desc[0]="Science";
  	        break;
            case 6:
	        desc[0]="Technology";
	        break;
            case 7:
	        desc[0]="Arts & Recreation";
	        break;
            case 8:
	        desc[0]="Literature";
	        break;
            case 9:
	        desc[0]="History & geography";
	        break;
            default:
	        desc[0]="unknown";
        }
    }


    public void printLong()
    {
        DecimalFormat df = new DecimalFormat("000.####");
        System.out.println(df.format(Double.parseDouble(dewey)));
        for(int count = 0; count < df.format(Double.parseDouble(dewey)).length(); count++)
            System.out.print("-");
        System.out.print("-");
        System.out.println("\n" + desc[0] + "\n|\n`-- " + desc[1] + "\n    |\n    `-- " + desc[2]);
        if(deprecated) 
            System.out.println("* No longer used");
    }

    public void printShort()
    {
        DecimalFormat df = new DecimalFormat("000.####");
        System.out.print(df.format(Double.parseDouble(dewey))+": "+desc[2]);
        //+"\n("+desc[0]+"::"+desc[1]+"::)\n");
    }
}
