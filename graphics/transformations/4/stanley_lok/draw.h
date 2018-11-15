#ifndef DRAW_H
#define DRAW_H

#include <math.h>
#include "matrix.h"

void draw_line(int x0, int y0, int x1, int y1, screen s, color c);
void add_point( struct matrix * points, int x, int y, int z);
void add_edge( struct matrix * points, 
	       int x0, int y0, int z0, 
	       int x1, int y1, int z1);
void draw_lines( struct matrix * points, screen s, color c);
double degrees_to_radians(double degrees);
struct matrix * translate(int dx, int dy, int dz);
struct matrix * scale(int x, int y, int z);
struct matrix * rotate_x(double theta);
struct matrix * rotate_y(double theta);
struct matrix * rotate_z(double theta);

#endif
