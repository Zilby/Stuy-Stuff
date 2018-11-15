import math

#matrix[row][col]
def make_translate( x, y, z ):
    m = new_matrix()
    ident(m)
    m [0][3] = x
    m [1][3] = y
    m [2][3] = z
    return m

def make_scale( x, y, z ):
    m = new_matrix()
    ident(m)
    m [0][0] = x
    m [1][1] = y
    m [2][2] = z
    return m
    
def make_rotX( theta ):    
    m = new_matrix()
    ident(m)
    m [0][0] = math.cos(theta)
    m [0][1] = math.sin(theta) * -1
    m [1][0] = math.sin(theta)
    m [1][1] = math.cos(theta)
    return m

def make_rotY( theta ):
    return 

def make_rotZ( theta ):
    return

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix ) ):
        for c in range( len(matrix[0]) ):
            s+= str(matrix[r][c]) + ' '
        s+= '\n'
    print s

 def ident( matrix ):
    i = 0
    while i < 4:
        matrix [i][i] = 1
        i+=1
        
def scalar_mult( matrix, x ):
    i = 0
    j = 0
    while i < len (matrix):
        while j < len (matrix[i]):
            matrix [i][j] = matrix [i][j] * x
            j+=1
        j = 0
        i+=1


#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    return
    
m = new_matrix()
ident (m)
m = make_scale (3, 4, 5)
print_matrix(m)
