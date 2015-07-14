#include <stdio.h>

int main(int argc, char* argv[])
{
    char text[100];

    fgets(text, 80, stdin);
    printf("\033[1m%s\033[0m", text);

    return 0;
}
