#include <stdio.h>
#include <string.h>

int detect_colon(char*);

int main(int argc, char* argv[]) 
{
    /* Make sure argument is present. */
    if(argc < 2){
        puts("Argument required.");
        return -1;
    }

    int colon_present = detect_colon(argv[1]), mins;
    double total_seconds = 0, secs;
    char *minutes, *seconds;

    // If there is a colon, output seconds
    if(colon_present){
	minutes = strtok(*(argv + 1), ":");
        //char *seconds = *(argv + 2 + sizeof(minutes));
	seconds = strtok(NULL, "\0");
	//printf("\"%s\" + \"%s\"", minutes); //, seconds);
	mins = atoi(minutes);
        secs = atof(seconds);        
        printf("%g\n", mins * 60 + secs);
        //printf("%d:%g\n", mins, secs);
    }    
    //If there is no colon, output mm:ss format
    return 0;
}

int detect_colon(char *string)
{
    // See if argument string contains a ':'.
    int count,
        flag = 0; //really a bool

    for(count = 0; count <= sizeof(string); count++){
        if(string[count] == ':'){
            flag = 1;
            break;
        }
    }
    return flag;
}

