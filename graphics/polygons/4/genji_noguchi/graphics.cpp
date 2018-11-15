#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <fstream>
#include <sstream>
#include "graphics.h"

using namespace std;

Graphics::Graphics() {
	init(500, 500);
}

Graphics::Graphics(int width, int height) {
	init(width, height);
}

void Graphics::init(int width, int height) {
	Raster raster(width, height);
	Vect4 view(0, 0, -1, 1);
	this->raster = raster;
	this->view = view;
}

int Graphics::addMesh(Mesh *m) {
	meshes.push_back(m);
	return meshes.size()-1;
}

void Graphics::writeScript() {
	ofstream fs;
	fs.open("backface.dwobj");

	int x=0, y=700;
	int vx=100, vy=100;
	int g=30;

	cout << "Writing backface.dwobj" << endl;
	while (x <= 1600)
	{
		vy -= g;
		x+=vx;
		y+=vy;
		
		if (y<100)
		{
			y = 100;
			vy = -vy;
		}

		fs << "m\n" + to_string(x) + " " + to_string(y) + " 50" << endl;
	}
	
	int i;
	for (i=0; i<10; i++) {
		fs << "d\n1000 50 "+ to_string(10-i) + " " + to_string(100 + (50*i)) << endl;
	}
	
	fs << "x\n20" << endl;
	fs << "y\n10" << endl;
	fs << "t\n-200 100 0" << endl;

	fs << "v" << endl;
	fs << "g\npic.png" << endl;
	fs.close();
}

void Graphics::exportGraph() {
	cout << "Exporting graph" << endl;
	int i,j;
	vector<Vect4> p;
	vector<int> e, f;

	raster.clear();

	for (j=0;j<meshes.size();j++) {
		/* Export edges and polygons */
		p = meshes[j]->transformPoints().data;
		e = meshes[j]->edges;
		f = meshes[j]->polygons;

		/* Edges */
		for (i=0;i<e.size();i+=2) {
			//cout << to_string(p[e[i]].y) << endl;
			//cout << to_string(p[e[i+1]].y) << endl;	
			//cout << endl;
			raster.drawLine(
					p[e[i]].x,	
					p[e[i]].y,	
					p[e[i+1]].x,	
					p[e[i+1]].y
					);
		}

		/* Polygons */	
		Vect4 normal, a, b;
		int mcost;
		for (i=0; i<f.size(); i+=3 ){

			
			/* Check the orientation of the polygon using backface culling */
			
			a.set(
				p[f[i+1]].x-p[f[i]].x,
				p[f[i+1]].y-p[f[i]].y,
				p[f[i+1]].z-p[f[i]].z,
				1);
			b.set(
				p[f[i+2]].x-p[f[i]].x,
				p[f[i+2]].y-p[f[i]].y,
				p[f[i+2]].z-p[f[i]].z,
				1);
			normal.set(
				a.y*b.z - a.z*b.y,
				a.z*b.x - a.x*b.z,
				a.x*b.y - a.y*b.x,
				1);
			

			// N • V
			mcost = 
				normal.x * view.x + 
				normal.y * view.y +
				normal.z * view.z;
			
			if (mcost <= 0 ) {
				/* Send the 3 edges to the raster */
				raster.drawLine(
						p[f[i]].x,	
						p[f[i]].y,	
						p[f[i+1]].x,	
						p[f[i+1]].y
						);
				raster.drawLine(
						p[f[i+1]].x,
						p[f[i+1]].y,
						p[f[i+2]].x,
						p[f[i+2]].y
						);
				raster.drawLine(
						p[f[i]].x,
						p[f[i]].y,
						p[f[i+2]].x,
						p[f[i+2]].y
						);
			}	
		}
	}
	

	raster.exportPPM();
}

void Graphics::display() {
	/*
	int f, w, status;

	if( f = fork() ) {
		// Parent waits
		cout << "Parent waiting" << endl;
		w = wait(&status);
		cout << "Parent done waitihg" << endl;	
	} else {
		cout << "Running imagemagick" << endl;
		execl("display", "out.ppm", NULL);
		exit(0);
	}
	*/
	execl("display", "out.ppm", NULL);
}

