#ifndef VECT4_H
#define VECT4_H

#define VECT4_SIZE 4
/* 
 * The vector/point class.
 *
 * Contains 4 data points:
 * [ double x;
 *   double y;
 *   double z;
 *   double w; ]
 *
 */

class Vect4 {
	public:
		double x, y, z, w;
		Vect4(
			double x,
			double y,
			double z,
			double w
		);
		Vect4();
		double get(int i);
		void set(int i, double v);
	private:
		void init(double x, double y, double z, double w);
};

#endif
