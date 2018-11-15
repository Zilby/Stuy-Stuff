#include "matrix.h"

/*============== struct matrix *new_matrix() ==============
Inputs:     int rows
            int cols
Returns:
A new matrix with a double **m of dimensions rows x cols

Once allocated, access the matrix as follows:
m->m[c][r]=something;
=========================================================*/
struct matrix *new_matrix(int rows, int cols) {
    double **tmp;
    int i;
    struct matrix *m;

    if (cols < 1) {
        cols = 1;
    }
    if (rows < 1) {
        rows = 1;
    }

    tmp = (double **) malloc(cols * sizeof(double *));
    if (tmp == NULL) {
        print_error("Memory allocation error.");
        exit(1);
    }
    for (i=0; i < cols; ++i) {
        tmp[i] = (double *) calloc(rows, sizeof(double));
        if (tmp[i] == NULL) {
            print_error("Memory allocation error.");
            exit(1);
        }
    }

    m = (struct matrix *) malloc(sizeof(struct matrix));
    if (m == NULL) {
        print_error("Memory allocation error.");
        exit(1);
    }
    m->m = tmp;
    m->rows = rows;
    m->cols = cols;
    m->lastcol = 0;

    return m;
}

/*============== void free_matrix() ==============
Inputs:     struct matrix *m
Returns:
1. free individual columns
2. free array holding column pointers
3. free actual matrix
=================================================*/
void free_matrix(struct matrix *m) {
    if (m != NULL) {
        int i;
        for (i = 0; i < m->cols; ++i) {
            free(m->m[i]);
        }
        free(m->m);
        free(m);
        m = NULL;
    }
}

/*======== void grow_matrix() ==========
Inputs:     struct matrix *m
            int newcols
Returns:
Reallocates the memory for m->m such that it now has
newcols number of columns
======================================*/
void grow_matrix(struct matrix *m, int newcols) {
    int i;
    double **ptr = realloc(m->m, newcols * sizeof(double *));
    if (ptr != NULL) {
        m->m = ptr;
    }
    else {
        print_error("Memory reallocation error.");
        exit(1);
    }
    for (i = m->cols; i < newcols; ++i) {
        m->m[i] = (double *) calloc(m->rows, sizeof(double));
        if (m->m[i] == NULL) {
            print_error("Memory allocation error.");
            exit(1);
        }
    }
    m->cols = newcols;
}

/*-------------- void copy_matrix() --------------
Inputs:     struct matrix *a
            struct matrix *b
Returns:
Copy matrix a to matrix b
*/
void copy_matrix(struct matrix *a, struct matrix *b) {
    int c, r;
    for (c = 0; c < a->cols; ++c) {
        for (r = 0; r < a->rows; ++r) {
            b->m[c][r] = a->m[c][r];
        }
    }
}

/*============== void print_matrix() ==============
Inputs:     struct matrix *m
Returns:
Print the matrix
=================================================*/
void print_matrix(struct matrix *m) {
    double **pts = m->m;
    int i;
    for (i = 0; i <= m->lastcol; ++i) {
        printf("(%.3lf,%.3lf,%.3lf)", pts[i][0], pts[i][1], pts[i][2]);
    }
    printf("\n");
}

// vim: ts=4:et:sts:sw=4:sr
