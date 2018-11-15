import math

def make_translate( x, y, z ):
    matrix=ident(new_matrix())
    matrix[3][0]=x
    matrix[3][1]=y
    matrix[3][2]=z
    return matrix
def make_scale( x, y, z ):
    matrix=ident(new_matrix())
    matrix[0][0]=x
    matrix[1][1]=y
    matrix[2][2]=z
    return matrix
    
def make_rotX( theta ):    
    rad =math.radians(theta)
    cos= math.cos(rad)
    sin =math.sin(rad)
    matrix=ident(new_matrix())
    matrix[1][1]= cos
    matrix[2][1]= -sin
    matrix[1][2]= sin
    matrix[2][2]= cos
    return matrix
def make_rotY( theta ):
    rad =math.radians(theta)
    cos= math.cos(rad)
    sin =math.sin(rad)
    matrix=ident(new_matrix())
    matrix[0][0]= cos
    matrix[2][0]= -sin
    matrix[0][2]= sin
    matrix[2][2]= cos
    return matrix
def make_rotZ( theta ):
    rad =math.radians(theta)
    cos= math.cos(rad)
    sin =math.sin(rad)
    matrix=ident(new_matrix())
    matrix[0][0]= cos
    matrix[1][0]= -sin
    matrix[0][1]= sin
    matrix[1][1]= cos
    return matrix
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    x=0;
    while x < len(matrix):
        y=0
        while y <len(matrix[x]):
            if (x == y):
                matrix[x][y]=1
            else:
                matrix[x][y]=0
            y+=1
        x+=1
    return matrix
def scalar_mult( matrix, x ):
   for row in matrix:
        for element in row:
            element = x * element
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m1[0]),len(m2))
    for x in range(0, len(m)):
        for y in range(0, len(m[x])):
            for x2 in range(0, len(m[x])):
                m[x][y] += m1[x2][y] * m2[x][x2]
    return m


