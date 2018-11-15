import math

def make_translate( x, y, z ):
    m1 = [[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          [x,y,z,1]]
    return m1

def make_scale( x, y, z ):
    m1 = [[x,0,0,0],
          [0,y,0,0],
          [0,0,z,0],
          [0,0,0,1]]
    return m1
    
def make_rotX( theta ):
    rad = theta * math.pi / 180
    return ""

def make_rotY( theta ):
    rad = theta * math.pi / 180
    return ""

def make_rotZ( theta ):
    rad = theta * math.pi / 180
    return ""

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
        s += '\n'
    print s

def ident( matrix ):
    m1 = [[1,0,0,0],
          [0,1,0,0]
          [0,0,1,0],
          [0,0,0,1]]
    return m1

def scalar_mult( matrix, x ):
    m1 = make_translate(x,x,x)
    return matrix_mult(m1,matrix)

#m1 * m2 -> m2
#4x4 * 4x1 => 4*1 (result)
def matrix_mult( m1, m2 ):
    #I'm going to pretend I don't have to check if the matrix can be multiplied in the first place
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
                row.append(dot)
                r += 1
                c = -1
                dot = 0
            c += 1
        result.append(row)
        row = []
        r = 0
        x += 1        
    return result
            

m1 = make_translate(1,2,3)
m2 = [[10,10,10,1],[20,20,20,1]]
result = matrix_mult(m1,m2)
print_matrix(result)

