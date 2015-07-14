#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char* argv[]) 
{
    if(argc == 2)
        printf("%.15lf\n", M_PI * atof(argv[1]));
  
    else if(argc == 3){
        if( !strcmp(argv[1], "-o") || !strcmp(argv[1], "--over") )
            printf("%.15lf\n", M_PI / atof(argv[2]));
    }
    else if (argc == 1)
        printf("3.14159265358979323846\n");

    return 0;
}
