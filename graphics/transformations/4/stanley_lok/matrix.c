#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "matrix.h"

/*-------------- struct matrix *new_matrix() --------------
Inputs:  int rows
         int cols 
Returns: 

Once allocated, access the matrix as follows:
m->m[r][c]=something;
if (m->lastcol)... 
*/
struct matrix *new_matrix(int rows, int cols) {
  double **tmp;
  int i;
  struct matrix *m;

  tmp = (double **)malloc(rows * sizeof(double *));
  for (i=0;i<rows;i++) {
      tmp[i]=(double *)malloc(cols * sizeof(double));
    }

  m=(struct matrix *)malloc(sizeof(struct matrix));
  m->m=tmp;
  m->rows = rows;
  m->cols = cols;
  m->lastcol = 0;

  return m;
}


/*-------------- void free_matrix() --------------
Inputs:  struct matrix *m 
Returns: 

1. free individual rows
2. free array holding row pointers
3. free actual matrix
*/
void free_matrix(struct matrix *m) {

  int i;
  for (i=0;i<m->rows;i++) {
      free(m->m[i]);
    }
  free(m->m);
  free(m);
}


/*======== void grow_matrix() ==========
Inputs:  struct matrix *m
         int newcols 
Returns: 

Reallocates the memory for m->m such that it now has
newcols number of collumns
====================*/
void grow_matrix(struct matrix *m, int newcols) {
  int i;
  for (i=0;i<m->rows;i++) {
      m->m[i] = realloc(m->m[i],newcols*sizeof(double));
    }
  m->cols = newcols;
}

/*-------------- void copy_matrix() --------------
Inputs:  struct matrix *a
         struct matrix *b 
Returns: 

copy matrix a to matrix b
*/
void copy_matrix(struct matrix *a, struct matrix *b) {
  int r, c;

  for (r=0; r < a->rows; r++) 
    for (c=0; c < a->cols; c++)  
      b->m[r][c] = a->m[r][c];  
}




/*-------------- void print_matrix() --------------
Inputs:  struct matrix *m 
Returns: 

print the matrix
*/
void print_matrix(struct matrix *m) {
  int col = 0;
  while(col < m->lastcol){
    printf("%f,%f,%f\n", m->m[0][col], m->m[1][col], m->m[2][col]);
    col++;
  }
  printf("\n");
}

void print_trans_matrix(struct matrix *m){
  int i,j;
  for(i = 0; i < m->rows; i++){
    printf("| ");
    for(j = 0; j < m->cols; j++){
      printf("%f ", m->m[i][j]);
    }
    printf("|\n");
  }
  printf("\n");
}
  

/*Scalar Multiplication

  Inputs: a matrix and a scalar (constant)

  Returns: a scaled matrix 
*/

struct matrix * scalar_multiplication(struct matrix *m, int scalar){

  int i,j;
  for(i = 0; i < m->rows; i++){
    for(j = 0; j < m->cols; j++){

      m->m[i][j] = m->m[i][j] * scalar;
    }
  }

  return m;
}

/* Identity Matrix

   | 1 0 0 0 |
   | 0 1 0 0 |
   | 0 0 1 0 |
   | 0 0 0 1 |
*/
struct matrix * create_identity_matrix(struct matrix * m){
  int i,j;
  
  for( i = 0; i < m->rows; i++){
    for( j = 0; j < m->cols; j++){
      if( i == j ){
	m->m[i][j] = 1;
      }
    }
  }
  return m;
}

/* Matrix Multiplication
   
   Takes two matrices and multiply them

   The result should be a 4 by 4 matrix but I made it so it should work for any size matrices
   
*/  

struct matrix * matrix_multiplication(struct matrix * m1, struct matrix * m2){
  //Check if you can multiply the matrices first
  if(m1->cols != m2->rows){
    printf("Matrix sizes are incorrect, cannnot multiply them\n");
    return NULL;
  }
  //Creates a new matrix m1 rows and m2 cols

  struct matrix * product = new_matrix(m1->rows,m2->cols);
  
  int i, j, k;

  for(i = 0; i < product->rows; i++){
    for(j = 0; j < product->cols; j++){
      
      int sum = 0;
      for(k = 0; k < product->rows; k++){
	sum += m1->m[i][k] * m2->m[k][j];
      }
      product->m[i][j] = sum;
    }
  }
  free_matrix(m1);
  free_matrix(m2);
  return product;
}

