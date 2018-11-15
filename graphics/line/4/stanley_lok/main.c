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

      c.red = random() % (MAX_COLOR + 1);
      c.green = random() % (MAX_COLOR + 1);
      c.blue = random() % (MAX_COLOR + 1);

      plot( s, c, i, j);
    }

  display( s );    
  save_ppm(s,  "image" );
  save_extension(s, "image.jpg");
  
}  
