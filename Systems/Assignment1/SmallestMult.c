#include <stdio.h>
#include <stdlib.h>

int main(){
  int x=1;
  int tf=1;
  while(tf){
    if(x%14==0&&
       x%15==0&&
       x%16==0&&
       x%17==0&&
       x%18==0&&
       x%19==0&&
       x%20==0&&
       x%13==0&&
       x%12==0&&
       x%11==0){
      tf=0;
    }else{
      x++;
    }
  }
  printf("~~~***   %d   ***~~~\n",x);
}
       
