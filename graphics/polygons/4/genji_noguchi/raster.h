#ifndef RASTER_H
#define RASTER_H

#include <vector>
#include "mesh.h"

#define DEFAULT_WIDTH 700
#define DEFAULT_HEIGHT 700

struct Pixel {
	unsigned char r, g, b;
};

class Raster {

	public:
		int width, height;
		Pixel *display;	
		Raster();
		Raster(int width, int height);

		void plot(int x, int y);
		void plot(int x, int y, Pixel);	
		Pixel get(int x, int y);

		void clear();
		void drawLine(int x1, int y1, int x2, int y2);

		void exportPPM();

		void print();

	private:
		void init(int width, int height);

		bool inRange(int x, int y);
		/*
		 * Plot the line on the raster.
		 *
		 * Givens: (x, y) coordinates of start and end points.
		 * Assumptions: x2 >= x1
		 *
		 */
		void drawLine_o1(int x1, int y1, int x2, int y2);// 0 <= m < 1
		void drawLine_o2(int x1, int y1, int x2, int y2);// 1 <= m < und
		void drawLine_o3(int x1, int y1, int x2, int y2);// -und < m <= -1
		void drawLine_o4(int x1, int y1, int x2, int y2);// -1 < m <= 0

};

#endif
