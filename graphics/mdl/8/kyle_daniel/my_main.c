/*========== my_main.c ==========

  This is the only file you need to modify in order
  to get a working mdl project (for now).

  my_main.c will serve as the interpreter for mdl.
  When an mdl script goes through a lexer and parser,
  the resulting operations will be in the array op[].

  Your job is to go through each entry in op and perform
  the required action from the list below:

  push: push a new origin matrix onto the origin stack
  pop: remove the top matrix on the origin stack

  move/scale/rotate: create a transformation matrix
                     based on the provided values, then
		     multiply the current top of the
		     origins stack by it.

  box/sphere/torus: create a solid object based on the
                    provided values. Store that in a
		    temporary matrix, multiply it by the
		    current top of the origins stack, then
		    call draw_polygons.

  line: create a line based on the provided values. Store
        that in a temporary matrix, multiply it by the
	current top of the origins stack, then call draw_lines.

  save: call save_extension with the provided filename

  display: view the image live

  jdyrlandweaver
  =========================*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "parser.h"
#include "symtab.h"
#include "y.tab.h"

#include "misc_headers.h"
#include "matrix.h"
#include "ml6.h"
#include "display.h"
#include "draw.h"
#include "stack.h"

void my_main( int polygons ) {

  int i;
  double step;
  double xval, yval, zval,x2,y2,z2;
  struct matrix *transform;
  struct matrix *tmp;
  struct stack *s;
  screen t;
  clear_screen( t );
  color g;
  g.red = 0;
  g.green = 0;
  g.blue = 255;

  s = new_stack();
  tmp = new_matrix(4, 1000);


  for (i=0;i<lastop;i++) {
    switch (op[i].opcode) {
  		case SCALE:
  			transform=new_matrix(4,4);
  			ident(transform);
  			xval=op[i].op.scale.d[0];
  			yval=op[i].op.scale.d[1];
  			zval=op[i].op.scale.d[2];
  			transform=make_scale(xval, yval, zval);
  			//if (op[i].op.scale.p)
  			//	scalar_mult(op[i].op.scale.p->s.value,transform);
  			matrix_mult(transform,s->data[s->top]);
  			break;
  		case PUSH:
  			push(s);
  			break;
  		case POP:
  			pop(s);
  			break;
  		case MOVE:
        transform=new_matrix(4,4);
        ident(transform);
        xval=op[i].op.move.d[0];
        yval=op[i].op.move.d[1];
        zval=op[i].op.move.d[2];
        transform=make_translate(xval, yval, zval);
        //if (op[i].op.move.p)
        //    scalar_mult(op[i].op.move.p->s.value,transform);
        matrix_mult(transform,s->data[s->top]);
        break;
  		case ROTATE:
        transform=new_matrix(4,4);
        ident(transform);
        xval=op[i].op.rotate.axis; //Axis
        yval=op[i].op.rotate.degrees; //Degree
        yval=M_PI * yval / 180;
        if (xval==0) //x axis
        transform=make_rotX(yval);
        if (xval==1)// y axis
        transform=make_rotY(yval);
        if (xval==2) //z axis
        transform=make_rotZ(yval);
        //if (op[i].op.rotate.p)
        //    scalar_mult(op[i].op.move.p->s.value,transform);
        matrix_mult(transform,s->data[s->top]);
        break;
  		case LINE:
  			xval=op[lastop].op.line.p0[0];
  			yval=op[lastop].op.line.p0[1];
  			zval=op[lastop].op.line.p0[2];
        x2=op[lastop].op.line.p1[0];
        y2=op[lastop].op.line.p1[1];
        z2=op[lastop].op.line.p1[2];
  			add_edge(tmp,xval,yval,zval,x2,y2,z2);
  			matrix_mult(s->data[s->top],tmp);
  			draw_lines(tmp,t,g);
  			free_matrix(tmp);
  			tmp = new_matrix(4, 1000);
  			break;
      case BOX:
        xval=op[lastop].op.box.d0[0];
        yval=op[lastop].op.box.d0[1];
        zval=op[lastop].op.box.d0[2];
        x2=op[lastop].op.box.d1[0];
        y2=op[lastop].op.box.d1[1];
        z2=op[lastop].op.box.d1[2];
        add_box(tmp,xval,yval,zval,y2,x2,z2);
        matrix_mult(s->data[s->top],tmp);
        //print_matrix(tmp);
        draw_polygons(tmp,t,g);
        free_matrix(tmp);
        tmp = new_matrix(4, 1000);
        break;
      case SPHERE:
        xval=op[lastop].op.sphere.d[0];
        yval=op[lastop].op.sphere.d[1];
        zval=op[lastop].op.sphere.d[2];
        x2=op[lastop].op.sphere.r;
        add_sphere(tmp,xval,yval,zval,x2,1);
        matrix_mult(s->data[s->top],tmp);
        draw_polygons(tmp,t,g);
        free_matrix(tmp);
        tmp = new_matrix(4, 1000);
        break;
      case TORUS:
        xval=op[lastop].op.torus.d[0];
        yval=op[lastop].op.torus.d[1];
        zval=op[lastop].op.torus.d[2];
        x2=op[lastop].op.torus.r0;
        y2=op[lastop].op.torus.r1;
        add_torus(tmp,xval,yval,zval,x2,y2,1);
        matrix_mult(s->data[s->top],tmp);
        draw_polygons(tmp,t,g);
        free_matrix(tmp);
        tmp = new_matrix(4, 1000);
        break;
      case SAVE:
        save_extension(t,op[lastop].op.save.p->name);
        break;
      case DISPLAY:
        display(t);
        break;




	  }
  }
}
