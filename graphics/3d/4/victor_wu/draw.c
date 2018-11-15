#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"
#include "matrix.h"


/*======== void add_circle() ==========
  Inputs:   struct matrix * points
            double cx
	    double cy
	    double y
	    double step  
  Returns: 


  03/16/12 19:53:52
  jdyrlandweaver
  ====================*/
void add_circle( struct matrix * points, 
		 double cx, double cy, 
		 double r, double step ) {
  double i;
  double oldX = cx + r;
  double oldY = cy + 0;
  double newX;
  double newY;
  
  for(i = 0; i < 2 + step; i += step) {
    double rad = M_PI * (i + step);
    newX = cx + r * cos(rad);
    newY = cy + r * sin(rad);
    add_edge(points, oldX, oldY, 0, newX, newY, 0);
    oldX = newX;
    oldY = newY;
  }
}

void add_prism(struct matrix * points,
	       double x, double y, double z,
	       double w, double h, double d) { 
  add_edge(points, x, y, z, x, y, z);
  add_edge(points, x+w, y, z, x+w, y, z);
  add_edge(points, x, y-h, z, x, y-h, z);
  add_edge(points, x, y, z-d, x, y, z-d);
  add_edge(points, x+w, y-h, z, x+w, y-h, z);
  add_edge(points, x+w, y, z-d, x+w, y, z-d);
  add_edge(points, x, y-h, z-d, x, y-h, z-d);
  add_edge(points, x+w, y-h, z-d, x+w, y-h, z-d);
} 

void add_sphere(struct matrix * points,
		double x, double y, double z,
		double r, double step) {
  double oldX = x + r;
  double oldY = y;
  double oldZ = z;

  int i, j;
  
  for(i = 0; i < 2 + step; i += step) {
    double radOne = M_PI * (i + step);
    double rc = r * cos(radOne);
    double rs = r * cos(radOne);
    for(j = 0; j < 2 + step; j += step) {
      double radTwo = M_PI * (j + step);
      double newX = x + rc;
      double newY = y + rs * cos(radTwo);
      double newZ = z + rs * sin(radTwo);
      add_edge(points, oldX, oldY, oldZ, oldX, oldY, oldZ);
      oldX = newX;
      oldY = newY;
      oldZ = newZ;
    }
  }
}

void add_torus(struct matrix * points,
	       double x, double y, double z,
	       double r1, double r2, double step) {
  double oldX = x + r1 + r2;
  double oldY = y;
  double oldZ = z;

  int i, j;
  
  for(i = 0; i < 2 + step; i += step) {
    double radOne = M_PI * (i + step);
    double rc = r1 * cos(radOne);
    double rs = r1 * cos(radOne);
    for(j = 0; j < 2 + step; j += step) {
      double radTwo = M_PI * (j + step);
      double newX = x + cos(radTwo) * (rc + r2);
      double newY = y + rs;
      double newZ = z + sin(radTwo) * (rc + r2);
      add_edge(points, oldX, oldY, oldZ, oldX, oldY, oldZ);
      oldX = newX;
      oldY = newY;
      oldZ = newZ;
    }
  }
}


/*======== void add_point() ==========
Inputs:   struct matrix * points
         int x
         int y
         int z 
Returns: 
adds point (x, y, z) to points and increment points.lastcol
if points is full, should call grow on points
====================*/
void add_point( struct matrix * points, double x, double y, double z) {
  
  if ( points->lastcol == points->cols )
    grow_matrix( points, points->lastcol + 100 );

  points->m[0][points->lastcol] = x;
  points->m[1][points->lastcol] = y;
  points->m[2][points->lastcol] = z;
  points->m[3][points->lastcol] = 1;

  points->lastcol++;
}

/*======== void add_edge() ==========
Inputs:   struct matrix * points
          int x0, int y0, int z0, int x1, int y1, int z1
Returns: 
add the line connecting (x0, y0, z0) to (x1, y1, z1) to points
should use add_point
====================*/
void add_edge( struct matrix * points, 
	       double x0, double y0, double z0, 
	       double x1, double y1, double z1) {
  add_point( points, x0, y0, z0 );
  add_point( points, x1, y1, z1 );
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
 
  if ( points->lastcol < 2 ) {
    
    printf("Need at least 2 points to draw a line!\n");
    return;
  }

  for ( i = 0; i < points->lastcol - 1; i+=2 ) {

    draw_line( points->m[0][i], points->m[1][i], 
	       points->m[0][i+1], points->m[1][i+1], s, c);
  } 	       
}

void draw_line(int x0, int y0, int x1, int y1, screen s, color c) {
 
  int x, y, d, dx, dy;

  x = x0;
  y = y0;
  
  //swap points so we're always draing left to right
  if ( x0 > x1 ) {
    x = x1;
    y = y1;
    x1 = x0;
    y1 = y0;
  }

  //need to know dx and dy for this version
  dx = (x1 - x) * 2;
  dy = (y1 - y) * 2;

  //positive slope: Octants 1, 2 (5 and 6)
  if ( dy > 0 ) {

    //slope < 1: Octant 1 (5)
    if ( dx > dy ) {
      d = dy - ( dx / 2 );
  
      while ( x <= x1 ) {
	plot(s, c, x, y);

	if ( d < 0 ) {
	  x = x + 1;
	  d = d + dy;
	}
	else {
	  x = x + 1;
	  y = y + 1;
	  d = d + dy - dx;
	}
      }
    }

    //slope > 1: Octant 2 (6)
    else {
      d = ( dy / 2 ) - dx;
      while ( y <= y1 ) {

	plot(s, c, x, y );
	if ( d > 0 ) {
	  y = y + 1;
	  d = d - dx;
	}
	else {
	  y = y + 1;
	  x = x + 1;
	  d = d + dy - dx;
	}
      }
    }
  }

  //negative slope: Octants 7, 8 (3 and 4)
  else { 

    //slope > -1: Octant 8 (4)
    if ( dx > abs(dy) ) {

      d = dy + ( dx / 2 );
  
      while ( x <= x1 ) {

	plot(s, c, x, y);

	if ( d > 0 ) {
	  x = x + 1;
	  d = d + dy;
	}
	else {
	  x = x + 1;
	  y = y - 1;
	  d = d + dy + dx;
	}
      }
    }

    //slope < -1: Octant 7 (3)
    else {

      d =  (dy / 2) + dx;

      while ( y >= y1 ) {
	
	plot(s, c, x, y );
	if ( d < 0 ) {
	  y = y - 1;
	  d = d + dx;
	}
	else {
	  y = y - 1;
	  x = x + 1;
	  d = d + dy + dx;
	}
      }
    }
  }
}

