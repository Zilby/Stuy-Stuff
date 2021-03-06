#include "mesh.h"


#include <cstring>
#include <cstdlib>
#include <cmath>

using std::endl;

Face::Face() {}

Face::Face(int a, int b, int c) {
	v1 = a;
	v2 = b;
	v3 = c;
}

string Face::to_string() {
	string temp;

	temp.append("");
	temp.append(std::to_string(v1));
	temp.append(", ");
	temp.append(std::to_string(v2));
	temp.append(", ");
	temp.append(std::to_string(v3));

	return temp;
}

Mesh::Mesh() 
: Entity() {
}

Mesh::Mesh(int deleteonremove) 
: Entity(), deleteOnRemove(deleteonremove) {
}

Mesh::Mesh(const Mesh& other) :
	markedForDeath(other.markedForDeath),
	deleteOnRemove(other.deleteOnRemove),
	verts(vector<Vect4>(other.verts)),
	faces(vector<Face>(other.faces)),
	children(unordered_map<string, Mesh*>(other.children)) {

		//clone all child meshes
		for(auto it = children.begin(); it != children.end(); it++) {
			it->second = new Mesh(*(it->second));
		}
}

Mesh::~Mesh() {
	clear();
	for(auto it = children.begin(); it != children.end(); it++) {
		delete it->second;
	}
}

void Mesh::clear() {
	verts.clear();
	faces.clear();
}

void Mesh::addChild(string name, Mesh *m) {
	if(children.count(name)) {
		cerr << "Child mesh already exists with name " << name << "\n";
		return;
	}
	children[name] = m;
}

Mesh* Mesh::getChild(string name) {
	if(!children.count(name)) {
		cerr << "No child mesh exists with name " << name << "\n";
		return NULL;
	}
	return children[name];
}

int Mesh::addVert(Vect4 v) {
	verts.push_back(v);
	return verts.size() - 1;
}

void Mesh::addFace(Face f) {
	faces.push_back(f);
}

//Replaces next occurence of delim with null
//Returns start of next string, or null if end
char *Mesh::myStrtok(char *s, char delim) { 
	while(1) {
		//Checl if hit end
		if(!*s)
			return NULL;

		//Check if hit delimiter
		if(*s == delim) { 
			//null all delimiters
			while(1) {
				*s = '\0';
				s++;
				if(!*s) 
					return NULL;
				if(*s != delim) {
					return s;
				}
			}
		}

		//If not, keep going
		s++;
	}
}

void Mesh::loadFromObjFile(string filename) {
	addVert(Vect4(0,0,0));//dummy vert to account for 1-indexing


	std::ifstream fs;
	char buffer[1024];

	fs.open(filename);
	
	while(!fs.eof()) {
		char *next, *curr;

		fs.getline(buffer, 1024);
		
		curr = buffer;
		next = myStrtok(curr, ' ');

		//Handles blank lines
		if(*curr == '\0')
			continue;

		

		if(!strcmp(buffer, "#")) {
			cerr << "Ignoring comment" << endl;
		} else if(!strcmp(buffer, "o")) {
			//cerr << "ignoring o for now" << endl;
		} else if(!strcmp(buffer, "v")) {
			//cerr << "handling v" << endl;
			Vect4 v;

			char *temp = next; //points to start of first float
			for(int i = 0; i < 3; i++)
				v.coord[i] = strtod(temp, &temp);
			v.coord[3] = 1;

			addVert(v);
		} else if(!strcmp(buffer, "vt")) {
			//cerr << "ignoring vt for now" << endl;
		} else if(!strcmp(buffer, "vn")) {
			//cerr << "ignoring vn for now" << endl;
		} else if(!strcmp(buffer, "f")) {
			Face f;

			char *temp = next; //points to start of first int
			f.v1 = strtol(temp, &temp, 0);
			while(*temp++ != ' ')
				;
			f.v2 = strtol(temp, &temp, 0);
			while(*temp++ != ' ')
				;
			f.v3 = strtol(temp, &temp, 0);

			//cerr << f.v1 << ", " << f.v2 << ", " << f.v3 << "\n";

			addFace(f);
			//cerr << "Woo! f" << endl;
		} else if(!strcmp(buffer, "s")) {
			cerr << "ignored s" << endl;
		} else {
			//Delay
			for(int i = 0; i < 100 * 1000 * 1000; i++)
				;
			cerr << "Unkown start word: '" << buffer << "'" << endl;
		}
	}


	fs.close();
}

