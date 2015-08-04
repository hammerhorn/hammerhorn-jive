#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sigintHandler(int);  // If ^C is pressed, unhide the cursor.
int spin(void);  // Displays spinning line animation to stdout.

int main(int argc, char* argv[])
{
    signal (SIGINT, sigintHandler);
    printf("\033[?25l");  // Hide cursor
    spin();
    return 0;
}

void sigintHandler (int sig_num)
{
  signal (SIGINT, sigintHandler);
  printf ("\b\b  \n\033[?25h");
  exit (0);
}

int spin(void)
{
  int count=0;
  setbuf(stdout, NULL);  // Make visible from this scope.
  while(1){
    printf("/");
    nanosleep((struct timespec[]){{0, 75000000}}, NULL);
    printf("\b|");
    nanosleep((struct timespec[]){{0, 75000000}}, NULL);
    printf("\b\\");
    nanosleep((struct timespec[]){{0, 75000000}}, NULL);
    printf("\b-");
    nanosleep((struct timespec[]){{0, 75000000}}, NULL);
    printf("\b");
  }
  return 0;
}

