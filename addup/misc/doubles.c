#include <stdio.h>

int main(int argc, char* argv[]) 
{
  float tab[1000];
  //  f = fopen(stdin, "r");
  int i = 0;
  while(feof(stdin) == 0){
     fscanf(stdin, "%f\n", &tab[i]);
     i++;
  }

  //  double *tab;
  //int num = 1000;
  //tab = malloc(num * sizeof *tab);
  //while(..){
    //  if(i >= num) num *= 2;
    //tab = realloc(tab, num * sizeof *tab);
  //}
  return 0;
}