std::string Mesh::to_string() const {
	std::string temp;

	temp.append(Entity::to_string());

	temp.append("\nfaces: ");
	temp.append(std::to_string(faces.size()));
	temp.append("\n");

	return temp;
}

void Mesh::genPrimEdge(Vect4 a, Vect4 b) {
	int av = addVert(a);
	int bv = addVert(b);
	addFace(Face {av, bv, bv});
}

void Mesh::genPrimCircle(Vect4 c, double r) {
	double t = 0;

	const int edges = 50;

	double lastx, lasty, currx, curry;

	lasty = sin(t) * r;
	lastx = cos(t) * r;

	for(int i = 1; i <= edges; i++) {
		t = (TWOPI / edges) * i;

		currx = cos(t) * r;
		curry = sin(t) * r;

		genPrimEdge(
				Vect4(currx + c[0], curry + c[1], c[2]), 
				Vect4(lastx + c[0], lasty + c[1], c[2]));

		lastx = currx;
		lasty = curry;
	}
}

//Start, start control, end control, end
void Mesh::genPrimBezier(Vect4 a, Vect4 b, Vect4 c, Vect4 d) {
	double t = 0;

	const int edges = 50;

	Vect4 ab;
	Vect4 bc;
	Vect4 cd;

	Vect4 ab_bc;
	Vect4 bc_cd;

	Vect4 end;

	Vect4 last = a; //starts at a

	for(int i = 1; i <= edges; i++) {
		t = (1.0 / edges) * i;

		ab = Vect4::vLerp(a, b, t);
		bc = Vect4::vLerp(b, c, t);
		cd = Vect4::vLerp(c, d, t);

		ab_bc = Vect4::vLerp(ab, bc, t);
		bc_cd = Vect4::vLerp(bc, cd, t);

		end = Vect4::vLerp(ab_bc, bc_cd, t);

		genPrimEdge(last, end);

		last = end;
	}
}

void Mesh::genPrimHermite(Vect4 p0, Vect4 p1, Vect4 r0, Vect4 r1) {
	const int edges = 80;

	Vect4 curr;
	Vect4 last = p0; //starts at p0

	for(int i = 1; i <= edges; i++) {
		double t = (1.0 / edges) * i;
		double t2 = t * t;
		double t3 = t2 * t;

		double h0 = 2 * t3 - 3 * t2 + 1;
		double h1 = -2 * t3 + 3 * t2;
		double h2 = t3 - 2 * t2 + t;
		double h3 = t3 - t2;

		//Do this for each coordinate
		for(int j = 0; j < 3; j++) {
			curr[j] = 
					h0 * p0[j] +
					h1 * p1[j] +
					h2 * r0[j] +
					h3 * r1[j];
		}

		genPrimEdge(last, curr);

		last = curr;
	}

}

