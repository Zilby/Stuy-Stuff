#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "ml6.h"
#include "display.h"
#include "draw.h"
#include "matrix.h"
#include "parser.h"


/*======== void parse_file () ==========
Inputs:   char * filename 
          struct matrix * transform, 
          struct matrix * pm,
          screen s
Returns: 

Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         l: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 i: set the transform matrix to the identity matrix - 
	 s: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 t: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 x: create an x-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 y: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 z: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 a: apply the current transformation matrix to the 
	    edge matrix
	 v: draw the lines of the edge matrix to the screen
	    display the screen
	 g: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 q: end parsing

See the file script for an example of the file format


IMPORTANT MATH NOTE:
the trig functions int math.h use radian mesure, but us normal
humans use degrees, so the file will contain degrees for rotations,
be sure to conver those degrees to radians (M_PI is the constant
for PI)

jdyrlandweaver
====================*/
void parse_file ( char * filename, 
                  struct matrix * transform, 
                  struct matrix * pm,
                  screen s) {
  FILE *file = fopen(filename , "r");
  char first;
  double arguments [6];
  while (fscanf(file,"%c",&first) != EOF){
    if (first=='l'){
      fscanf(file,"%lf%lf%lf%lf%lf%lf",&arguments[1],&arguments[2],&arguments[3],
	     &arguments[4],&arguments[5],&arguments[6]);
      add_edge(pm , arguments[1],arguments[2],arguments[3],
		arguments[4],arguments[5],arguments[6]);
    }
    if (first=='i'){
      ident(transform);
    }
    if (first=='s'){ 
      fscanf(file,"%lf%lf%lf",&arguments[1],&arguments[2],&arguments[3]);
      struct matrix *scale = make_scale(arguments[1],arguments[2],arguments[3]);
      matrix_mult(scale , transform);
    }
    if (first=='t'){ 
      fscanf(file,"%lf%lf%lf",&arguments[1],&arguments[2],&arguments[3]);
      struct matrix *trans = make_translate(arguments[1],arguments[2],arguments[3]);
      matrix_mult(trans , transform);
    }
    if (first=='x'){ 
      fscanf(file,"%lf",&arguments[1]);
      struct matrix *x = make_rotX(arguments[1]);
      matrix_mult(x , transform);
    }
    if (first=='y'){ 
      fscanf(file,"%lf",&arguments[1]);
      struct matrix *y = make_rotY(arguments[1]);
      matrix_mult(y , transform);
    }
    if (first=='z'){ 
      fscanf(file,"%lf",&arguments[1]);
      struct matrix *z = make_rotZ(arguments[1]);
      matrix_mult(z , transform);
    }
    if (first=='a'){ 
      matrix_mult(transform , pm);
    }
    if (first=='v'){
      color c; c.red = 0; c.blue = 0; c.green = 255;
      draw_lines(pm,s,c);
    }
    if (first=='g'){ 
      display(s);
      char *line;
      fscanf(file,"%s\n",line);
      printf("%s\n" , line);
      save_extension(s , line);
    }
    if (first=='q'){ 
      return;
    }
  }
}

  
