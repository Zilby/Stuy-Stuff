#ifndef LOADER_H
#define LOADER_H

#include <string>
#include "mesh.h"
#include "graphics.h"

using std::string;

/*
 * Container class for loading in drawing files.
 */
class Loader {

	public:

		static Mesh loadObj(string filename);

};

#endif
