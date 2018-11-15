"""
Points will be stored as 4 element lists: [x, y, z, 1]
Well will store all the points for an image is a list of points
that will be referred to as a matrix
"""

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#Print the point list
def print_matrix( matrix ):
    c = 0
    for i in range( len(matrix) ):
        print "point " + c + ": (" + matrix[c][0] + ", " + matrix[c][1] + ", " + matrix[c][2] + ")\n"
        c += 1
