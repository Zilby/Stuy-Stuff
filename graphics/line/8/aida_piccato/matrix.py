"""
Points will be stored as 4 element lists: [x, y, z, 1]
We will store all the points for an image as a list of points
that will be referred to as a matrix
"""

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
    return m

#Print the point list
def print_matrix( matrix ):
	res = "X Y Z 1\n"
	for r in range(0, len( matrix[0] ) ):
		for c in range(0, 4):
			res += str( matrix[c][r] ) + " "
		res += "\n"
	print(res)

		



