#include <stdio.h>

int main()
{
    char text[100];

    if(fgets(text, 80, stdin) != NULL)
        printf("\033[1m%s\033[0m", text);

    return 0;
}
