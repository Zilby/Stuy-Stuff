#include <iostream>
#include "graphics.h"
#include "raster.h"
#include "matrix.h"
#include "mesh.h"
#include "vect4.h"
#include "loader.h"

using namespace std;

int main() {
	Graphics g(500,500);
	//Mesh m, m2;

	/*
	int p1,p2,p3,p4,p5,p6,p7,p8;
	int m1;


	p1 = m.insert(210,210,0,1);
	p2 = m.insert(300,210,0,1);
	p3 = m.insert(300,300,0,1);
	p4 = m.insert(210,300,0,1);
	p5 = m.insert(210,210,90,1);
	p6 = m.insert(300,210,90,1);
	p7 = m.insert(300,300,90,1);
	p8 = m.insert(210,300,90,1);


	m.insertEdge(p1,p2);
	m.insertEdge(p2,p3);
	m.insertEdge(p3,p4);
	m.insertEdge(p4,p1);
	m.insertEdge(p5,p6);
	m.insertEdge(p6,p7);
	m.insertEdge(p7,p8);
	m.insertEdge(p8,p5);
	m.insertEdge(p1,p5);
	m.insertEdge(p2,p6);
	m.insertEdge(p3,p7);
	m.insertEdge(p4,p8);

	m2 = m;

	m.rotateY(45);
	m.rotateX(45);
	m.rotateZ(45);
	m.transformation.print();

	//m.insertEdge(p4,p1);
	m.toString();


	g.addMesh(m);
	//g.addMesh(m2);

	*/

	g.exportGraph();

	int i = g.loadDWFile("curvetest.dwobj");

	cout << "Done." << endl;

}
