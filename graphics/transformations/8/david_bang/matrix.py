import math

def make_translate( x, y, z ):
    m = ident(new_matrix())
    m [0][3] = x
    m [1][3] = y
    m [2][3] = z
    return m 

    
def make_scale( x, y, z ):
    m = new_matrix ()
    m [0][0] = x
    m [1][1] = y
    m [2][2] = z
    m [3][3] = 1
    return m 
    
def make_rotX( theta ):
    theta = theta * 180/math.pi 
    m = new_matrix ()
    m [0][0] = 1
    m [1][1] = math.cos(theta)
    m [1][2] = 0 - math.sin(theta)
    m [2][1] = math.sin(theta)
    m [2][2] = math.cos(theta)
    m [3][3] = 1
    return m 

def make_rotY( theta ):
    theta = theta * 180/math.pi 
    m = new_matrix ()
    m [0][0] = math.cos(theta)
    m [0][2] = 0 - math.sin(theta)
    m [1][1] = 1 
    m [2][2] = math.cos(theta)
    m [2][0] = math.sin(theta)
    m [3][3] = 1
    return m 

def make_rotZ( theta ):
    theta = theta * 180/math.pi 
    m = new_matrix ()
    m [0][0] = math.cos(theta)
    m [1][0] = math.sin(theta)
    m [0][1] = 0 - math.sin(theta)
    m [1][1] = math.cos(theta)
    m [2][2] = 1
    m [3][3] = 1
    return m

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ): # opposite?
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
    for c in range( len(matrix) ):
        for r in range( len(matrix) ):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    return matrix

def scalar_mult( matrix, x ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix [i][j] = matrix[i][j] * x
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = new_matrix (len(m1), len (m2[0]))
    for i in range (len(m1)): 
        for j in range (len (m2[i])):
            m [i][j] = m1 [i][0] * m2 [0][j] +  m1 [i][1] * m2 [1][j] +  m1 [i][2] * m2 [2][j] +  m1 [i][3] * m2 [3][j]
    m2 = m
    return m2


print (ident(new_matrix()))
print (make_translate(4,5,6))
print (make_scale(1,2,3))
