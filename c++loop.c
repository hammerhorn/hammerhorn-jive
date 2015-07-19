#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sigintHandler (int);

main (int argc, char *argv[])
{
  // I used quite a big buffer.  This could be optimized.
  char lines[100][100];
  char total[1000] = "";
  char includes[100] = "";
  //string lines[100],
    total,
    includes;

  int i, len;
  FILE *file_ptr;

  signal (SIGINT, sigintHandler);

  while (1)
    {
      int count;
      total[0] = '\0';

      printf ("%%");

      i = 0;
      while (fgets (lines[i], 80, stdin) != NULL)
	i++;
      len = i;
      for (i = 0; i < len; i++)
	{
	  if (!strcmp (substr (lines[i], 0, 8), "#include"))
	    {
	      strcat (includes, lines[i]);
	    }
	  else
	    {
	      strcat (total, lines[i]);
	    }
	}
      file_ptr = fopen ("tmp.cpp", "w");
      fprintf (file_ptr, "#include <iostream>\n");
      fprintf (file_ptr, "%s\n", includes);
      fprintf (file_ptr, "\nusing namespace std;\n\nint main(int argc, char* argv[])\n{");
      fprintf (file_ptr, "%s", total);
      fprintf (file_ptr, "return 0;}");
      fclose (file_ptr);
      if (!system ("g++ ./tmp.cpp"))
	system ("./a.out");
    }

  return 0;
}


void
sigintHandler (int sig_num)
{
  signal (SIGINT, sigintHandler);
  printf("\b\b\b");
  remove("./tmp.c");
  remove("./a.out");
  exit (0);
}
