#include <stdio.h>
#include <stdlib.h>

int main(){
  /*
  int nums[100];
  int placeholder=0;
  int x=0;
  while(x<=1000){
    if(x%3==0||x%5==0){
      int y=0;
      int TF=1;
      while(y<100){
	if(nums[y]==x){
	  TF=0;
	}else{
	  y++;
	}
      }
      if(TF){
	nums[placeholder]=x;
      }
    }
    x++
  }
  */
  int x=0;
  int ans=0;
  while(x<=1000){
    if(x%3==0||x%5==0){
      ans+=x;
    }
    x++;
  }
  printf("%d\n",ans);
}
