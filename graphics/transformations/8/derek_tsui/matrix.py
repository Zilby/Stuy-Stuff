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
    rad = theta*math.pi/180
    return [ [1, 0, 0, 0],
             [0, math.cos(rad), math.sin(rad), 0],
             [0, -1*math.sin(rad), math.cos(rad), 0],
             [0, 0, 0, 1] ]

def make_rotY( theta ):
    rad = theta*math.pi/180
    return [ [math.cos(rad), 0, math.sin(rad), 0],
             [0, 1, 0, 0],
             [-math.sin(rad), 0, math.cos(rad), 0],
             [0, 0, 0, 1] ]

def make_rotZ( theta ):
    rad = theta*math.pi/180
    return [ [math.cos(rad), math.sin(rad), 0, 0],
             [-math.sin(rad), math.cos(rad), 0, 0],
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

def ident():
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1] ]

def scalar_mult( matrix, x ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if (len(m1) != len(m2[0])):
        print "matrix mult error"
    else:
        m = new_matrix(len(m1[0]), len(m2))
        for i in range(len(m1[0])):
            for j in range(len(m2)):
                for k in range(len(m2[0])):
                    m[j][i] += m1[k][i] * m2[j][k]
    return m
