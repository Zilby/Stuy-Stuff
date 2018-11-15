#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>


int sq(int x){

  return x * x;
}

int main(){

  int red, blue, green;
  int fd = open("pic.ppm", O_CREAT | O_TRUNC | O_WRONLY, 0644);

  char line[256];

  sprintf( line, "P3\n500 500\n255\n" );
  write( fd, line, strlen(line) );


  int h,k;
  h = 250;
  k = 250;

  int i,j;
  for (i = 0; i<500; i++){
    for (j = 0; j < 500; j++){

      red = 0;
      green = 0;
      blue = 0;
      
      if((sq(i-h) + (sq(j-k))) <= sq(100) ){
	red = i%255;
	green = 255;
	blue = j%255;
      }

      
      /*if((i+j)%2){
	red = i%255;
	green = j%255;
	blue = 255;
      }   
      */

      sprintf( line, "%d %d %d ", red, green, blue);
      write( fd, line, strlen(line) );
  
    }
  }




  close(fd);
  
}
