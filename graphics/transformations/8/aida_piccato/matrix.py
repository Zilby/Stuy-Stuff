import math

def make_translate( x, y, z ):
    res = ident(new_matrix())
    res[3][0] = x
    res[3][1] = y
    res[3][2] = z
    return res

def make_scale( x, y, z ):
    res = ident(new_matrix())
    res[0][0] = x
    res[1][1] = y
    res[2][2] = z
    res[3][3] = 1
    return res

def make_rotZ( theta ):    
    theta = math.radians(theta)
    res = ident(new_matrix())
    res[0][0] = math.cos(theta)
    res[0][1] = math.sin(theta)
    res[1][0] = -1 * math.sin(theta)
    res[1][1] = math.cos(theta)
    return res

def make_rotY( theta ):
    theta = math.radians(theta)
    res = ident(new_matrix())
    res[0][0] = math.cos(theta)
    res[2][0] = -1 * math.sin(theta)
    res[0][2] = math.sin(theta)
    res[2][2] = math.cos(theta)
    return res

def make_rotX( theta ):
    theta = math.radians(theta)
    res = ident(new_matrix())
    res[1][1] = math.cos(theta)
    res[1][2] = math.sin(theta)
    res[2][1] = -1 * math.sin(theta)
    res[2][2] = math.cos(theta)
    return res

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
    for i in range(0,len(matrix)):
        matrix[i][i] = 1
    return matrix

def scalar_matrix(matrix, x ):
    for i in range(0,4):
        for j in range(0,4):
            matrix[i][j] = matrix[i][j]*x
    return matrix

def matrix_mult( m1, m2 ):
    res = new_matrix(len(m1[0]),len(m2))
    for r in range(0,len(res[0])):
        for c in range(0,len(res)):
            for c2 in range(0, 4):
                res[c][r] += m1[c2][r] * m2[c][c2]
    return res

