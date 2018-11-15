"""
Points will be stored as 4 element lists: [x, y, z, 1]
We will store all the points for an image is a list of points
that will be referred to as a matrix

For example...
[
   [1,2,3,1],
   [1,2,3,1]
]

"""
STD_ROWS = 4

#Creates a new matrix
def new_matrix(rows, cols):
    rows = STD_ROWS
    m = []
    #c represents a new point
    for c in range( cols ):
        m.append( [] )
        #r is always 4; that is, there should always be 4 elements
        for r in range( rows ):
            m[c].append( 0 )
    return m

#Print the point list
def print_matrix( matrix ):
    retStr = "{"
    for c in range(len(matrix)):
        retStr += "\t[" 
        for r in range(len(matrix[0])):
            retStr += " " + str(matrix[c][r]) + " "
        retStr += "]\n"
    retStr += "\t\t\t\t}" 
    print retStr
    
if __name__ == "__main__":
    test = new_matrix(STD_ROWS, 7)
    print_matrix(test)
