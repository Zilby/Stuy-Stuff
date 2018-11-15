import math

def make_translate( x, y, z ):
    m = ident(new_matrix())
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m

def make_scale( x, y, z ):
    m = ident(new_matrix())
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    return m

    
def make_rotX( theta ):    
    m = ident(new_matrix())
    theta = math.radians(theta)
    m[1][1] = math.cos(theta)
    m[2][1] = -1 * math.sin(theta)
    m[1][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotY( theta ):
    m = ident(new_matrix())
    theta = math.radians(theta)
    m[0][0] = math.cos(theta)
    m[2][0] = -1 * math.sin(theta)
    m[0][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotZ( theta ):
    m = ident(new_matrix())
    theta = math.radians(theta)
    m[0][0] = math.cos(theta)
    m[1][0] = -1 * math.sin(theta)
    m[0][1] = math.sin(theta)
    m[1][1] = math.cos(theta)
    return m

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
    n = len(matrix[0])
    m = new_matrix(n, n)
    for i in range(n):
        m[i][i] = 1
    return m

def scalar_mult( matrix, x ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r] = matrix[c][r] * x
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m1[0]), len(m2))
    for i in range(len(m[0])):
        for j in range(len(m)):
            for k in range(4):
                m[j][i] += m1[k][i] * m2[j][k]
    return m


