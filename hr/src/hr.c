#include <termios.h>
#include <sys/ioctl.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    struct winsize ws;
    ioctl(0, TIOCGWINSZ, &ws);
    int i = 0;
    for(; i < ws.ws_col; ++i) printf("-");
    printf("\n");
    return 0;
}
