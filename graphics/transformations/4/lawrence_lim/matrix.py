import math

def make_translate( x, y, z ):
    rmat = new_matrix(4,4)
    rmat = ident(rmat)
    rmat[3][0] = x
    rmat[3][1] = y
    rmat[3][2] = z
    return rmat

def make_scale( x, y, z ):
    rmat = new_matrix(4,4)
    rmat[0][0] = x
    rmat[1][1] = y
    rmat[2][2] = z
    rmat[3][3] = 1
    return rmat
    
def make_rotX( theta ):
    rmat = new_matrix(4,4)
    rad = math.radians(theta)
    rmat[1][1] = math.cos(rad)
    rmat[2][2] = math.cos(rad)
    rmat[1][2] = math.sin(rad)
    rmat[2][1] = -math.sin(rad)
    rmat[0][0] = 1
    rmat[3][3] = 1
    return rmat
    
def make_rotY( theta ):
    rmat = new_matrix(4,4)
    rad = math.radians(theta)
    rmat[0][0] = math.cos(rad)
    rmat[2][2] = math.cos(rad)
    rmat[0][2] = math.sin(rad)
    rmat[2][0] = -math.sin(rad)
    rmat[1][1] = 1
    rmat[3][3] = 1
    return rmat
    
def make_rotZ( theta ):
    rmat = new_matrix(4,4)
    rad = math.radians(theta)
    rmat[0][0] = math.cos(rad)
    rmat[1][1] = math.cos(rad)
    rmat[0][1] = math.sin(rad)
    rmat[1][0] = -math.sin(rad)
    rmat[2][2] = 1
    rmat[3][3] = 1
    return rmat

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

def print_matrix_vert( matrix ):
    for c in matrix:
        print c

def ident( matrix ):
    idmat = new_matrix( len(matrix), len(matrix) )
    for i in range( len( idmat ) ):
        idmat[i][i] = 1
    return idmat

def scalar_mult( matrix, x ):
    for c in range( len(matrix) ):
        for r in range( len( matrix[0] ) ):
            matrix[c][r] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for c in range( len(m2) ):
        for r in range( len(m1[0]) ):
            cell = 0
            for i in range( len(m2[0]) ):
                cell += m1[i][r] * m2[c][i]
            m2[c][r] = cell
