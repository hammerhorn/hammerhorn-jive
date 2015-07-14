#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
    float abv1, 
          abv2, 
    target_abv, 
    target_vol;

   if(argc - 1 == 0) { 
       cout << "%ABV of first ingredient: ";
       cin >> abv1;
   }  
   else abv1 = atof(argv[1]);
   

   if(argc - 1 <= 1) {
       cout << "%ABV of second ingredient: ";
       cin >> abv2;
   }
   else abv2 = atof(argv[2]);
   

   if(argc - 1 <= 2) { 
       cout << "%Target ABV: ";
       cin >> target_abv;
   }
   else target_abv = atof(argv[3]);
   

   if((target_abv > abv1 && target_abv > abv2) || (target_abv < abv1 && target_abv < abv2)){
       cerr << "Sorry, that's not possible." << endl;
       exit(1);
   }

   if(argc-1 <= 3) {
      cout << "Target volume (fl. oz.): ";
      cin >> target_vol;
   }

   else target_vol=atof(argv[4]);
   
   float vol1 = target_vol * (target_abv - abv2)/(abv1 - abv2);
   float vol2 = target_vol - vol1;

   cout << "\nYou will need " << vol1 << " fl. oz. of the first ingredient (" << abv1 << "% ABV), and";
   cout << "\n              " << vol2 << " fl. oz. of the second ingredient (" << abv2 << "% ABV).\n\n";

   return 0;
}
