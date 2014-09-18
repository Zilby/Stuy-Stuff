#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {

    char s[10]="hello";
    int x=0;
    while(s[x]!=0){
      x++;
    }
    printf("%s: %d\n",s,x);
}
