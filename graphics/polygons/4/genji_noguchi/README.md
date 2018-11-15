Coding Bresenham's Line Algorithm
=================================

Language : C++


main.cpp --------- Contains the main function runner and things.

class Matrix ----- Contains the static functions for matrix manipulation.

struct Vect4 ----- A simple struct that contains 4 ints- x, y, z, 1. Represents a single column of the Mat4.

class Mesh ------- Extends the Matrix class. Extras include a 4x4 matrix for temporary 

class Graphics --- The main function for the graphics library. Contains the function to export to ppm.

class Raster ----- Contains the information to translate the graphics information into something displayable on the screen. Contains the function to export to image (ppm).

class Loader ----- Contains the parsers for different types of object files.


<br>
<br>
<br>
<br>



Things to do:
Short-term
* Fix the translations for 3d shapes
* Polygon implementation
* Write a .obj parser.
* Fix the null return warnings
* Optimize the for loops so that ints are used instead of doubles
 
<br>
<br>

Long-term
* Update the changelog!!!!!!
* Turn header files into documentation
* Mucho comments
* Add file interpreter
* Colors (textures?)
* Optimize the matrix class
* Optimize the sphere insertion algorithms-- possibly using matrix multiplication instead of for loops?
* Compatibility with Linux





~ Genji Noguchi

