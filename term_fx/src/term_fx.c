#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) 
{
  int c,
      suppress_newline = 0;
  char buf[100] = "";
  opterr = 0;
   
  while((c = getopt(argc, argv, "bnu")) != -1)
      switch(c)
      {
        case 'b':
          strcat(buf, "\033[1m");
          break;
        case 'n':
          suppress_newline = 1;
          break;
        case 'u':
          strcat(buf, "\033[4m");
          break;
        case '?':
          if(isprint(optopt))
	    fprintf(stderr, "Unknown option `-%c'.\n", optopt);
          else
	    fprintf(stderr, "Unknown option character `\\x%x'.\n", optopt);
          return 1;
        default:
  	  abort();
     }

  int index;
  for(index = optind; index < argc; index++)
      strcat(buf, argv[optind]);
      strcat(buf, " ");
  strcat(buf, "\033[0m");
  if(!suppress_newline)
    strcat(buf, "\n");
  printf("%s", buf);
  return 0;
}
