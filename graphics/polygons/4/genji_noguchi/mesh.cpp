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

void Mesh::insertPolygon(int a, int b, int c) {
	polygons.push_back(a);
	polygons.push_back(b);
	polygons.push_back(c);
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

/* 3D Shapes */
void Mesh::insertRectPrism(
		double x, double y, double z,
		double w, double h, double d ) {
	
	int tbl, tbr, tfl, tfr,
		bbl, bbr, bfl, bfr;
	
	bfl = insert(x, y, z, 1);
	bfr = insert(x+w, y, z, 1);
	bbl = insert(x, y, z+d, 1);
	bbr = insert(x+w, y, z+d, 1);
	tfl = insert(x, y+h, z, 1);
	tfr = insert(x+w, y+h, z, 1);
	tbl = insert(x, y+h, z+d, 1);
	tbr = insert(x+w, y+h, z+d, 1);

	insertPolygon(tfl, bfl, bfr);
	insertPolygon(tfl, bfr, tfr);
	insertPolygon(tfr, bfr, bbr);
	insertPolygon(tfr, bbr, tbr);
	insertPolygon(tbr, bbr, bbl);
	insertPolygon(tbr, bbl, tbl);
	insertPolygon(tbl, bbl, bfl);
	insertPolygon(tbl, bfl, tfl);
	insertPolygon(tbl, tfl, tfr);
	insertPolygon(tbl, tfr, tbr);
	insertPolygon(bfl, bbl, bbr);
	insertPolygon(bfl, bbr, bfr);
	/*
	insertEdge(tfl, tfl);
	insertEdge(tfr, tfr);
	insertEdge(tbl, tbl);
	insertEdge(tbr, tbr);
	insertEdge(bfl, bfl);
	insertEdge(bfr, bfr);
	insertEdge(bbl, bbl);
	insertEdge(bbr, bbr);
	*/

	
}

void Mesh::insertSphere(
		double x, double y,
		double r ) {
	double theta, phi;
	double x1, y1, z1;
	int p, f;
	int FIRST_POINT;	// The index of the first point P0 of the sphere.
	int SPHERE_RES; 	// Level of detail of the sphere, calculated by step_size.
	int p1,p2;

	FIRST_POINT = data.size();
	SPHERE_RES = 1 / STEP_SIZE;
	cout << to_string(SPHERE_RES) << endl;
	
	// Plot the points 
	for( phi=0; phi<=1+STEP_SIZE; phi+=STEP_SIZE ){
		for( theta=0; theta<=1+STEP_SIZE; theta+=STEP_SIZE ){
			x1 = x + (r * unitSphereX(theta, phi));
			y1 = y + (r * unitSphereY(theta, phi));
			z1 =  	 (r * unitSphereZ(theta, phi));
			p = insert( x1, y1, z1, 1 );				// Add point to point matrix	
			//insertEdge( p, p );							// Plot point as line
		}
	}

	cout << "Plotting sphere pole faces" << endl;


	for( phi=0; phi<SPHERE_RES; phi++ ){

		// Edge Cases - notice that the for loop excludes these 
		// Genji pls fix this code. it's ugly.
		theta = 0;
		insertPolygon(
				FIRST_POINT,
				FIRST_POINT+1 + ((phi+1)*(SPHERE_RES+1)),
				FIRST_POINT+1 +  (phi*(SPHERE_RES+1))
				);

		theta = SPHERE_RES;
		insertPolygon(
				FIRST_POINT+SPHERE_RES,
				FIRST_POINT+theta-1   +  (phi   *(SPHERE_RES+1)),
				FIRST_POINT+theta-1   + ((phi+1)*(SPHERE_RES+1))
				);
		
		// Middle Cases
		for( theta=1; theta<SPHERE_RES-1; theta++ ){
			p1 = FIRST_POINT + (phi*(SPHERE_RES+1));
			p2 = FIRST_POINT +((phi+1)*(SPHERE_RES+1));
			insertPolygon(
				p1 + theta,
				p2 + theta,
				p1 + theta+1
				);
			
			insertPolygon(
				p1 + theta + 1,
				p2 + theta,
				p2 + theta + 1
				);
				
		}
	}
}

inline double Mesh::unitSphereX(double theta, double phi) {
	return cos(theta * M_PI);
}
inline double Mesh::unitSphereY(double theta, double phi) {
	return sin(theta * M_PI)*cos(phi * 2 * M_PI);
}
inline double Mesh::unitSphereZ(double theta, double phi) {
	return sin(theta * M_PI)*sin(phi * 2 * M_PI);
}


void Mesh::insertTorus(
		double x, double y,
		double r1, double r2) {
	double theta, phi;
	double x1, y1, z1;
	int FIRST_POINT;
	int TORUS_RES;
	int p;
	int p1, p2; // The starting points of rows

	FIRST_POINT = data.size();
	TORUS_RES = 1 / STEP_SIZE;


	// Insert points into the point matrix.
	for( phi=0; phi<=1+STEP_SIZE; phi+=STEP_SIZE ){
		for( theta=0; theta<=1+STEP_SIZE; theta+=STEP_SIZE){
			x1 = x + torusX( theta, phi, r1, r2 );
			y1 = y + torusY( theta, phi, r1, r2 );
			z1 = torusZ( theta, phi, r1, r2 );
			p = insert( x1, y1, z1, 1 );			// Add point to point matrix.
			insertEdge( p, p );						// Plot point as line
		}
	}

	// Draw Wireframe
	for (phi=0; phi<=TORUS_RES-1; phi++) {
		for (theta=0; theta<=TORUS_RES-1; theta++){
			p1 = FIRST_POINT + (phi*(TORUS_RES+1));
			p2 = FIRST_POINT +((phi+1)*(TORUS_RES+1));	
			insertPolygon(
				p1 + theta,
				p1 + theta + 1,
				p2 + theta
				);	
			insertPolygon(
				p1 + theta+1,
				p2 + theta + 1,
				p2 + theta
				);
		}
	}

}
inline double Mesh::torusX(
		double t, double p,
		double cr, double tr ){
	return cos(2*M_PI * p) * (cr*cos(2*M_PI * t) + tr);
}
inline double Mesh::torusY(
		double t, double p,
		double cr, double tr ){
	return cr*sin(2*M_PI * t);
}
inline double Mesh::torusZ(
		double t, double p,
		double cr, double tr ){
	return -sin(2*M_PI * p) * (cr*cos(2*M_PI * t) + tr);
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