void Graphics::save(string filename) {	
	int f, w, status;

	if( f = fork() ) {
		// Parent waits
		w = wait(&status);
	} else {		
		char *a=new char[filename.size()+1];
		a[filename.size()]=0;
		memcpy(a,filename.c_str(),filename.size());
		execl("convert", "out.ppm", a, NULL);
	}
}

int Graphics::loadDWFile(string filename) {
	ifstream file(filename);
	Mesh *m = new Mesh();
	int i;

	i = -1;
	i = addMesh(m);

	string line, args;
	while( getline(file, line) ){
		if( line == "l" ) {
			cout << "Found l" << endl;
			double x0, y0, z0, x1, y1, z1;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x0 >> y0 >> z0 >> x1 >> y1 >> z1) {
				m->insertEdge(m->insert(x0,y0,z0,1), m->insert(x1,y1,z1,1));
			}
		} else if( line == "i" ) {
			cout << "Found i" << endl;
			m->resetPosition();
		} else if( line == "s" ) {
			cout << "Found s" << endl;
			double a, b, c;
			getline(file, args);
			istringstream iss(args);
			if(iss >> a >> b >> c) {
				m->scale(a, b, c);
			}
		} else if( line == "t" ) {
			cout << "Found t" << endl;
			double dx, dy, dz;
			getline(file, args);
			istringstream iss(args);
			if(iss >> dx >> dy >> dz) {
				m->trans(dx, dy, dz);
			}
		} else if( line == "x" ) {
			cout << "Found x" << endl;
			double theta;
			getline(file, args);
			istringstream iss(args);
			if(iss >> theta) {
				m->rotateX(theta);
			}
		} else if( line == "y" ) {
			cout << "Found y" << endl;
			double theta;
			getline(file, args);
			istringstream iss(args);
			if(iss >> theta) {
				m->rotateY(theta);
			}
		} else if( line == "z" ) {
			cout << "Found z" << endl;
			double theta;
			getline(file, args);
			istringstream iss(args);
			if(iss >> theta) {
				m->rotateZ(theta);
			}
		} else if (line == "c") {
			cout << "Found c" << endl;
			double x, y, r;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x >> y >> r) {
				m->insertCircle(x, y, r);
			}
		} else if (line == "b") {
			cout << "Found b" << endl;
			double x0, y0, x1, y1, x2, y2, x3, y3;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x0 >> y0 >> x1 >> y1 >> x2 >> y2 >> x3 >> y3) {
				m->insertBezier(x0, y0, x1, y1, x2, y2, x3, y3);
			}
		} else if (line == "h") {
			cout << "Found h" << endl;
			double x0, y0, x1, y1, x2, y2, x3, y3;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x0 >> y0 >> x1 >> y1 >> x2 >> y2 >> x3 >> y3) {
				m->insertHermite(x0, y0, x1, y1, x2, y2, x3, y3);
			}
		} else if (line == "p") {
			cout << "Found p" << endl;
			double x, y, z, w, h, d;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x >> y >> z >> w >> h >> d) {
				m->insertRectPrism(x, y, z, w, h, d);
			}
		} else if (line == "m") {
			cout << "Found m" << endl;
			double x, y, r;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x >> y >> r) {
				m->insertSphere(x, y, r);
			}
		} else if (line == "d") {
			cout << "Found d" << endl;
			double x, y, r1, r2;
			getline(file, args);
			istringstream iss(args);
			if(iss >> x >> y >> r1 >> r2) {
				m->insertTorus(x, y, r1, r2);
			}
		} else if( line == "a" ) {
			cout << "Found a" << endl;
			m->applyTransformation();
			
		} else if( line == "v" ) {
			cout << "Found v" << endl;
			exportGraph();
			system("display out.ppm");
		} else if( line == "g" ) {
			cout << "Found g" << endl;
			getline(file, args);
			exportGraph();
			string tmp = "convert out.ppm " + args;
			system(tmp.c_str());
		} else {
			cout << "Syntax error." << endl;
		}
	}
	

	file.close();
}
