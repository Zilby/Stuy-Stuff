import math

def add_row(matrix,x,y,z,one):
    matrix.append([x,y,z,one])
    
def make_translate( x, y, z ):
    translate = []
    add_row(translate, 1,0,0,a)
    add_row(translate, 0,1,0,b)
    add_row(translate, 0,0,1,c)
    add_row(translate, 0,0,0,1)
    return translate

def make_scale( x, y, z ):
    scale = []
    add_row(scale, a,0,0,0)
    add_row(scale, 0,b,0,0)
    add_row(scale, 0,0,c,0)
    add_row(scale, 0,0,0,1)
    return scale

def make_rotX( theta ):
    theta = theta * (math.pi)/180
    print theta
    rotX = []
    add_row(rotX, 1,0,0,0)
    add_row(rotX, 0,math.cos(theta),-1*math.sin(theta),0)
    add_row(rotX, 0,math.sin(theta),math.cos(theta),0)
    add_row(rotX, 0,0,0,1)
    print_matrix(rotX)


def make_rotY( theta ):
    theta = theta * (math.pi)/180
    print theta
    rotY = []
    add_row(rotY, math.cos(theta),0,-1*math.sin(theta),0)
    add_row(rotY, 0,1,0,0)
    add_row(rotY, math.sin(theta),0,math.cos(theta),0)
    add_row(rotY, 0,0,0,1)
    print_matrix(rotY)
    return rotY

def make_rotZ( theta ):
    #theta is always in degress -> always convert to radians
    theta = theta * (math.pi)/180
    print theta
    rotZ = []
    add_row(rotZ, math.cos(theta),-1*math.sin(theta),0,0)
    add_row(rotZ, math.sin(theta),math.cos(theta),0,0)
    add_row(rotZ, 0,0,1,0)
    add_row(rotZ, 0,0,0,1)
    print_matrix(rotZ)
    return rotZ

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
    #### NOT general!!!
    me = []
    add_row(me,1,0,0,0)
    add_row(me,0,1,0,0)
    add_row(me,0,0,1,0)
    add_row(me,0,0,0,1)
    matrix = me
    print_matrix(matrix)
    return matrix
    pass
   
def scalar_mult( matrix, x ):

    
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    print_matrix(m1)
    print "\n"
    print_matrix(m2)
    ans = []
    
    #check that row and col match
    #Assume matrix is created correctly (as in every row has same number of elements)
    if len(m1) == len(m2[0]):
        # if # of elements in row of m1 is equal to # elements in (1st) column of m2
        c2 = 0 # column of m2, row of m1
        while c2 < len(m2):
            summy = 0
            ansrow = []
            r2 = 0 #row of m2, column of m1
            while r2 < len(m2[0]) : #assume matrices are placed in correctly (as in all eclosed with each row and column of equal length)
                summy += m1[r2][c2]*m2[c2][r2]
                print m1[r2][c2], m2[c2][r2], summy
                r2 += 1
            ansrow.append(summy)
            c2 += 1
        ans.append(ansrow)
        print ansrow
       


            
                
        print "ANS : "
        print_matrix(ans)
      
    else:
        print "ERROR, these MATRIXES cannot be multiplied together"
        print_matrix(m1)
        print_matrix(m2)
        

        
