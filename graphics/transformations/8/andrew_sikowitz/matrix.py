import math

def make_translate( x, y, z ):
    pass
def make_scale( x, y, z ):
    pass
    
def make_rotX( theta ):    
    pass
def make_rotY( theta ):
    pass
def make_rotZ( theta ):
    pass
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
    n = len(matrix)
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]
def scalar_mult( matrix, x ):
    return [[i*x for i in j] for j in matrix]
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m = len(m1)
    n = len(m2[0])
    l = len(m2) #same as len(m1[0])
    print reduce(lambda x,y: m1[0][x]*m2[x][0] + y, range(l))
    #return [[reduce(lambda k,y: m1[i][k]*m2[k][j]+y, range(l)) for i in range(m)] for j in range(n)]
