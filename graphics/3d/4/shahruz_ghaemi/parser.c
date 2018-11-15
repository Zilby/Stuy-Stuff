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
	 c: add a circle to the edge matrix - 
	    takes 3 arguments (cx, cy, r)
	 h: add a hermite curve to the edge matrix -
	    takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
	 b: add a bezier curve to the edge matrix -
	    takes 8 arguments (x0, y0, x1, y1, x2, y2, x3, y3)
	 p: add a rectangular prism to the edge matrix
	    takes 6 arguments (x, y, z, width, height, depth)
	 m: adds a sphere (munchkin) to the edge matrix - 
	    takes 3 parameters (x, y, radius)
	 d: adds a torus (doughnut) to the edge matrix - 
	    takes 4 parameters (x, y, radius1, radius2)
	    radius1 is circle radius
	    radius2 is torus radius
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
	 w: clear the screen of all points
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

03/08/12 16:22:10
jdyrlandweaver
====================*/
void parse_file ( char * filename, 
                  struct matrix * transform, 
                  struct matrix * pm,
		  screen s) {

  FILE *f;
  char line[256];
  struct matrix * tmp;
  double angle;
  color g;

  g.red = 255;
  g.green = 0;
  g.blue = 255;
  
  clear_screen(s);

  if ( strcmp(filename, "stdin") == 0 ) 
    f = stdin;
  else
    f = fopen(filename, "r");
  
  while ( fgets(line, 255, f) != NULL ) {
    line[strlen(line)-1]='\0';
    //printf(":%s:\n",line);
    char c;
    double x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, cx, cy, r, w, h, d;
   
    c = line[0];

    switch (c) {
    case 'l':
      //      printf("LINE!\n");
      fgets(line, 255, f);
      //      printf("\t%s", line);
      //line[strlen(line)-1]='\0';
      sscanf(line, "%lf %lf %lf %lf %lf %lf", &x, &y, &z, &x1, &y1, &z1);
      add_edge(pm, x, y, z, x1, y1, z1);
      // printf( "%lf %lf %lf %lf %lf %lf\n", x, y, z, x1, y1, z1);
      break;
    case 'c':
      //printf("CIRCLE!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf %lf %lf", &cx, &cy, &r);
      add_circle(pm, cx, cy, r, STEP_SIZE);
      break; 
    case 'h':
      //printf("HERMITE!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf %lf %lf %lf %lf %lf %lf %lf", &x, &y, &x1, &y1, &x2, &y2, &x3, &y3);
      add_curve(pm, x, y, x1, y1, x2, y2, x3, y3, STEP_SIZE, HERMITE_MODE);
      break; 
    case 'b':
      //printf("BEZIER!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf %lf %lf %lf %lf %lf %lf %lf", &x, &y, &x1, &y1, &x2, &y2, &x3, &y3);
      add_curve(pm, x, y, x1, y1, x2, y2, x3, y3, STEP_SIZE, BEZIER_MODE);
      break; 
    case 'p':
      printf("BOX!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf %lf %lf %lf %lf %lf", &x, &y, &z, &w, &h, &d);
      add_rect(pm, x, y, z, w, h, d, STEP_SIZE);
      break;
    case 'm':
      //printf("SPHERE!\n");
    case 'd':
      //printf("TORUS!\n");
    case 's':
      //printf("SCALE\n");
      fgets(line, 255, f);
      //line[strlen(line)-1]='\0';      
      sscanf(line, "%lf %lf %lf", &x, &y, &z);
      tmp = make_scale(x, y, z);
      matrix_mult(tmp, transform);
      //print_matrix(transform);
      break;
    case 't':
      //printf("TRANSLATE\n");
      fgets(line, 255, f);
      //      line[strlen(line)-1]='\0';      
      sscanf(line, "%lf %lf %lf", &x, &y, &z);
      tmp = make_translate(x, y, z);
      matrix_mult(tmp, transform);
      //print_matrix(transform);
      break;
    case 'x':
      //printf("ROTATE!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf", &angle);
      angle = angle * (M_PI / 180);
      tmp = make_rotX( angle);
      matrix_mult(tmp, transform);
      break;
    case 'y':
      //printf("ROTATE!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf", &angle);
      angle = angle * (M_PI / 180);
      tmp = make_rotY( angle);
      matrix_mult(tmp, transform);
      break;
    case 'z':
      //printf("ROTATE!\n");
      fgets(line, 255, f);
      sscanf(line, "%lf", &angle);
      angle = angle * (M_PI / 180);
      tmp = make_rotZ( angle);
      matrix_mult(tmp, transform);
      break;
    case 'i':
      ident(transform);
      break;
    case 'a':
      //printf("APPLY!\n");
      //print_matrix( transform );
      //      print_matrix(pm);
      matrix_mult(transform, pm);
      break;
    case 'v':
      clear_screen(s);
      draw_lines(pm, s, g);
      display(s);
      break;
    case 'w':
      clear_screen(s);
      display(s);
      break;
    case 'g':
      fgets(line, 255, f);
      // line[strlen(line)-1] = '\0';
      clear_screen(s);
      draw_lines(pm, s, g);
      save_extension(s, line);
      break;
    case 'q':
      return;
    default:
      printf("Invalid command\n");
      break;
    }
  }

  free_matrix(tmp);
  fclose(f);
  //printf("END PARSE\n");
}

  
