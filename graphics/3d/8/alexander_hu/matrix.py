import math

def make_bezier():
    t = [[-1,3,-3,1],
         [3,-6,3,0],
         [-3,3,0,0],
         [1,0,0,0]]
    return t
    
def make_hermite():
    t = [[2,-3,0,1],
         [-2,3,0,0],
         [1,-2,1,0],
         [1,-1,0,0]]
    return t

def generate_curve_coefs( p1, p2, p3, p4, curve_type ):
    meh = []
    if curve_type == 'bezier':
        blah = make_bezier()
        meh = matrix_mult(blah,[[p1,p2,p3,p4]])
    elif curve_type == 'hermite':
        blah = make_hermite()
        meh = matrix_mult(blah,[[p1,p2,p3,p4]])
    return meh

def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    return t

def make_scale( x, y, z ):
    s = new_matrix()
    ident(s)
    s[0][0] = x
    s[1][1] = y
    s[2][2] = z
    return s
    
def make_rotX( theta ):    
    rx = new_matrix()
    ident( rx )
    rx[1][1] = math.cos( theta )
    rx[2][1] = -1 * math.sin( theta )
    rx[1][2] = math.sin( theta )
    rx[2][2] = math.cos( theta )
    return rx

def make_rotY( theta ):
    ry = new_matrix()
    ident( ry )
    ry[0][0] = math.cos( theta )
    ry[2][0] = -1 * math.sin( theta )
    ry[0][2] = math.sin( theta )
    ry[2][2] = math.cos( theta )
    return ry

def make_rotZ( theta ):
    rz = new_matrix()
    ident( rz )
    rz[0][0] = math.cos( theta )
    rz[1][0] = -1 * math.sin( theta )
    rz[0][1] = math.sin( theta )
    rz[1][1] = math.cos( theta )
    return rz

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
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, x ):
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            matrix[c][r] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    result = []
    r = 0 #which row to go down
    c = 0 #which column to go down
    x = 0
    dot = 0
    while x < len(m2):
        row = []
        while r < len(m1):
            dot += m1[c][r] * m2[x][c]
            if c >= 3:
                row.append(dot) #because trying to read floats in a line drawer sucks. There are inaccuracies with this but... :/
                r += 1
                c = -1
                dot = 0
            c += 1
        result.append(row)
        row = []
        r = 0
        x += 1
    #print_matrix(result)
    return result

    '''
    
    t = new_matrix( 4, 1 )

    for c in range( len( m2 ) ):        
        
        for r in range(4):
            t[0][r] = m2[c][r]
            
        for r in range(4):
            m2[c][r] = m1[0][r] * t[0][0] + m1[1][r] * t[0][1] + m1[2][r] * t[0][2] + m1[3][r] * t[0][3]'''

#uh = matrix_mult(make_hermite(),[[1,1,1,1]])
#print_matrix(uh)