void Mesh::genPrimBox(double lx, double ly, double lz) {
	lx *= lx > 0 ? 1 : -1;
	ly *= ly > 0 ? 1 : -1;
	lz *= lz > 0 ? 1 : -1;

	int v0 = addVert(Vect4( 0,  0,  0));
	int v1 = addVert(Vect4(lx,  0,  0));
	int v2 = addVert(Vect4( 0, ly,  0));
	int v3 = addVert(Vect4( 0,  0, lz));
	int v4 = addVert(Vect4( 0, ly, lz));
	int v5 = addVert(Vect4(lx,  0, lz));
	int v6 = addVert(Vect4(lx, ly,  0));
	int v7 = addVert(Vect4(lx, ly, lz));

	//0 xy face
	addFace(Face(v0, v2, v1));
	addFace(Face(v6, v1, v2));

	//far xy face
	addFace(Face(v4, v3, v5));
	addFace(Face(v5, v7, v4));

	//0 xz face
	addFace(Face(v0, v1, v3));
	addFace(Face(v5, v3, v1));

	//far xz face
	addFace(Face(v6, v2, v4));
	addFace(Face(v4, v7, v6));

	//0 yz face
	addFace(Face(v0, v3, v2));
	addFace(Face(v4, v2, v3));

	//far yz face
	addFace(Face(v5, v1, v6));
	addFace(Face(v6, v7, v5));
}

void Mesh::genPrimSphere(double r) {
	const int slices = 20;
	const int pps = 10;//points per slice

	int top = addVert(Vect4(0, r, 0));
	int bot = addVert(Vect4(0, -r, 0));

	//Contains all the vert indices except the top and bottom
	int points[slices][pps - 1];

	for(int i = 0; i < slices; i++) {
		double phi = (TWOPI / slices) * i;

		for(int j = 1; j < pps; j++) {
			double theta = (PI / pps) * j;

			//theta 0 -> top, theta pi -> bottom
			//phi 0 -> +x, goes counterclockwise from top

			double vert = r * cos(theta);
			double horiz = r * sin(theta);

			Vect4 temp;
			temp[0] = horiz * sin(phi);
			temp[1] = vert;
			temp[2] = horiz * cos(phi);

			points[i][j - 1] = addVert(temp);
		}
	}

	//make caps
	for(int i = 0; i < slices; i++) {
		addFace(Face(
				top, 
				points[i][0], 
				points[(i + 1) % slices][0]));
		addFace(Face(
				bot, 
				points[(i + 1) % slices][pps - 2],
				points[i][pps - 2]));
	}

	//make body
	for(int i = 0; i < slices; i++) {
		for(int j = 1; j < pps - 1; j++) {
			//bottomleft
			addFace(Face(
					points[i][j - 1], 
					points[i][j], 
					points[(i + 1) % slices][j]));

			//topright
			addFace(Face(
					points[(i + 1) % slices][j - 1], 
					points[i][j - 1], 
					points[(i + 1) % slices][j]));
		}
	}
}

void Mesh::genPrimTorus(double R, double r) {
	const int circles = 20;
	const int ppc = 15;//points per circle

	int points[circles][ppc];

	for(int i = 0; i < circles; i++) {
		double phi = (TWOPI / circles) * i;

		Mat4 currRot = Mat4::mult(Mat4::RotateYMat(phi), Mat4::TranslateMat(Vect4(R, 0 , 0)));

		for(int j = 0; j < ppc; j++) {
			double theta = (TWOPI / ppc) * j;

			//theta 0 -> top, theta pi -> bottom
			//phi 0 -> +x, goes counterclockwise from top

			double vert = r * cos(theta);
			double horiz = r * sin(theta);

			Vect4 temp;
			temp[0] = horiz;
			temp[1] = vert;
			temp[2] = 0;

			points[i][j] = addVert(currRot.mult(temp));
		}
	}


	//make body
	for(int i = 0; i < circles; i++) {
		for(int j = 0; j < ppc; j++) {
			//bottomleft
			addFace(Face(
					points[i][j], 
					points[i][(j + 1) % ppc], 
					points[(i + 1) % circles][(j + 1) % ppc]));

			//topright
			addFace(Face(
					points[(i + 1) % circles][j], 
					points[i][j], 
					points[(i + 1) % circles][(j + 1) % ppc]));
		}
	}
}

void Mesh::doCommand(vector<string> c) {
	if(!c[0].compare("loadfromfile")) {
		loadFromObjFile(c[1]);
	}
}
