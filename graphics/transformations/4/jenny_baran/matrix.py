import math

def make_translate( x, y, z ):
#return matrix, which you then multiply trans_matrix by

def make_scale( x, y, z ):
#return matrix, which you then multiply trans_matrix by

def make_rotX( theta ):    
#return matrix, which you then multiply trans_matrix by

def make_rotY( theta ):
#return matrix, which you then multiply trans_matrix by

def make_rotZ( theta ):
#return matrix, which you then multiply trans_matrix by

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

def ident( trans_matrix ):
    for c in range( 4 ):
        for r in range( 4 ):
            if (c == r):
                trans_matrix[c][r] = 1
            else:
                trans_matrix[c][r] = 0

def scalar_mult( matrix, x ):
    for c in range( len(matrix) ):
        for r in range( 3 ):
            matrix[c][r] *= x=

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = []
    for c in range( len(m2) ): #point
        for r in range( len( m2[c] ) ): #coord
            m[c][r] = 0
            for i in range( len( m2[c] ) ): #iterate down col to sum
                m[c][r] += m1[i][r] * m2[c][r]
    return m