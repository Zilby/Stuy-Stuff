#ifndef PARSER_H
#define PARSER_H

#include "matrix.h"
#include "ml6.h"

#define STEP 0.001

void parse_file ( char * filename, 
		  struct matrix * transform, 
		  struct matrix * pm,
		  screen s);

#endif
