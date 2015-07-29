#include<iostream>
#include<ctime>
#include<cstdlib>

using namespace std;
int main(int argc, char* argv[]) 
{
  int left, right, sum;
  srand(time(NULL));
  left = rand() % 6 + 1;
  right = rand() % 6 + 1;
  sum = left + right;
  cout << sum << " = " << left << " + " << right << endl;
  return 0;
}
