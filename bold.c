#include <stdio.h>

/* Boldens a single line of text from pipe or stdin. */

int main(int argc, char* argv[])
{
    char text[100];

    fgets(text, 80, stdin);
    printf("\033[1m%s\033[0m", text);

    return 0;
}
