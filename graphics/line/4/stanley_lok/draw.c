#include <stdio.h>
#include <stdlib.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"
#include "matrix.h"

/*======== void add_point() ==========
Inputs:   struct matrix * points
         int x
         int y
         int z 
Returns: 
adds point (x, y, z) to points and increment points.lastcol
if points is full, should call grow on points
====================*/
void add_point( struct matrix * points, int x, int y, int z) {
  if(points->lastcol > points->cols - 1){
    grow_matrix(points, points->cols); //should double the matrix
  }
  points->m[lastcol][x];
  points->m[lastcol][y];
  points->m[lastcol][z];
  points->m[lastcol][1];

  points->lastcol = points->lastcol + 1;
}

/*======== void add_edge() ==========
Inputs:   struct matrix * points
          int x0, int y0, int z0, int x1, int y1, int z1
Returns: 
add the line connecting (x0, y0, z0) to (x1, y1, z1) to points
should use add_point
====================*/
void add_edge( struct matrix * points, 
	       int x0, int y0, int z0, 
	       int x1, int y1, int z1) {

  add_point(points, x0, y0, z0);
  add_point(points, x1, y1, z1);
}

/*======== void draw_lines() ==========
Inputs:   struct matrix * points
         screen s
         color c 
Returns: 
Go through points 2 at a time and call draw_line to add that line
to the screen
====================*/
void draw_lines( struct matrix * points, screen s, color c) {

  int current_col = 0;
  while (current_col < points->lastcol){
    draw_line(points->m[current_col][0],
	      points->m[current_col][1],
	      points->m[current_col][2],
	      points->m[current_col + 1][0],
	      points->m[current_col + 1][1],
	      points->m[current_col + 1][2],
	      s,
	      c);
    current_col += 2;
  }
}



/*======== void draw_line() ==========
Inputs:  int x0
         int y0
         int x1
         int y1
         screen s
         color c 
Returns: 

Plots all the points necessary to draw line (x0, y0) - (x1, y1) onto
screen c using color c
====================*/
void draw_line(int x0, int y0, int x1, int y1, screen s, color c) {
  
}
