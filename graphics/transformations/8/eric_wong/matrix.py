import math

def make_translate( x, y, z ):
    return [ [1, 0, 0, 0], 
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [x, y, z, 1]
           ]

def make_scale( x, y, z ):
    return [ [x, 0, 0, 0],
             [0, y, 0, 0],
             [0, 0, z, 0],
             [0, 0, 0, 1]
           ]

def make_rotX( theta ):
    angle = float(theta * math.pi / 180)
    return [ [1, 0, 0, 0],
             [0, math.cos(angle), math.sin(angle), 0],
             [0, -1*math.sin(angle), math.cos(angle), 0],
             [0, 0, 0, 1]
           ]

def make_rotY( theta ):
    angle = float(theta * math.pi / 180)
    return [ [math.cos(angle), 0, math.sin(angle), 0],
             [0, 1, 0, 0],
             [-1*math.sin(angle),0, math.cos(angle), 0],
             [0, 0, 0, 1]
           ]

def make_rotZ( theta ):
    angle = float(theta * math.pi / 180)
    return [ [math.cos(angle), math.sin(angle), 0, 0],
             [-1*math.sin(angle),math.cos(angle), 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]
           ]

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
            s+= str(int(matrix[c][r])) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]
           ]

def scalar_mult( matrix, x ):
    m = matrix
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            m[c][r] = matrix[c][r] * x
    return m

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if (len(m1) != len(m2[0])):
        print "Cannot multiply these matrices together"
        return
    m3 = new_matrix(len(m1[0]), len(m2))
    for c2 in range(len(m2)):
        for r2 in range(len(m2[c2])):
            for c1 in range(len(m1)):
                if c1 == r2:
                    sum = 0
                    for r1 in range(len(m1[c1])):
                        sum = sum + m2[c2][r2] * m1[c1][r1]
                    m3[c2][r2] = sum
    return m3
            

