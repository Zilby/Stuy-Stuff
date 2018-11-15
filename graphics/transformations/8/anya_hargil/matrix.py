import math

def make_translate( x, y, z ):
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [x, y, z, 1] ]

def make_scale( x, y, z ):
    return [ [x, 0, 0, 0],
             [0, y, 0, 0],
             [0, 0, z, 0],
             [0, 0, 0, 1] ]
    
def make_rotX( theta ):
    return [ [1, 0, 0, 0],
             [0, math.cos(math.pi*theta/180), math.sin(math.pi*theta/180), 0],
             [0, -(math.sin(math.pi*theta/180)), math.cos(math.pi*theta/180), 0],
             [0, 0, 0, 1] ]

def make_rotY( theta ):
    return [ [math.cos(math.pi*theta/180), 0, math.sin(math.pi*theta/180), 0],
             [0, 1, 0, 0],
             [-(math.sin(math.pi*theta/180)), 0, math.cos(math.pi*theta/180), 0],
             [0, 0, 0, 1] ]

def make_rotZ( theta ):
    return [ [math.cos(math.pi*theta/180), math.sin(math.pi*theta/180), 0, 0],
             [-(math.sin(math.pi*theta/180)), math.cos(math.pi*theta/180), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1] ]

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
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1] ]

def scalar_mult( matrix, x ):
    m = make_scale(x, x, x)
    return matrix_mult( m, matrix )

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if (len(m1) != len(m2[0])):
        print "You cannot do this matrix multiplication!"
        return
    sun = 0
    m = new_matrix(len(m1[0]), len(m2))
    for c2 in range(len(m2)):
        for r1 in range(len(m1[0])):
            for c1r2 in range(len(m1)):
		m[r1][c2] += m1[c1r2][c2] * m2[r1][c1r2]
    return m
