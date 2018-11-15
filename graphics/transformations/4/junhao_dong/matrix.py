import math

def make_translate( x, y, z ):

def make_scale( x, y, z ):

    
def make_rotX( theta ):    

def make_rotY( theta ):

def make_rotZ( theta ):

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

def scalar_mult( matrix, x ):

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):


