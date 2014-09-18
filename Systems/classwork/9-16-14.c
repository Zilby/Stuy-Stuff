#include <stdio.h>
#include <stdlib.h>

int main(){
  int i;
  double d;
  char c;
  int *ip=&i; //declares as address of a variable
  double *dp=&d; 
  char *cp=&c;
  printf("Int: %lu\nDouble: %lu\nChar: %lu\n",ip,dp,cp);
  ip++; //note, int grows by 4
  dp++; //double grows by 8
  cp++; //char grows by 1 (byte(s))
  printf("\nInt+1: %lu\nDouble+1: %lu\nChar+1: %lu\n",ip,dp,cp);
  return 0;
}
