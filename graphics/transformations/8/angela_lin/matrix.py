import math

#makes a translation matrix given x, y, z
def make_translate( x, y, z ):
    return [ [ 1, 0, 0, 0 ],
             [ 0, 1, 0, 0 ], 
             [ 0, 0, 1, 0 ],
             [ x, y, z, 1 ]
            ]

#makes a dilation matrix given x, y, z
def make_scale( x, y, z ):
    return [ [ x, 0, 0, 0 ],
             [ 0, y, 0, 0 ], 
             [ 0, 0, z, 0 ],
             [ 0, 0, 0, 1 ]
           ]

#makes a rotation-in-x matrix given angle of rotation (in x-axis)
def make_rotX( theta ): 
    t = theta*math.pi/180
    return [ [ 1, 0, 0, 0 ],
             [ 0, math.cos(t), math.sin(t), 0 ], 
             [ 0, -1*math.sin(t), math.cos(t), 0 ],
             [ 0, 0, 0, 1 ]
           ]

#makes a rotation-in-y matrix given angle of rotation (in y-axis)
def make_rotY( theta ):
    t = theta*math.pi/180
    return [ [ math.cos(t), 0, math.sin(t), 0 ],
             [ 0, 1, 0, 0 ], 
             [ -1*math.sin(t), 0, math.cos(t), 0 ],
             [ 0, 0, 0, 1 ]
           ]
    
#makes a rotation-in-z matrix given angle of rotation (in z-axis)
def make_rotZ( theta ):
    t = theta*math.pi/180
    return [ [ math.cos(t), math.sin(t), 0, 0 ],
             [ -1*math.sin(t), math.cos(t), 0, 0 ], 
             [ 0, 0, 1, 0 ],
             [ 0, 0, 0, 1 ]
           ]
    
#creates a new 4x4 matrix
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#prints given matrix
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        #num of elements in each array; always 4
        for c in range( len(matrix) ):
            #num of points
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s
    
#returns a 4x4 identity matrix
def ident():
    return [
        [ 1, 0, 0, 0 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 1, 0 ],
        [ 0, 0, 0, 1 ]
]

#applies a scalar multiplication operation on given matrix and returns new matrix
def scalar_mult( matrix, x ):
    for c in range(len(matrix)):
        for r in range(4): #should always be 4 since each pt --> length 4
            matrix[c][r] *= x
    return matrix

#m1 * m2 -> m3
#cols: len(m)
#rows: len(m[0])
def matrix_mult( m1, m2 ):
    m = []
    if (len(m1) != len(m2[0])):
        print "cannot apply matrix multiplication"
    else:
        for r in range(len(m2)):
            l = [] #new, transformed pt
            for c in range(len(m2[0])):#always 4
                s = 0
                for i in range(len(m1)): #always 4
                    #print "m1[c][i]:"+str(m1[c][i])+","+"m2[r][i]:"+str(m2[r][i])
                    s += m1[c][i] * m2[r][i]
                l.append(s)
            m.append(l)
    return m

#tests:
if __name__ == "__main__":
    i = ident()
    
    b = new_matrix()
    b[1][2] = 1
    b.append([1,2,3,4])
    
    t = make_scale(5,6,7)
    
    print_matrix(b)
    print_matrix(t)
    mult = matrix_mult(t,b)
    print_matrix(mult)
