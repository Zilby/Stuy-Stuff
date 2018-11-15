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
  c.green = 0;
  c.blue = 0;

  int i, j;

  for( i=0; i<XRES; i++) 
    for ( j=0; j<YRES; j++) {

      c.red = 255;
      c.green = 255;
      c.blue = 255;

      plot( s, c, i, j);
    }

  c.red = 0;
  c.green = 0;
  c.blue = 0;

  struct matrix *mat = new_matrix(3 , 500);

  add_edge(mat , 100, 100 , 0, 200, 200, 0);
  add_edge(mat , 50, 50 , 0, 10, 10, 0);
  add_edge(mat , 75, 300 , 0, 25, 25, 0);
  add_edge(mat , 300, 25 , 0, 200, 450, 0);

  draw_lines(mat , s , c);

  display( s );    
  save_ppm(s,  "image" );
  save_extension(s, "image.jpg");
  
}  
