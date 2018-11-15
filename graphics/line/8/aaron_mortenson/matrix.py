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
     for i in range(len(matrix[0])):
        print "(%i,%i,%i,%i)," % (matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i])

