import math

def make_translate( x, y, z ):
    i = ident(new_matrix())
    i[3][0] = x
    i[3][1] = y
    i[3][2] = z
    return i

def make_scale( x, y, z ):
    i = ident(new_matrix())
    i[0][0] = x
    i[1][1] = y
    i[2][2] = z
    return i
    
# [1, 0, 0, 0]
# [0, cos, -sin, 0]
# [0, sin, cos, 0]
# [0, 0, 0, 1]
def make_rotX( theta ):    
    t = math.radians(theta)
    i = ident(new_matrix())
    i[1][1] = math.cos(t)
    i[1][2] = math.sin(t)
    i[2][1] = -1 * math.sin(t)
    i[2][2] = math.cos(t)
    return i

# [cos, 0, -sin, 0]
# [0, 1, 0, 0]
# [sin, 0, cos, 0]
# [0, 0, 0, 1]
def make_rotY( theta ):
    t = math.radians(theta)
    i = ident(new_matrix())
    i[0][0] = math.cos(t)
    i[0][2] = math.sin(t)
    i[2][0] = -1 * math.sin(t)
    i[2][2] = math.cos(t)
    return i

# [cos, -sin, 0, 0]
# [sin, cos, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
def make_rotZ( theta ):
    t = math.radians(theta)
    i = ident(new_matrix())
    i[0][0] = math.cos(t)
    i[0][1] = math.sin(t)
    i[1][0] = -1 * math.sin(t)
    i[1][1] = math.cos(t)
    return i

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

# [1, 0, 0, 0]
# [0, 1, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
def ident( matrix ): #why does this even have a parameter????
    #for i in range(0,len(matrix)):
    #    matrix[i][i] = 1
    # nah there's a better way for a 4x4 identity
    m = new_matrix()
    for i in range(0, len(m)):
        m[i][i] = 1
    return m

def scalar_mult( matrix, x ):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] * x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix(len(m1[0]),len(m2)) #m1 height x m2 width
    for i in range(0, len(m[0])):
        for j in range(0, len(m)):
            for k in range(0, 4):
                m[j][i] += m1[k][i] * m2[j][k]
    return m

