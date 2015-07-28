#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double total = 0.0;
    int count;

    if(argc > 1)
	for(count = 1; count < argc; count++)
	    total += atof(argv[count]);

    else {
	float tab[1000];
	int i = 0,
            vals_read;

	while(feof(stdin) == 0) {
	    vals_read = fscanf(stdin, "%f\n", &tab[i]);
	    total += tab[i];
	    i += vals_read;
	}
    }

    printf("%g\n", total);
    return 0;
}
