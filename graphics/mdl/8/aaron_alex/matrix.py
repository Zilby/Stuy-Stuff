import math

VIEW = [0, 0, -1]

def facing_view(poly):
    A = [poly[1][0]-poly[0][0],poly[1][1]-poly[0][1],poly[1][2]-poly[0][2]]
    B = [poly[2][0]-poly[0][0],poly[2][1]-poly[0][1],poly[2][2]-poly[0][2]]
    NORM = [A[1]*B[2] - A[2]*B[1],A[2]*B[0] - A[0]*B[2], A[0]*B[1] - A[1]*B[0]]
    COS = NORM[0]*VIEW[0] + NORM[1]*VIEW[1] + NORM[2]*VIEW[2]
    return COS < 0

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
    m = new_matrix(4,4)
    ident(m)
    m[3][0], m[3][1], m[3][2], m[3][3] = x,y,z,1
    return m

def make_scale( x, y, z ):
    m = new_matrix(4,4)
    m[0][0], m[1][1], m[2][2], m[3][3] = x,y,z,1
    return m
 
def make_rotX( theta ): 
    theta = math.radians(theta)
    m = new_matrix(4,4)
    ident(m)
    m[1][1] = math.cos(theta)
    m[1][2] = math.sin(theta)
    m[2][1] = -1*math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotY( theta ):
    theta = math.radians(theta)
    m = new_matrix(4,4)
    ident(m)
    m[0][0] = math.cos(theta)
    m[0][2] = math.sin(theta)
    m[2][0] = -1*math.sin(theta)
    m[2][2] = math.cos(theta)
    return m

def make_rotZ( theta ):
    theta = math.radians(theta)
    m = new_matrix(4,4)
    ident(m)
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
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            if x == y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= x
    
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m1[0]),len(m2))
    for x in range(len(m3)):
        for y in range(len(m3[0])):
            for z in range(len(m2[0])):
                m3[x][y] += m1[z][y] * m2[x][z]
    for x in range(len(m2)):
        for y in range(len(m1[0])):
            if y > len(m2[0]) - 1:
                m2[x].append(m3[x][y])
            else:
                m2[x][y] = m3[x][y]
                
