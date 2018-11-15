#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include "mesh.h"

using namespace std;

Mesh::Mesh() {
	transformation = identity();
}


void Mesh::insertEdge(int a, int b) {
	edges.push_back(a);
	edges.push_back(b);
}

/* Circle Functions */
void Mesh::insertCircle(double cx, double cy, double r) {
	double t;
	double  x,  y,
		   x0, y0;

	x0 = cx + r;
	y0 = cy;
	for( t=0; t<=1+STEP_SIZE; t+=STEP_SIZE ) {
		x = cx + r*unitCircleX(t);
		y = cy + r*unitCircleY(t);
		insertEdge(insert(x0,y0,0,1), insert(x,y,0,1));
		x0 = x;
		y0 = y;
	}
}
inline double Mesh::unitCircleX(double t) {
	return cos(t*2*M_PI);
}
inline double Mesh::unitCircleY(double t) {
	return sin(t*2*M_PI);
}

/* Bezier Curve Functions */
void Mesh::insertBezier( double x0, double y0,
						 double x1, double y1,
                         double x2, double y2,
                         double x3, double y3) {
	double x, y, Px, Py;	
	Mat4 input, bezier, coef;
	Vect4 v1(x0, x1, x2, x3);
	Vect4 v2(y0, y1, y2, y3);
	input.insert(v1);
	input.insert(v2);

	bezier = bezierMatrix();

	Px = x0;
	Py = y0;
	double t;
	for( t=0; t<1.0+STEP_SIZE; t+=STEP_SIZE ){
		coef = mult(bezier, input);
		x = calcCubic(
				coef.get(0,0),
				coef.get(1,0),
				coef.get(2,0),
				coef.get(3,0),
				t );
		y = calcCubic(
				coef.get(0,1),
				coef.get(1,1),
				coef.get(2,1),
				coef.get(3,1),
				t );
		insertEdge(insert(Px, Py, 0, 1), insert(x, y, 0, 1));
		Px = x;
		Py = y;
	}
}

inline double Mesh::calcCubic(double a, double b, double c, double d, double t) {
	return (a*t*t*t) + (b*t*t) + (c*t) + d;
}

Mat4 Mesh::bezierMatrix() {	
	Mat4 tmp;
	Vect4 v1(-1, 3,-3, 1 ),
		  v2( 3,-6, 3, 0 ),
		  v3(-3, 3, 0, 0 ),
		  v4( 1, 0, 0, 0 );

	tmp.insert(v1);
	tmp.insert(v2);
	tmp.insert(v3);
	tmp.insert(v4);

	return tmp;

}


/* Hermite Creation Functions */
void Mesh::insertHermite(double x0, double y0,
	                     double x1, double y1,
	                     double x2, double y2,
                         double x3, double y3){
	double x, y, Px, Py;
	double rx0, ry0, rx2, ry2;

	rx0 = x1 - x0;
	ry0 = y1 - y0;
	rx2 = x3 - x2;
	ry2 = y3 - y2;

	Mat4 input, hermite, coef;
	Vect4 v1(x0, x2, rx0, rx2);
	Vect4 v2(y0, y2, ry0, ry2);
	input.insert(v1);
	input.insert(v2);

	hermite = hermiteMatrix();

	Px = x0;
	Py = y0;
	double t;
	for( t=0; t<1.0+STEP_SIZE; t+=STEP_SIZE ){
		coef = mult(hermite, input);
		x = calcCubic(
				coef.get(0,0),
				coef.get(1,0),
				coef.get(2,0),
				coef.get(3,0),
				t );
		y = calcCubic(
				coef.get(0,1),
				coef.get(1,1),
				coef.get(2,1),
				coef.get(3,1),
				t );
		insertEdge(insert(Px, Py, 0, 1), insert(x, y, 0, 1));
		Px = x;
		Py = y;
	}
}

Mat4 Mesh::hermiteMatrix() {	
	Mat4 tmp;
	Vect4 v1( 2,-3, 0, 1 ),
		  v2(-2, 3, 0, 0 ),
		  v3( 1,-2, 1, 0 ),
		  v4( 1,-1, 0, 0 );

	tmp.insert(v1);
	tmp.insert(v2);
	tmp.insert(v3);
	tmp.insert(v4);

	return tmp;
}





void Mesh::applyTransformation() {
	apply(transformation);
}
Mat4 Mesh::transformPoints() {
	return Mat4::mult(transformation, *this);
}

// Transformation Function Overrides
bool Mesh::trans(double dx, double dy, double dz) {
	transformation.apply(transMatrix(dx,dy,dz));
	return true;
}
bool Mesh::scale(double a, double b, double c) {
	transformation.apply(scaleMatrix(a,b,c));
	return true;
}
bool Mesh::rotateX(double theta) {
	transformation.apply(rotXMatrix(theta));
	return true;
}
bool Mesh::rotateY(double theta) {
	transformation.apply(rotYMatrix(theta));
	return true;
}
bool Mesh::rotateZ(double theta) {
	transformation.apply(rotZMatrix(theta));
	return true;
}

void Mesh::resetPosition() {
	transformation = identity();
}
