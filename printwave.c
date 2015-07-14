#include <math.h>
#include <stdio.h>

void print_title(void);

int main(int argc, char* argv[]) 
{
    int toggle = 0, //This could be a bit
    iter_count = 0,
      width,
      indent = 0,//(width - 10) * math;
      count;
    double s;

    print_title();

    printf("\033[?25l"); // Hide cursor
    while(1){
      s = iter_count / 4.0;
      width = 80; // Make this dynamic
      indent = ((width - 10) * sin(s) + width - 8) / 2;
      for(count = 0; count < indent; count++) printf(" ");
      if(toggle == 1){
          printf("CREATIVE\n");
          toggle = 0;
      }
      else{
          printf("COMPUTING\n");
          toggle = 1;
      }
      //sleep
      iter_count += 1;
    }
    printf("\033[?25h"); // Unhide cursor



    return 0;
}

void print_title(void)
{
    int count;
    printf("\x1b[2J\x1b[H");
    for(count = 0; count < 30; count++) printf(" ");
    printf("SINE WAVE\n");
    for(count = 0; count < 15; count++) printf(" ");
    printf("CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY");
    for(count = 0; count < 5; count++) printf("\n");
    printf("Press Enter to Continue");
    while( getchar() != '\n');
}

