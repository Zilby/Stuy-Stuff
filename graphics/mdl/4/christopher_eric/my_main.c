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
  double xval, yval, zval;
  struct matrix *transform;
  struct matrix *tmp;
  struct stack *s;
  screen t;
  color g;
  step = 20;
  
  s = new_stack();
  tmp = new_matrix(4, 1000);
  clear_screen( t );

  for (i=0;i<lastop;i++) {  
    switch (op[i].opcode) {
    case 'push':
      push(s);
      break;
    case 'pop':
      pop(s);
      break;
    case 'move':
      print_matrix((s->data[s->top]));
      /*
	for (int i=0;i<4;i++){
	(s->data[s->top])->m[i][3] += op[i].move.d[i];
	}
	
	//multiply here
	*/
      transform=new_matrix(4,4);
      ident(transform);
      transform=make_translate(op[i].op.move.d[0],
			       op[i].op.move.d[1],
			       op[i].op.move.d[2]);
      matrix_mult(transform,s->data[s->top]);
      break;
    case 'scale':
      /*
	for (int i=0;i<4;i++){
	(s->data[s->top])->m[i][i] *= op[i].scale.d[i];
	}
	
	//multiply here
	*/
      transform=new_matrix(4,4);
      ident(transform);
      transform=make_scale(op[i].op.scale.d[0],
			   op[i].op.scale.d[1],
			   op[i].op.scale.d[2]);
      matrix_mult(transform,s->data[s->top]);
      break;
    case 'rotate':
      transform=new_matrix(4,4);
      ident(transform);
      if (op[i].op.rotate.axis == 0)
	transform=make_rotX(op[i].op.rotate.degrees);
      else if (op[i].op.rotate.axis == 1)
	transform=make_rotY(op[i].op.rotate.degrees);
      else
	transform=make_rotZ(op[i].op.rotate.degrees);
      matrix_mult(transform,s->data[s->top]); 
      break;
    case 'box':
      add_box(tmp , op[i].op.box.d0[0],
	      op[i].op.box.d0[1] ,
	      op[i].op.box.d0[2] ,
	      op[i].op.box.d1[0] ,
	      op[i].op.box.d1[1] ,
	      op[i].op.box.d1[2] );
      matrix_mult(s->data[s->top],tmp);
      draw_lines(tmp,t,g);
      break;
    case 'sphere':
      add_sphere(tmp, step,
		 op[i].op.sphere.d[0],
		 op[i].op.sphere.d[1],
		 op[i].op.sphere.d[2],
		 op[i].op.sphere.r);
      matrix_mult(s->data[s->top],tmp);
      draw_lines(tmp,t,g);
      break;
    case 'torus':
      add_torus(tmp, step,
		op[i].op.torus.d[0],
		op[i].op.torus.d[1],
		op[i].op.torus.d[2],
		op[i].op.torus.r0,
		op[i].op.torus.r1);
      matrix_mult(s->data[s->top],tmp);
      draw_lines(tmp,t,g);
      break;
    case 'line':
      add_point(tmp , op[lastop].op.line.p0[0],
		op[lastop].op.line.p0[1],
		op[lastop].op.line.p0[2]);
      add_point(tmp , op[lastop].op.line.p1[0],
		op[lastop].op.line.p1[1],
		op[lastop].op.line.p1[2]);
      matrix_mult(s->data[s->top],tmp);
      draw_lines(tmp,t,g);
      break;
    case 'save':
      save_extension(s , "ok.ppm");
      break;
    case 'display':
      display(s);
      break;
    }
  }
}
