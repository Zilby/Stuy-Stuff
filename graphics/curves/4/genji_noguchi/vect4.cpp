#include <iostream>
#include "vect4.h"

/*
 * Point Definitions
 */
Vect4::Vect4() {
	init(0,0,0,0);
}
Vect4::Vect4(double x, double y, double z, double w) {
	init(x, y, z, w);	
}

void Vect4::init(double x, double y, double z, double w) {
	this->x = x;
	this->y = y;
	this->z = z;
	this->w = w;
}

double Vect4::get(int i) {
	switch( i ) {
		case 0:
			return x;
		case 1:
			return y;
		case 2:
			return z;
		case 3:
			return w;
		default:
			return NULL;
	}
}

void Vect4::set(int i, double d) {
	switch( i ) {
		case 0:
			x = d;
		case 1:
			y = d;
		case 2:
			z = d;
		case 3:
			w = d;
	}
}	
