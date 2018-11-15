#ifndef MATRIX_H
#define MATRIX_H

struct matrix {
  double **m;
  int rows, cols;
  int lastcol;
} matrix;

//Basic matrix manipulation routines
struct matrix *new_matrix(int rows, int cols);
void free_matrix(struct matrix *m);
void grow_matrix(struct matrix *m, int newcols);
void copy_matrix(struct matrix *a, struct matrix *b);
void print_matrix(struct matrix *m);
void print_trans_matrix(struct matrix *m);
struct matrix *scalar_multiplication(struct matrix *m, int scalar);
struct matrix *create_identity_matrix();
struct matrix *matrix_multiplication(struct matrix *m1, struct matrix *m2);

#endif
