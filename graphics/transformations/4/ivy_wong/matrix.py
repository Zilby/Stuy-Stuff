import math

def make_translate( x, y, z ):
    trans = []
    trans.append([1,0,0,0])
    trans.append([0,1,0,0])
    trans.append([0,0,1,0])
    trans.append([x,y,z,1])
    return trans 

def make_scale( x, y, z ):
    scale = []
    scale.append([x,0,0,0])
    scale.append([0,y,0,0])
    scale.append([0,0,z,0])
    scale.append([0,0,0,1])
    return scale
    
def make_rotX( theta ):
    theta = math.radians(theta)
    rot = []
    rot.append([1,0,0,0])
    rot.append([0,math.cos(theta),math.sin(theta),0])
    rot.append([0,-math.sin(theta),math.cos(theta),0])
    rot.append([0,0,0,1])
    return rot 

def make_rotY( theta ):
    theta = math.radians(theta)
    rot = []
    rot.append([math.cos(theta),0,math.sin(theta),0])
    rot.append([0,1,0,0])
    rot.append([-math.sin(theta),0,math.cos(theta),0])
    rot.append([0,0,0,1])
    return rot

def make_rotZ( theta ):
    theta = math.radians(theta)
    rot = []
    rot.append([math.cos(theta),math.sin(theta),0,0])
    rot.append([-math.sin(theta),math.cos(theta),0,0])
    rot.append([0,0,1,0])
    rot.append([0,0,0,1])
    return rot

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix ) ):
        for c in range( len(matrix[0]) ):
            s+= str(matrix[r][c]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    ident = []
    ident.append([1,0,0,0])
    ident.append([0,1,0,0])
    ident.append([0,0,1,0])
    ident.append([0,0,0,1])
    return ident

def scalar_mult( matrix, x ):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] = x*matrix[r][c]
    return matrix

def matrix_mult( m1, m2 ):
    if len(m1) != len(m2[0]):
        print "THIS IS NOT ALLOWED. ABORTING."
        return
    
    m3 = new_matrix(len(m1),len(m2[0]))
    curr_row = 0
    val = 0
    while(curr_row < len(m1)): #loop through m1 rows
        for col in range(len(m1[0])):
            for curr_col in range(len(m2[0])): #loop through m2 cols
                val = m1[curr_row][col]*m2[col][curr_col]
                m3[curr_row][curr_col]+=val
        curr_row+=1
    return m3

def matrix_mult( m1, m2 ):
    if len(m1[0]) != len(m2):
        print "THIS IS NOT ALLOWED. ABORTING."
        return
    
    m3 = new_matrix(len(m1),len(m2[0]))
    curr_row = 0
    val = 0
    while(curr_row < len(m1)): #loop through m1 rows
        for col in range(len(m1[0])):
            for curr_col in range(len(m2[0])): #loop through m2 cols
                val = m1[curr_row][col]*m2[col][curr_col]
                m3[curr_row][curr_col]+=val
        curr_row+=1
    return m3
