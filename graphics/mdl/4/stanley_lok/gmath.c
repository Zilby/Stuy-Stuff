#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "matrix.h"
#include "gmath.h"



/*======== double * calculate_normal() ==========
  Inputs:   double ax
            double ay
	    double az
	    double bx
	    double by
	    double bz  
  Returns: A double arry of size 3 representing the 
           cross product of <ax, ay, az> and <bx, by, bz>

  04/17/12 16:46:30
  jonalf
  ====================*/
double * calculate_normal( double ax, double ay, double az,	
			   double bx, double by, double bz ) {
  
  double *normal;
  normal = (double *)malloc(3 * sizeof(double));
  normal[0] = ay*bz - az*by;
  normal[1] = az*bx - ax*bz;
  normal[2] = ax*by - ay*bx;
  return normal;
}

/*======== double calculate_dot() ==========
  Inputs:   struct matrix *points
            int i  
  Returns: The dot product of a surface normal and
           a view vector
  
  calculates the dot product of the surface normal to
  triangle points[i], points[i+1], points[i+2] and a 
  view vector (use <0, 0, -1> to start.

  04/17/12 16:38:34
  jonalf
  ====================*/
double calculate_dot( struct matrix *points, int i ) {

  double dot = -1;
  double * normal = calculate_normal( points->m[0][i + 1] - points->m[0][i],
				      points->m[1][i + 1] - points->m[1][i],
				      points->m[2][i + 1] - points->m[2][i],
				      points->m[0][i + 2] - points->m[0][i],
				      points->m[1][i + 2] - points->m[1][i],
				      points->m[2][i + 2] - points->m[2][i]);
  double view[3];
  view[0] = 0;
  view[1] = 0;
  view[2] = 1;
  dot = normal[0] * view[0] + normal[1] * view[1] + normal[2] * view[2];
  free(normal);
  return dot; 
}
