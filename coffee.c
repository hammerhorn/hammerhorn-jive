#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/*
 TODO:
 - Hide the cursor and add a sigint handler that restores it.
 - Move mmss code into the main program.
 - Use ANSI escape sequences to make a smoother animation.
*/

int main(int argc, char *argv[])
{
    int seconds,
        since,
        remaining;
    char buffer[6];

    if(argc == 1)
	seconds = 330;
    else
	seconds = atof(argv[1]);

    since = (unsigned) time(NULL);
    remaining = seconds;

    while(remaining > 0) {
	system("clear");
	sprintf(buffer, "echo -n $(mmss.jar %d) remaining", remaining);
	// why is echo used?
	system(buffer);
	nanosleep((struct timespec[]) { {
		  0, 400000000}}, NULL);
	remaining = seconds - (unsigned) time(NULL) + since;
    }

    system("toilet \"Done\"");
    system("play -n synth .5 sin 1000 vol 0.05 > /dev/null 2>&1");
    exit(0);
}

void sigintHandler(int sig_num)
{
    signal(SIGINT, sigintHandler);
    printf("");
    exit(0);
}
