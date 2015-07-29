#include<time.h>
#include<stdlib.h>
#include <stdio.h>

#define SIDES 6

int main(int argc, char* argv[]) 
{
  int left, right, sum;
  srand(time(NULL));
  left = rand() % SIDES + 1;
  right = rand() % SIDES + 1;
  sum = left + right;
  printf("%d = %d + %d\n", sum, left, right);
  return 0;
}
