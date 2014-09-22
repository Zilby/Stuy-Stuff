#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int len(char t[]); //compiler needs to know how function is supposed to work
                   //before doing main
//int len(char) works too

int main() {
    char s[10]="hello";
    printf("%s: %d\n",s,slen(s));
    return 0;
}

int slen(char t[]){
    int x=0;
    while(t[x]){
      x++;
    }
    return x;
}

