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
    double x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4;
    double cx , cy , r , r2;
    double height , width , depth;
    c = line[0];
    double step = 0.01;

    switch (c) {
    case 'w':
      pm = new_matrix(4 , 4);
      break;
    case 'p':
      fgets(line, 255, f);
      sscanf(line, "%lf %lf %lf %lf %lf %lf", &x, &y, &z, &width, &height, &depth);
      //add_edge(pm, x, y, z, x1, y1, z1);
      add_edge(pm , x , y , z , x , y , z);
      add_edge(pm , x+width , y , z , x+width , y , z);
      add_edge(pm , x , y+height , z , x , y+height , z);
      add_edge(pm , x , y , z+depth , x , y , z+depth);
      add_edge(pm , x+width , y+height , z , x+width , y+height , z);
      add_edge(pm , x+width , y , z+depth , x+width , y , z+depth);
      add_edge(pm , x , y+height , z+depth , x , y+height , z+depth);
      add_edge(pm , x+width , y+height , z+depth , x+width , y+height , z+depth);
      break;
    case 'm':
      fgets(line , 255 , f);
      sscanf(line , "%lf %lf %lf" , &cx , &cy , &r);
      add_sphere(pm , cx , cy , r , step);
      break;
    case 'd':
      fgets(line , 255 , f);
      sscanf(line , "%lf %lf %lf %lf" , &cx , &cy , &r , &r2);
      add_torus(pm , cx , cy , r , r2 , step);   
      break;
    case 'c':
      fgets(line , 255 , f);
      sscanf(line , "%lf %lf %lf" , &cx , &cy , &r);
      add_circle(pm, cx , cy , r , step);
      break;
    case 'h':
      fgets(line , 255 , f);
      sscanf(line , "%lf %lf %lf %lf %lf %lf %lf %lf" , &x , &y , &x1 , &y1,
	     &x2 , &y2 , &x3 , &y3);
      add_curve(pm, x , y , x1 , y1 , x2 , y2 , x3 , y3 , step , 0); 
      break;
    case 'b':
      fgets(line , 255 , f);
      sscanf(line , "%lf %lf %lf %lf %lf %lf %lf %lf" , &x , &y , &x1 , &y1,
	     &x2 , &y2 , &x3 , &y3);
      add_curve(pm, x , y , x1 , y1 , x2 , y2 , x3 , y3 , step , 1); 
      break;
    case 'l':
      //      printf("LINE!\n");
      fgets(line, 255, f);
      //      printf("\t%s", line);
      //line[strlen(line)-1]='\0';
      sscanf(line, "%lf %lf %lf %lf %lf %lf", &x, &y, &z, &x1, &y1, &z1);
      add_edge(pm, x, y, z, x1, y1, z1);
      // printf( "%lf %lf %lf %lf %lf %lf\n", x, y, z, x1, y1, z1);
      break;
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

  
