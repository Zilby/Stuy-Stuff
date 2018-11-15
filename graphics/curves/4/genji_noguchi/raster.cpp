#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <stdio.h>
#include "raster.h"

using namespace std;

// Constructor definitions
Raster::Raster() {
	Raster::init(DEFAULT_WIDTH,DEFAULT_HEIGHT);
}

Raster::Raster(int width, int height) {
	Raster::init(width, height);
}

void Raster::init(int width, int height) {
	this->width = width;
	this->height = height;
	display = (Pixel *)malloc(width*height*sizeof(Pixel));
	clear();
}


void Raster::clear() {
	int i;

	for (i=0; i<(width*height); i++) {
		display[i].r=0;
		display[i].g=0;
		display[i].b=0;
	}
}
void Raster::plot(int x, int y, Pixel p) {
	if(inRange(x, y)) {
		y = height - y;
		display[y*width + x].r = p.r;
		display[y*width + x].g = p.g;
		display[y*width + x].b = p.b;
	}
}
void Raster::plot(int x, int y) {
	Pixel p;

	p.r = 255;
	p.g = 255;
	p.b = 255;
	plot(x, y, p);
}
Pixel Raster::get(int x, int y) {
	if (inRange(x,y)) {
		return display[y*width + x];
	}
}
bool Raster::inRange(int x, int y) {
	return (x<width && y<height) && (x > 0 && y > 0);
}


void Raster::exportPPM() {
	ofstream fs;
	fs.open("out.ppm");
	
	// file header
	fs << "P3" << endl;
	fs << width << " " << height << endl;
	fs << "255" << endl;

	int i;
	Pixel tmp;
	for (i=0; i<(width*height); i++) {
		tmp = display[i];
		fs << to_string(tmp.r) << " ";
		fs << to_string(tmp.g) << " ";
		fs << to_string(tmp.b) << " ";
	}
	fs.close();
}





/* Bresenham's Line Drawing Algorithm */
void Raster::drawLine(int x1, int y1, int x2, int y2) {
	double m;
	double tmp1, tmp2, tmp3, tmp4;

	
	// make sure that for the calls to the helper functions, x2>=x1.
	if (x1 > x2) {
		drawLine(x2, y2, x1, y1);
		return;
	}


	// Account for the divide by zero error
	if (x1 == x2) {
		if (y2==y1) {
			return;
		} else if (y2>y1) {
			drawLine_o2(x1, y1, x2, y2);
		} else {
			drawLine_o3(x1, y1, x2, y2);
		}
	}

	// Calculate slope with no risk of divide by zero
	m = ((double)y2 - (double)y1) / ((double)x2 - (double)x1);
	//cout << "m = " << to_string(y2-y1) << "/" << to_string(x2-x1) << " = " << to_string(m) << endl;	
	
	// Split the line-drawing into octants.
	if ( 0 <= m && m <= 1 ) {
		//cout << "Drawing line in quadrant 1." << endl;
		drawLine_o1(x1, y1, x2, y2);
	} else if ( 1 < m ) {
		//cout << "Drawing line in quadrant 2." << endl;
		drawLine_o2(x1, y1, x2, y2);
	} else if ( m < -1 ) {
		//cout << "Drawing line in quadrant 3." << endl;
		drawLine_o3(x1, y1, x2, y2);
	} else {   // -1 < m && m <= 0
		//cout << "Drawing line in quadrant 4." << endl;
		drawLine_o4(x1, y1, x2, y2);
	}
}


void Raster::drawLine_o1(int x1, int y1, int x2, int y2) {
	int A, B, d;
	int x, y;

	x = x1;
	y = y1;
	A = 2 * (y2 - y1);
	B = -2 * (x2 - x1);
	d = A + B/2;

	while (x <= x2) {
		plot(x, y);
		if (d>0) {
			y++;
			d+=B;
		}
		x++;
		d+=A;
	}	
}
void Raster::drawLine_o2(int x1, int y1, int x2, int y2) {
	int A, B, d;
	int x, y;

	x = x1;
	y = y1;
	A = 2 * (y2 - y1);
	B = -2 * (x2 - x1);
	d = A/2 + B;

	while (y <= y2) {
		plot(x, y);
		if (d<0) {
			x++;
			d+=A;
		}
		y++;
		d+=B;
	}	
}

void Raster::drawLine_o3(int x1, int y1, int x2, int y2) {
	int A, B, d;
	int x, y;

	x = x1;
	y = y1;
	A = 2 * (y2 - y1);
	B = -2 * (x2 - x1);
	d = A/2 - B;

	while (y >= y2) {
		plot(x, y);
		if (d>0) {
			x++;
			d+=A;
		}
		y--;
		d-=B;
	}	
}
void Raster::drawLine_o4(int x1, int y1, int x2, int y2) {
	int A, B, d;
	int x, y;

	x = x1;
	y = y1;
	A = 2 * (y2 - y1);
	B = -2 * (x2 - x1);
	d = A - B/2;

	while (x <= x2) {
		plot(x, y);
		if (d<0) {
			y--;
			d-=B;
		}
		x++;
		d+=A;
	}	
}

