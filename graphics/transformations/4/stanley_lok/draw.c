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
  if(points->lastcol >= points->cols){
    grow_matrix(points, points->cols * 2); //should double the matrix
  }
  printf("LastCol:%d\n", points->lastcol);
  printf("MaxCol:%d\n", points->cols);
  int lastcol = points->lastcol;
  
  points->m[0][lastcol] = x;
  points->m[1][lastcol] = y;
  points->m[2][lastcol] = z;
  points->m[3][lastcol] = 1;
  
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
  for(current_col = 0; current_col < points->lastcol; current_col += 2){
    draw_line(points->m[0][current_col],
	      points->m[1][current_col],
	      points->m[0][current_col + 1],
	      points->m[1][current_col + 1],
	      s,
	      c);
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
  //Switch Coordinates if necessary

  if(x0 > x1){
    int tmp = x0;
    x0 = x1;
    x1 = tmp;
    tmp = y0;
    y0 = y1;
    y1 = tmp;
  }

  //Initial computations
  int deltay = 2 * (y1 - y0);
  int deltax = -2 * (x1 - x0);
  int x = x0;
  int y = y0;
  
  //Octant 1 and 5
  if(deltay >= 0 && deltay <= (deltax * -1)){ //checks if the slope is between 0 and 1
      int difference = deltay + (deltax/2);
      while(x <= x1){
	plot(s,c,x,y);
	if( difference > 0 ){
	  y++;
	  difference += deltax;
	}
	else{
	  x++;
	  difference += deltay;
	}
      }
  }
  
  //Octant 2 and 6
  else if(deltay >= (deltax * -1)){
    
    int difference = deltay / 2 + deltax;
    while(y <= y1){
      plot(s,c,x,y);
      if(difference < 0){
	x++;
	difference += deltay;
      }
      else{
	y++;
	difference += deltax;
      }
    }
  }

  //Octant 3 and 7
  else if(deltay < 0 && deltay <= deltax){
    int difference = deltay / 2 - deltax;
    while(y >= y1){
      plot(s,c,x,y);
      if(difference > 0){
	x += 1;
	difference += deltay;
      }
      else{
	y -= 1;
	difference -= deltax;
      }
    }
  }

  //Octant 3 and 8
  else if( deltay < 0 && deltay >= deltax){
    // printf("test");
    int difference = deltay - (deltax / 2);
    while(x <= x1){
      plot(s,c,x,y);
      if(difference < 0){
	y -= 1;
	difference -= deltax;
      }
      else{
	x += 1;
	difference += deltay;
      }
    }
  }

  else{
    printf("test\n");
  }
    
  
}
    
/* Translation 
   Takes a transformation matrix and 3 values

   Returns a transformation matrix with the translation values applied
*/

struct matrix * translate(int dx, int dy, int dz){
  struct matrix * trans;
  
  trans = new_matrix(4,4);

  int i,j;

  for(i = 0; i < trans->rows; i++){
    for(j = 0; j < trans->cols; j++){

      if(i == j){
	trans->m[i][j] = 1;
      }
      else if(j == 3){
	if(i == 0){
	  trans->m[i][j] = dx;
	}
	else if(i == 1){
	  trans->m[i][j] = dy;
	}
	else{
	  trans->m[i][j] = dz;
	}
      }
    }
  }
  print_trans_matrix(trans); //debug
  return trans;
}


struct matrix * scale(int x, int y, int z){
  struct matrix *trans;
  
  trans = new_matrix(4,4);
  trans = create_identity_matrix(trans);
  
  int i,j;

  for(i = 0; i < trans->rows; i++){

    for(j = 0; j< trans->cols; j++){

      if(i == j && j == 0){
	trans->m[i][j] = x;
      }
      else if(i == j && j == 1){
	trans->m[i][j] = y;
      }
      else if(i == j && j == 2){
	trans->m[i][j] = z;
      }
    }
  }
  
  print_trans_matrix(trans);

  return trans;
}

double degrees_to_radians(double degrees){
  double radians = degrees*M_PI / 180;
  return radians;
}

struct matrix * rotate_x(double theta){
  struct matrix *trans;
  
  trans = new_matrix(4,4);
  trans = create_identity_matrix(trans);
  
  trans->m[1][1] = cos(degrees_to_radians(theta));
  trans->m[1][2] = -1 * sin(degrees_to_radians(theta));
  trans->m[2][1] = sin(degrees_to_radians(theta));
  trans->m[2][2] = cos(degrees_to_radians(theta));
  
  print_trans_matrix(trans);
  return trans;
}

struct matrix * rotate_y(double theta){
  struct matrix *trans;
  
  trans = new_matrix(4,4);
  trans = create_identity_matrix(trans);
  
  trans->m[0][0] = cos(degrees_to_radians(theta));
  trans->m[0][2] = -1 * sin(degrees_to_radians(theta));
  trans->m[2][0] = sin(degrees_to_radians(theta));
  trans->m[2][2] = cos(degrees_to_radians(theta));
  
  print_trans_matrix(trans);
  return trans;
}

struct matrix * rotate_z(double theta){
  struct matrix *trans;
  
  trans = new_matrix(4,4);
  trans = create_identity_matrix(trans);
  
  trans->m[0][0] = cos(degrees_to_radians(theta));
  trans->m[0][1] = -1 * sin(degrees_to_radians(theta));
  trans->m[1][0] = sin(degrees_to_radians(theta));
  trans->m[1][1] = cos(degrees_to_radians(theta));
  
  print_trans_matrix(trans);
  return trans;
}
