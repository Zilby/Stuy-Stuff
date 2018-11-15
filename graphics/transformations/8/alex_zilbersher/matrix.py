import math

def make_translate( x, y, z ):
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [x, y, z, 1] ]

def make_scale( x, y, z ):
    return [ [x, 0, 0, 0],
             [0, y, 0, 0],
             [0, 0, z, 0],
             [0, 0, 0, 1] ]

def make_rotX( theta ):    
    o = theta*math.pi/180
    return [ [ 1, 0, 0, 0 ],
             [ 0, math.cos(o), math.sin(o), 0 ], 
             [ 0, -1*math.sin(o), math.cos(o), 0 ],
             [ 0, 0, 0, 1 ]
           ]

def make_rotY( theta ):
    o = theta*math.pi/180
    return [ [ math.cos(o), 0, math.sin(o), 0 ],
             [ 0, 1, 0, 0 ], 
             [ -1*math.sin(o), 0, math.cos(o), 0 ],
             [ 0, 0, 0, 1 ]
           ]
    
def make_rotZ( theta ):
    o = theta*math.pi/180
    return [ [ math.cos(o), math.sin(o), 0, 0 ],
             [ -1*math.sin(o), math.cos(o), 0, 0 ], 
             [ 0, 0, 1, 0 ],
             [ 0, 0, 0, 1 ]
           ]

def new_matrix(rows=4,cols=4):
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

def ident():
    return [ [1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1] ]

def scalar_mult( matrix, x ):
    m = make_scale(x, x, x)
    return matrix_mult( m, matrix )

def matrix_mult( m1, m2 ):
    m = []
    if (len(m1) != len(m2[0])):
        print "Matrix multiplication unapplicable"
    else:
        for r in range(len(m2)):
            l = []
            for c in range(len(m2[0])):
                s = 0
                for i in range(len(m1)):
                    s += m1[c][i] * m2[r][i]
                l.append(s)
            m.append(l)
    return m
