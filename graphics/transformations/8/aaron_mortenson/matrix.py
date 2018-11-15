import math

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
    

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m1[0]),len(m2))
    for x in range(len(m3)):
        for y in range(len(m3[0])):
            for z in range(len(m2[0])):
                m3[x][y] += m1[z][y] * m2[x][z]
    return m3

'''m1 = [[1,5],[4,4],[3,2]]
m2 = [[2,5,4],[3,0,0],[4,3,1],[1,2,2]] 
m3 = matrix_mult(m1,m2)
m4 = ident(m3)
m5 = matrix_mult(m3,m4)
m6 = scalar_mult(m5,2)
m7 = [[1,2,3,1]]
m8 = make_translate(1,1,2)
m9 = matrix_mult(m8,m7)
print_matrix(m1)
print("times")
print_matrix(m2)
print("equals")
print_matrix(m3)
print("identity:")
print_matrix(m4)
print("multiplied by its own identity:")
print_matrix(m5)
print("scaled up by 2:")
print_matrix(m6)
print_matrix(m7)
print_matrix(m8)
print_matrix(m9)'''


