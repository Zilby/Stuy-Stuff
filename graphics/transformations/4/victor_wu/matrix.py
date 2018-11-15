import math

def make_translate( x, y, z ):
    t = new_matrix()
    t[0] = [1, 0, 0, x]
    t[1] = [0, 1, 0, y]
    t[2] = [0, 0, 1, z]
    t[3] = [0, 0, 0, 1]
    return t

def make_scale( x, y, z ):
    s = new_matrix()
    s[0] = [x, 0, 0, 0]
    s[1] = [0, y, 0, 0]
    s[2] = [0, 0, z, 0]
    s[3] = [0, 0, 0, 1]
    return s

def make_rotX( theta ):
    angle = float(theta * math.pi / 180)
    rotX = new_matrix()
    rotX[0] = [1, 0, 0, 0]
    rotX[1] = [0, math.cos(angle), -1*math.sin(angle), 0]
    rotX[2] = [0, math.sin(angle), math.cos(angle), 0]
    rotX[3] = [0, 0, 0, 1]
    return rotX

def make_rotY( theta ):
    angle = float(theta * math.pi / 180)
    rotY = new_matrix()
    rotY[0] = [math.cos(angle), 0, -1*math.sin(angle), 0]
    rotY[1] = [0, 1, 0, 0]
    rotY[2] = [math.sin(angle),0, math.cos(angle), 0]
    rotY[3] = [0, 0, 0, 1]
    return rotY

def make_rotZ( theta ):
    angle = float(theta * math.pi / 180)
    rotZ = new_matrix()
    rotZ[0] = [math.cos(angle), -1*math.sin(angle), 0, 0]
    rotZ[1] = [math.sin(angle),math.cos(angle), 0, 0]
    rotZ[1] = [0, 0, 1, 0]
    rotZ[3] = [0, 0, 0, 1]
    return rotZ

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
    matrix[0] = [1, 0, 0, 0]
    matrix[1] = [0, 1, 0, 0]
    matrix[2] = [0, 0, 1, 0]
    matrix[3] = [0, 0, 0, 1]
    return matrix

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
    m3 = new_matrix(len(m2), len(m1[0]))
    for c2 in range(len(m2)):
        for r2 in range(len(m2[c2])):
            for c1 in range(len(m1)):
                if c1 == r2:
                    sum = 0
                    for r1 in range(len(m1[c1])):
                        sum = sum + m2[c2][r2] * m1[c1][r1]
                    m3[c2][r2] = sum
    return m3
            

