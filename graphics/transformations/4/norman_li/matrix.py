from pixel import Pixel
from copy import deepcopy
from math import degrees, radians, sin, cos, tan

# Matrix Class
class Matrix(object):
    # Constructor
    def __init__(self):
        self.matrix = []

    # Add Point Function
    def add_point(self, x, y, z=0, t=1):
        self.matrix.append( [x, y, z, t] )

    # Add Edge Function
    def add_edge(self, x0, y0, z0, x1, y1, z1, pixel):
        self.add_point( x0, y0, z0 )
        self.add_point( x1, y1, z1 )
        self.matrix.append( pixel ) # Pixel Type

    # --- START Master Transformation Matrix Stuff --- #
    # Revert to Identtiy Matrix Function
    def identity(self):
        del self.matrix
        self.matrix = []

        # Add Matrix
        self.matrix.append([1, 0, 0, 0])
        self.matrix.append([0, 1, 0, 0])
        self.matrix.append([0, 0, 1, 0])
        self.matrix.append([0, 0, 0, 1])

    # Scalar Multiplication
    def multiply_scalar(self, n):
        for i in range( len( self.matrix ) ):
            for j in range( len( self.matrix[0] ) ):
                self.matrix[i][j] *= n

    # Matrix Multiplication (Forwards)
    def multiply_forwards(self, matrix):
        new_matrix = [[0 for y in range( len(self.matrix[0]) )] for x in range( len( matrix.matrix ) )]

        for i in range( len( self.matrix[0] ) ):
            for j in range( len( matrix.matrix ) ):
                for k in range( len( matrix.matrix[0] ) ):
                    new_matrix[j][i] += self.matrix[k][i] * matrix.matrix[j][k]

        del self.matrix
        self.matrix = deepcopy(new_matrix)

    # Matrix Multiplication (Backwards)
    def multiply_backwards(self, matrix):
        new_matrix = deepcopy(matrix)

        new_matrix.multiply_forwards(self)

        del self.matrix
        self.matrix = new_matrix.matrix

    # Edge Matrix Multiplication (SPECIAL CASE)
    # As every third (index 2, 5, 8, etc...) has a color
    def multiply_edge(self, master):
        new_matrix_list = deepcopy( self.matrix )
        new_matrix_list_no_color = []
        color_list = []

        for i in new_matrix_list:
            if ( type( i ) is Pixel ):
                color_list.append( i )
            else:
                new_matrix_list_no_color.append( i )

        no_color_edge = Matrix()
        for j in new_matrix_list_no_color:
            no_color_edge.matrix.append(j)

        # The Actual Multiplication
        no_color_edge.multiply_backwards(master)

        # Readd Colors
        del self.matrix
        self.matrix = no_color_edge.matrix

        k = 2
        while ( len(color_list) != 0 ):
            self.matrix.insert( k, color_list.pop(0) )
            k += 3

    # Translation Matrix
    def translation(self, x, y, z):
        self.identity()

        # X, Y, Z Placement
        self.matrix[3][0] = x
        self.matrix[3][1] = y
        self.matrix[3][2] = z

    # Scale Matrix
    def scale(self, x, y, z):
        self.identity()

        # X, Y, Z Placement
        self.matrix[0][0] = x
        self.matrix[1][1] = y
        self.matrix[2][2] = z

    # Rotation about the x-axis
    def rotate_x(self, theta):
        self.identity()
        theta_radians = radians(theta)

        # Placement
        self.matrix[1][1] = cos( theta_radians )
        self.matrix[1][2] = sin( theta_radians )
        self.matrix[2][1] = -1 * sin( theta_radians )
        self.matrix[2][2] = cos( theta_radians )

    # Rotation about the y-axis
    def rotate_y(self, theta):
        self.identity()
        theta_radians = radians(theta)

        # Placement
        self.matrix[0][0] = cos( theta_radians )
        self.matrix[0][2] = sin( theta_radians )
        self.matrix[2][0] = -1 * sin( theta_radians )
        self.matrix[2][2] = cos( theta_radians )

    # Rotation about the z-axis
    def rotate_z(self, theta):
        self.identity()
        theta_radians = radians(theta)

        # Placement
        self.matrix[0][0] = cos( theta_radians )
        self.matrix[0][1] = sin( theta_radians )
        self.matrix[1][0] = -1 * sin( theta_radians )
        self.matrix[1][1] = cos( theta_radians )

    # --- END Master Transformation Matrix Stuff --- #

    # toString() Method
    def __str__(self):
        result = ""

        for i in range( len( self.matrix[0] ) ):
            for j in range( len( self.matrix ) ):
                result += "%d\t" %( self.matrix[j][i] )

            result += "\n"

        return result
