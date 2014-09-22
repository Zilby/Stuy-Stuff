#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {
  char s[4];

  s[0] = 'h';
  s[1] = 'i';
  s[2] = '!';
  s[3] = 0; //need null character because default value is not null but randomized

  printf("s :%s:\n", s);
  printf("strlen(s): %lu\n", strlen(s));

  return 0;
}
