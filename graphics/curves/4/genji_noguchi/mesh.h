#ifndef MESH_H
#define MESH_H

#include <vector>
#include "vect4.h"
#include "matrix.h"
#include "raster.h"
#define MIN_MAT_SIZE 64
#define VECTOR_COMPS 4
#define STEP_SIZE 0.01

using std::vector;

class Mesh : public Mat4 {
	
	public:
		Mesh();
				
		vector<int> edges;
		Mat4 transformation;
		
		////////// Edge Creation //////////////////////////
		/* 
		 * Insert 2 edges into the edge matrix.
		 * Ints represent the position of the points in the point matrix.
		 */
		void insertEdge(int, int);

		////////// Curve Creation /////////////////////////
		
		/* 
		 * Circle Creation Functions
		 */
		void insertCircle(double x, double y, double r);
		inline double unitCircleX(double t);
		inline double unitCircleY(double t);

		/*
		 * Hermite Creation Functions
		 */
		void insertHermite(double x0, double y0,
						   double rx0, double ry0,
						   double x1, double y1,
						   double rx1, double ry1);
		static Mat4 hermiteMatrix();

		/*
		 * Bezier Creation Functions
		 */
		void insertBezier(double x1, double y1,
						  double x2, double y2,
						  double x3, double y3,
						  double x4, double y4);	
		inline double calcCubic(double a, double b, double c, double d, double t);
		static Mat4 bezierMatrix();
		

		/* Apply the transformation matrix */
		void applyTransformation();

		/* Return a copy of the translated matrix */
		Mat4 transformPoints();

		/* Transformation function overrides.
		 *
		 * This is necessary because meshes must behave differently than standar Mat4 matrices.
		 	* Mat4 matrix operations work directly on the original points themselves.
			* Mesh matrix operations will alter the transformation matrix, which will be applied right before drawing in order to maintain the integrity of the original positions of the points of the mesh.
		*/
		bool trans(double dx, double dy, double dz);
		bool scale(double a, double b, double c);
		bool rotateX(double theta);
		bool rotateY(double theta);
		bool rotateZ(double theta);

		/* Resets the transformation matrix back to the unit matrix. */
		void resetPosition();

	private:

};

#endif
