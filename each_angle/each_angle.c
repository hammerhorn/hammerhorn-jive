#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int sides;

    // If arg given, convert to int, sides.
    // Else, exit.
    if(argc == 2)
        sides = atoi(argv[1]);
    else {
        printf("\n\t Use: each_angle $NUMBER_OF_SIDES\n\n");
        return -1;
    }

    if(sides >= 3){
        printf("In a figure with %d sides,\n", sides);
        printf("\n\tsum of all angles = %g°\n", (sides - 2) * 180.0);
        printf("\t    average angle = %g°\n\n", (sides - 2) * 180.0 / sides);
    } 
    else printf("You need at least 3 sides to form a polygon.\n");

    return 0;
}
