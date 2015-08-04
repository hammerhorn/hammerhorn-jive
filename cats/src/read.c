#include <stdio.h>

int main(int argc, char* argv[])
{
  char buffer[100];
  read(stdin, buffer, 99);
  printf("%s", buffer);

  return 0;
}
