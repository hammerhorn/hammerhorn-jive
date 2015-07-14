#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    float abv1,
          abv2,
          target_abv,
          target_vol,
          vol1,
          vol2;

    if(argc-1 == 0) { 
        printf("%%ABV of first ingredient: ");
        scanf("%f", &abv1);
    } 
    else abv1 = atof(argv[1]);

    if(argc-1 <= 1) {
        printf("%%ABV of second ingredient: ");
        scanf("%f", &abv2); 
    }   
    else abv2 = atof(argv[2]);

    if(argc-1 <= 2) { 
        printf("%%Target ABV: ");
        scanf("%f", &target_abv);
    }
    else target_abv = atof(argv[3]);

    if(argc-1 <= 3) {
        printf("Target volume (fl. oz.): ");
        scanf("%f", &target_vol);
    }
    else target_vol=atof(argv[4]);

    vol1 = target_vol * (target_abv - abv2)/(abv1 - abv2);
    vol2 = target_vol - vol1;

    printf("\nYou will need %.1f fl. oz. of the first ingredient (%.1f%% ABV), and", vol1, abv1);
    printf("\n              %.1f fl. oz. of the second ingredient (%.1f%% ABV).\n\n", vol2, abv2);

    return 0;
}
