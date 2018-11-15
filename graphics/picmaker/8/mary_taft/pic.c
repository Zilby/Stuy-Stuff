#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int main(){
  
  int fd;
  char buf[32];
  int xres, yres, max_val;

  xres = 700;
  yres = 500;
  max_val = 255;
  
  fd = open("pic.ppm", O_CREAT | O_EXCL | 0666);
  sprintf(buf, "P3 \n %d %d \n %d", xres, yres, max_val);
  write(fd, buf, sizeof(buf));
  
  int i, j; //counters
  int r, g, b; //colors
  
  for(i=0; i<xres; i++){
    for(j=0; j<yres; j++){
      
      if(i<xres/3){
	r = 200;
	g = i%256;
	b = j%256;
      }else if(i<2*xres/3){
	r = i%256;
	g = 200;
	b = j%256;
      }else if(i<xres){
	r = i%256;
	g = j%256;
	b = 200;
      }

      sprintf(buf, "%d %d %d \t", r, g, b);
      write(fd, buf, sizeof(buf));

    }

    write(fd, "\n", 1);
    
  }
  
}
