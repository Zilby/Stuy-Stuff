import math

def make_bezier():
    return [[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]]

def make_hermite():
    return [[2,-3,0,1],[-2,3,0,0],[1,-2,1,0],[1,-1,0,0]]

def generate_curve_coefs( p1, p2, p3, p4, t ):
    if t == 'bezier':
        return matrix_mult(make_bezier(),[[p1,p2,p3,p4]])
    elif t == 'hermite':
        return matrix_mult(make_hermite(),[[p1,p2,p3,p4]])

def make_translate( x, y, z ):
    m = ident(new_matrix(4,4))
    m[3][0], m[3][1], m[3][2], m[3][3] = x,y,z,1
    return m

def make_scale( x, y, z ):
    m = new_matrix(4,4)
    m[0][0], m[1][1], m[2][2], m[3][3] = x,y,z,1
    return m
 
def make_rotX( theta ): 
    theta = math.radians(theta)
    m = ident(new_matrix(4,4))
    m[1][1] = math.cos(theta)
    m[1][2] = math.sin(theta)
    m[2][1] = -1*math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotY( theta ):
    theta = math.radians(theta)
    m = ident(new_matrix(4,4))
    m[0][0] = math.cos(theta)
    m[0][2] = math.sin(theta)
    m[2][0] = -1*math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotZ( theta ):
    theta = math.radians(theta)
    m = ident(new_matrix(4,4))
    m[0][0] = math.cos(theta)
    m[0][1] = math.sin(theta)
    m[1][0] = -1*math.sin(theta)
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
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    maxlen = max(len(matrix),len(matrix[0])) 
    m2 = new_matrix(maxlen,maxlen)
    for i in range(maxlen):
        m2[i][i] = 1
    return m2

def scalar_mult( matrix, x ):
    m2 = new_matrix(len(matrix[0]),len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m2[i][j] = matrix[i][j] * x
    return m2
    
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m1[0]),len(m2))
    for x in range(len(m3)):
        for y in range(len(m3[0])):
            for z in range(len(m2[0])):
                m3[x][y] += m1[z][y] * m2[x][z]
    return m3

