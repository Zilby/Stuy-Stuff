#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>


int main(){
  
  int fd = open("pic.ppm", O_CREAT & O_WRONLY & O_TRUNC, 0644);

  char header[1024] = "P3 500 500 255\n";
  write(fd, header, 1024);


  close(fd);
}
