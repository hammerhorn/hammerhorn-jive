#include <iostream>

#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main (int argc, char *argv[])
{
    double numbers[10], total = 0.0;
    int count;

    if(argc > 1)
        for(count = 1; count < argc; count++)
 	     total += atof (argv[count]);
    else {
        float tab[1000];
        int i = 0;

	while (feof (stdin) == 0){           //
	    fscanf (stdin, "%f\n", &tab[i]); // translate to C++
	    total += tab[i];                 //
	    i++;
	}
    }

    cout << total << endl;
    return 0;
}
