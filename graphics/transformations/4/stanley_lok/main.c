#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"

int main() {

  screen s;
  color c;

  c.red = 0;
  c.green = 255;
  c.blue = 255;

  int i, j;

  for( i=0; i<XRES; i++) 
    for ( j=0; j<YRES; j++) {
      plot( s, c, i, j);
    }
  
  //Change color for the lines

  c.red = 100;
  c.green = 100;
  c.blue = 100;
  
  struct matrix * trans1;
  struct matrix * trans2;
  struct matrix * trans3;
  
  trans1 = rotate_x(90);
  trans2 = rotate_y(90);
  trans3 = rotate_z(90);
  
  
  display( s );    
  save_ppm(s,  "image" );
  save_extension(s, "image.jpg");
  
}  
