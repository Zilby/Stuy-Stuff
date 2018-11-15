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
  if (points->lastcol >= points->cols - 1 )
    grow_matrix(points , points->cols * 2);
  points->m[0][points->lastcol] = x;
  points->m[1][points->lastcol] = y;
  points->m[2][points->lastcol] = z;
  points->lastcol += 1;
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
  add_point(points , x0 , y0 , z0);
  add_point(points , x1 , y1 , z1);
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
  int i; 
  for ( i = 0; i < points->lastcol; i+= 2){
    draw_line(points->m[0][i] , points->m[1][i] , points->m[0][i+1] , 
    	      points->m[1][i+1] , s , c);
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
  if (x0 > x1){
    int i = x0; x0 = x1; x1 = i; i = y0; y0 = y1; y1 = i; }
  double slope = 0;
  if (x1 - x0 != 0)
    slope = (y1 - y0) / (x1 - x0);
  else
    slope = 0.5;
  int a = 2 * (y1 - y0);
  int b = -2 * (x1 - x0);
  if (slope > 1){
    int d = a / 2 + b;
    while (y0 < y1){
      s[x0][y0] = c;
      if (d < 0){
	x0 += 1; d += a; }
      y0 += 1; d += b;
    }
  }
  else if (slope > 0){
    int d = a + b / 2;
    while (x0 < x1){
      s[x0][y0] = c;
      if (d > 0){
	y0 += 1; d += b; }
      x0 += 1; d += a;
    }
  }
  else if (slope < -1){
    int d = a / 2 - b;
    while (y0 > y1){
      s[x0][y0] = c;
      if (d > 0){
	x0 += 1; d += a; }
      y0 -= 1; d -= b;
    }
  }
  else if (slope < 0){
    int d = a - b / 2;
    while (x0 < x1){
      printf("%d\n" , x0);
      s[x0][y0] = c;
      if (d > 0){
	y0 -= 1; d -= b; }
      x0 += 1; d += a;
    }
  } 
}
