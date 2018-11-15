#ifndef MATRIX_H
#define MATRIX_H

#include <string>
#include <vector>
#include "vect4.h"


using std::vector;
using std::string;

/* 
 * A class for a 4xN matrix. 
 * Includes a full matrix function library.
 */
class Mat4 {
	private:
	
	public:
		Mat4();

		vector<Vect4> data;

		bool set(int r, int c, double value);
		int insert(Vect4 v);
		int insert(double x, double y, double z, double w);
	
		double get(int r, int c);

		int size();

		/* Special Matrices (Square) */
		static Mat4 zeros();
		static Mat4 ones();
		static Mat4 identity();

		/* Transformation matrices */
		static Mat4 transMatrix(double dx, double dy, double dz);
		static Mat4 scaleMatrix(double a, double b, double c);
		static Mat4 rotXMatrix(double theta);
		static Mat4 rotYMatrix(double theta);
		static Mat4 rotZMatrix(double theta);

		/* Transformation Operations. Returns false if failed, true if success.*/
		bool trans(double dx, double dy, double dz);
		bool scale(double a, double b, double c);
		bool rotateX(double theta);
		bool rotateY(double theta);
		bool rotateZ(double theta);

		/* Basic Matrix Operations */
		void apply(Mat4 m); // Performs the matrix operation mat = m * mat;
		static Mat4 mult(Mat4 a, Mat4 b);

		bool isSquare();
		static bool isSquare(Mat4 m);

		/* Math */
		static double toRadians(double deg);
		static double toDegrees(double rad);
	
		void print();
		string toString();
};

#endif
