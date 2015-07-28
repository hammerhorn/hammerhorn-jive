#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cjh.h"

// "cjh.h" gives us the substr(char*, int, int) function.

void sigintHandler(int);

int main (int argc, char *argv[])
{
    char  lines[100][100],    //
          total[1000] = "",   // This should be optimized.
          includes[100] = ""; //
    int   index, 
          len;
    FILE* file_ptr;

    signal(SIGINT, sigintHandler); // Handle ^C

    while(1){ // Loop continues until ^C is pressed.
        int count;
        total[0] = '\0';

        printf("%%");

        index = 0;
        
        // Accepts C statements until ^D is pressed.
        while(fgets(lines[index], 80, stdin) != NULL)
	        index++;
        len = index;
        for(index = 0; index < len; index++){
 	        if(!strcmp(substr(lines[index], 0, 8), "#include"))
	            strcat(includes, lines[index]);
	        else
	            strcat(total, lines[index]);
	    }

        file_ptr = fopen ("tmp.c", "w");
        fprintf(file_ptr, "#include <stdio.h>\n");
        fprintf(file_ptr, "%s\n", includes);
        fprintf(file_ptr, "int main(int argc, char* argv[])\n{");
        fprintf(file_ptr, "%s", total);
        fprintf(file_ptr, "return 0;}");
        fclose(file_ptr);

        // Uses Tiny C Compiler
        if(!system("tcc ./tmp.c"))
	        system("./a.out");
    }
    return 0;
}

// If ^C is hit, reposition cursor, erase temporary files, and end.
void sigintHandler (int sig_num)
{
    signal(SIGINT, sigintHandler);
    printf("\b\b\b");
    remove("./tmp.c");
    remove("./a.out");
    exit(0);
}
