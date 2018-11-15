#include <iostream>
#include <cmath>
#include "matrix.h"

using namespace std;


/* 
 * Matrix Class Definitions
 */

Mat4::Mat4() {
	//transform = Mat4::identity();
}



void Mat4::print() {
	//cout << "NOTE: rows and columns switched." << endl;
	cout << toString() << endl;
}
string Mat4::toString() {
	string s;
	int r, c;

	for( r=0; r<VECT4_SIZE; r++ ) {
		for( c=0; c<size(); c++ ) { // << haha
			s += to_string(get(r, c)) + "\t";
		}
		s += "\n";
	}
	/* Swapping the rows adn columns for large sets of points */
	/*
	for( r=0; r<size(); r++ ) {
		for( c=0; c<VECT4_SIZE; c++ ) {
			s += to_string(get(r, c)) + " ";
		}
		s += "\n";
	}
	*/
	
	return s;
}

/* 
 * Math helpers
 */
double Mat4::toRadians(double deg) {
	return deg / 180 * M_PI;
}
double Mat4::toDegrees(double rad) {
	return rad / M_PI * 180;
}

/*
 * Special Matrices (Square)
 */
Mat4 Mat4::zeros() {
	Mat4 tmp;

	Vect4 v1( 0, 0, 0, 0 ),
          v2( 0, 0, 0, 0 ),
          v3( 0, 0, 0, 0 ),
          v4( 0, 0, 0, 0 );

	tmp.insert(v1);
	tmp.insert(v2);
	tmp.insert(v3);
	tmp.insert(v4);

	return tmp;
}
Mat4 Mat4::ones() {
	Mat4 tmp;
	Vect4 v1( 1, 1, 1, 1 ),
		  v2( 1, 1, 1, 1 ),
		  v3( 1, 1, 1, 1 ),
		  v4( 1, 1, 1, 1 );

	tmp.insert(v1);
	tmp.insert(v2);
	tmp.insert(v3);
	tmp.insert(v4);

	return tmp;
}
Mat4 Mat4::identity() {
	Mat4 tmp;
	Vect4 v1( 1, 0, 0, 0 ),
          v2( 0, 1, 0, 0 ),
          v3( 0, 0, 1, 0 ),
          v4( 0, 0, 0, 1 );

	tmp.insert(v1);
	tmp.insert(v2);
	tmp.insert(v3);
	tmp.insert(v4);
	
	return tmp;
}

/* 
 * Transformations
 */
bool Mat4::trans(double dx, double dy, double dz) {
	apply(transMatrix(dx,dy,dz));
	return true;
}
bool Mat4::scale(double a, double b, double c) {
	apply(scaleMatrix(a,b,c));
	return true;
}
bool Mat4::rotateX(double theta) {
	apply(rotXMatrix(theta));
	return true;
}
bool Mat4::rotateY(double theta) {
	apply(rotYMatrix(theta));
	return true;
}
bool Mat4::rotateZ(double theta) {
	apply(rotZMatrix(theta));
	return true;
}


/*
 * Helper Functions 
 * */

/* Size Function */
int Mat4::size() {
	return data.size();
}

/* Getters and setters */
double Mat4::get(int r, int c) {
	return data[c].get(r);
}
int Mat4::insert(Vect4 v) {
	data.push_back(v);
	return size() - 1;
}
int Mat4::insert(double x, double y, double z, double w) {
	Vect4 v(x, y, z, w);
	return insert(v);
}
bool Mat4::set(int r, int c, double value) {
	if( r > 3 ||
		c > size()-1) {
		return false;
	} else {
		data[c].set(r, value);
	}
}

/* isSquare */
bool Mat4::isSquare() {
	if (data.size() == 4) {
		return true;
	}
	return false;
}
bool Mat4::isSquare(Mat4 m) {
	return m.isSquare();
}

/* Matrix Multiplication */
void Mat4::apply(Mat4 m) {
	if (!m.isSquare()) {
		return;
	}

	int r, c, i;
	double dot;
	Vect4 tmp_row;
	for( c=0; c<size(); c++ ) {		// <<<<<< haha i wrote c++
		tmp_row = data[c];
		for( r=0; r<VECT4_SIZE; r++ ) {
			dot = 0;
			for( i=0; i<VECT4_SIZE; i++ ) {
				dot += m.get(r, i) * tmp_row.get(i);
			}
			set(r, c, dot);
		}
	}
}
Mat4 Mat4::mult(Mat4 a, Mat4 b) {
	Mat4 tmp;
	tmp = b;
	tmp.apply(a);
	return tmp;
}

/* Transformation helpers */
Mat4 Mat4::transMatrix( double dx, double dy, double dz) {
	Mat4 tmp;
	Vect4 v1(	1, 	0,	0,	0),
		  v2(	0,	1,	0,	0),
		  v3(	0,	0,	1,	0),
		  v4(	dx,	dy,	dz,	1 );

	tmp.insert(v1);	
	tmp.insert(v2);	
	tmp.insert(v3);	
	tmp.insert(v4);	
	
	return tmp;
}
Mat4 Mat4::scaleMatrix(double a, double b, double c) {
	Mat4 tmp;	
	Vect4 v1(	a, 	0,	0,	0),
		  v2(	0,	b,	0,	0),
		  v3(	0,	0,	c,	0),
		  v4(	0,	0,	0,	1);

	tmp.insert(v1);	
	tmp.insert(v2);	
	tmp.insert(v3);	
	tmp.insert(v4);	
	
	return tmp;
}
Mat4 Mat4::rotXMatrix(double theta) {
	Mat4 tmp;
	double t;
	
	t = Mat4::toRadians(theta);
	Vect4 v1(		 1,		  0,		  0,	0),
		  v2(		 0,  cos(t),	 sin(t),	0),
		  v3(		 0,	-sin(t),	 cos(t),	0),
		  v4(		 0,	   	  0,		  0,	1);

	tmp.insert(v1);	
	tmp.insert(v2);	
	tmp.insert(v3);	
	tmp.insert(v4);	

	tmp.print();

	return tmp;
}
Mat4 Mat4::rotYMatrix(double theta) {
	Mat4 tmp;
	double t;

	t = Mat4::toRadians(theta);
	Vect4 v1(	cos(t),		  0,    sin(t),		0),
          v2(		 0,		  1,		 0,		0),
          v3(  -sin(t),	 	  0, 	cos(t),		0),
          v4(		 0,	   	  0,		 0,		1);

	tmp.insert(v1);	
	tmp.insert(v2);	
	tmp.insert(v3);	
	tmp.insert(v4);	

	return tmp;
}
Mat4 Mat4::rotZMatrix(double theta) {
	Mat4 tmp;
	double t;

	t = Mat4::toRadians(theta);
	Vect4 v1(	cos(t),	 sin(t),		 0,		0),
		  v2(  -sin(t),	 cos(t),		 0,		0),
		  v3(		 0,		  0,		 1,		0),
		  v4(		 0,	   	  0,		 0,		1);

	tmp.insert(v1);	
	tmp.insert(v2);	
	tmp.insert(v3);	
	tmp.insert(v4);	

	return tmp;
}
