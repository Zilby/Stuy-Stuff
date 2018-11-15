import math

def make_translate( x, y, z ):
    return [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]
    
def make_scale( x, y, z ):
    return [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    
def make_rotX( theta ):    
    return [[1, 0, 0, 0], [0, math.cos(math.radians(theta)), -math.sin(math.radians(theta)), 0], [0, math.sin(math.radians(theta)), math.cos(math.radians(theta)), 0], [0, 0, 0, 1]]

def make_rotY( theta ):
    return [[math.cos(math.radians(theta)), 0, -math.sin(math.radians(theta)), 0], [0, 1, 0, 0], [math.sin(math.radians(theta)), 0, math.cos(math.radians(theta)), 0], [0, 0, 0, 1]]

def make_rotZ( theta ):
    return [[math.cos(math.radians(theta)), -math.sin(math.radians(theta)), 0, 0], [math.sin(math.radians(theta)), math.cos(math.radians(theta)), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    
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
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            if (r == c):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    
def scalar_mult( matrix, x ):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            matrix[c][r] = matrix[c][r] * x
    
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if (len(m1[0]) == len(m2)):
        matrix = new_matrix(len(m2[0]), len(m1))
        for r in range(len(m1)):            
            for i  in range(len(m2[0])):
                sum = 0
                for c in range(len(m2)):
                    #print("%d * %d")%(m1[r][c], m2[c][i])
                    sum = sum + m1[r][c] * m2[c][i]
                matrix[r][i] = sum
        return matrix
