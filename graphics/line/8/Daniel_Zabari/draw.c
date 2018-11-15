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
	if (point->cols == points->lastcol)
		grow_matrix(points,points->cols*2);
	int i;
	int a[3];
	a[0]=x;
	a[1]=y;
	a[2]=z;
	for (i=0;i<3;i++){
		points->m[(points->lastcol)++]=a[i];
	}
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
	       	add_point(points,x0,y0,z0);
	       	add_point(points,x1,y1,z1);
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
