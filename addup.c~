#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double numbers[10],
           total = 0.0;
    int count;

    // If args present, add them up.
    if(argc > 1)
        for(count = 1; count < argc; count++)
            total += atof(argv[count]);

    // Otherwise, get values from stdin and add them up
    else {
        float tab[1000];
        int i = 0;

        while(feof(stdin) == 0){
            fscanf(stdin, "%f\n", &tab[i]);
            total += tab[i];
            i++;
        }
    }

    // Output the total.
    printf("%g\n", total);
    return 0;
}
