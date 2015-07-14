#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cjh.h"

// Remove trailing newline.
void chomp(char* line)
{
  line[strcspn(line, "\n")] = '\0';
}

// Get substring from index1 until index2.
char* substr(char* buf, int start, int end)
{
  char* subbuff = malloc(end - start + 1);
  strncpy(subbuff, buf + start, end);
  subbuff[end] = '\0';
  return subbuff;
}
