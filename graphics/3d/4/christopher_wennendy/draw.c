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
  double current;
  double x , y , x1 , y1;
  x1 = cx + cos(0)*r;
  y1 = cy + sin(0)*r;
  for(current = step; current <= 2 + step; current += step){
    double ang = (current + step) * M_PI;
    x = cx + cos(ang)*r;
    y = cy + sin(ang)*r;
    add_edge(points , x1 , y1 , 0 , x , y , 0);
    x1 = x; y1 = y;
  }
}
void add_sphere( struct matrix * points, 
		 double cx, double cy, 
		 double r, double step ) {
  double current , current2; double x1,y1;
  x1 = cx +r; y1 = cy;
  for(current = step; current <= 2 + step; current += step){
    double ang1 = (current + step) * M_PI;
    double rcos = cos(ang1) * r;
    double rsin = sin(ang1) * r;
    for (current2 = step; current2 <= 2 + step; current2 += step){
      double ang2 = (current2 + step) * r;
      double x = cx + rcos;
      double y = cy + rsin * cos(ang2);
      add_edge(points , x1 ,  y1 , 0  ,x1 , y1 , 0);
      x1 = x;
      y1 = y;
    }
  }
}

void add_torus(struct matrix *points,
	       double cx, double cy,
	       double r, double r2 , double step){
  double current , current2; double x1,y1;
  x1 = cx + r + r2; y1 = cy;
  for(current = step; current <= 2 + step; current += step){
    double ang1 = (current + step) * M_PI;
    double rcos = cos(ang1) * r;
    double rsin = sin(ang1) * r;
    for (current2 = step; current2 <= 2 + step; current2 += step){
      double ang2 = (current2 + step) * r;
      double x = cx + cos(ang2) * (rcos + r2);
      double y = cy + rsin;
      add_edge(points , x1 ,  y1 , 0  ,x1 , y1 , 0);
      x1 = x;
      y1 = y;
    }
  }
}


/*======== void add_curve() ==========
Inputs:   struct matrix *points
         double x0
         double y0
         double x1
         double y1
         double x2
         double y2
         double x3
         double y3
         double step
         int type  
Returns: 

Adds the curve bounded by the 4 points passsed as parameters
of type specified in type (see matrix.h for curve type constants)
to the matrix points

03/16/12 15:24:25
jdyrlandweaver
====================*/
void add_curve( struct matrix *points, 
		double x0, double y0, 
		double x1, double y1, 
		double x2, double y2, 
		double x3, double y3, 
		double step, int type ) {
  struct matrix *coef1 = generate_curve_coefs(x0,x1,x2,x3,type);
  struct matrix *coef2 = generate_curve_coefs(y0,y1,y2,y3,type);
  double current;
  double currentx, currenty , x , y;
  x = x0; y = y0;
  for (current = 0; current < 1 + step; current += step){
    double current2 = current*current; double current3 = current*current2;
    currentx = coef1->m[0][0]*current3 + coef1->m[1][0]*current2 + coef1->m[2][0]*current + coef1->m[3][0];
    currenty = coef2->m[0][0]*current3 + coef2->m[1][0]*current2 + coef2->m[2][0]*current + coef2->m[3][0];
    printf("%lf\n" , current3);  
    add_edge(points , x , y , 0 , currentx , currenty , 0);
    x = currentx;
    y = currenty;
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

