from pixel import Pixel

# Matrix Class

class Matrix(object):
    matrix = []

    # Add Point Function
    def add_point(self, x, y, z=0, t=1):
        self.matrix.append( [x, y, z, t] )

    # Add Edge Function
    def add_edge(self, x0, y0, x1, y1, pixel):
        self.add_point( x0, y0 )
        self.add_point( x1, y1 )
        self.matrix.append( pixel ) # Pixel Type

    # toString() Method
    def __str__(self):
        result = "Edge Drawing Instructions: \n"
        result += "[x1, y1, z1, t1] -> [x2, y2, z2, t2]\n"
        result += "========================================\n\n"

        end = len( self.matrix )
        i = 0

        while (i < end):
            result += "%s -> %s. RGB Values: %s\n" %( self.matrix[i], self.matrix[i + 1], self.matrix[i + 2] )

            i += 3

        return result
