import math

def make_translate( x, y, z ):
    m = new_matrix()
    m = ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m

def make_scale( x, y, z ):
    m = new_matrix()
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    m[3][3] = 1
    return m

def make_rotX( theta ):
    m = new_matrix()
    m = ident(m)
    theta = math.radians(theta)
    cos = math.cos(theta)
    sin = math.sin(theta)
    m[1][1] = cos
    m[1][2] = sin
    m[2][1] = -sin
    m[2][2] = cos
    return m

def make_rotY( theta ):
    m = new_matrix()
    m = ident(m)
    theta = math.radians(theta)
    cos = math.cos(theta)
    sin = math.sin(theta)
    m[0][0] = cos
    m[0][2] = sin
    m[2][0] = -sin
    m[2][2] = cos
    return m

def make_rotZ( theta ):
    m = new_matrix()
    m = ident(m)
    theta = math.radians(theta)
    cos = math.cos(theta)
    sin = math.sin(theta)
    m[0][0] = cos
    m[0][1] = sin
    m[1][0] = -sin
    m[1][1] = cos
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
    return s

def ident( matrix ):
    i = new_matrix(len(matrix), len(matrix))
    for r in range (len (i[0])):
        for c in range (len(i)):
            if r == c:
                i[c][r] = 1
            else:
                i[c][r] = 0
    return i

def scalar_mult( matrix, x ):
    for r in range (len (matrix[0] )) :
        for c in range (len (matrix)) :
            matrix[c][r] *= x


def matrix_mult( m1, m2 ):
    if len(m1) != len (m2[0]):
        print ("cant mult")
        return
    m  = new_matrix(len(m1[0]), len(m2))
    for r in range (len (m[0])):
        for c in range (len (m)):
            i = 0
            sum = 0
            while (i <= len(m)):
                sum += m1[i][r]*m2[c][i]
                i += 1
            m[c][r] = sum
    return m