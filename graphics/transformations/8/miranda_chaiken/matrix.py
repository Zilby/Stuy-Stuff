import math

def make_translate( x, y, z ):
    matrix=new_matrix()
    matrix = ident(matrix)
    matrix[3][0]=x
    matrix[3][1]=y
    matrix[3][2]=z
    return matrix


def make_scale( x, y, z ):
    matrix=new_matrix()
    ident(matrix)
    matrix[0][0]=x
    matrix[1][1]=y
    matrix[2][2]=z
    matrix[3][3]=1
    return matrix

    
def make_rotX( theta ):
    rad =math.radians(theta)
    matrix = new_matrix()
    ident(matrix)
    cos= math.cos(rad)
    sin =math.sin(rad)

    matrix[1][1] = cos
    matrix[2][1] = -sin
    matrix[1][2] = sin
    matrix[2][2] = cos
    return matrix

def make_rotY( theta ):
    rad =math.radians(theta)
    matrix = new_matrix()
    ident(matrix)
    matrix[0][0] = math.cos(rad)
    matrix[2][0] = -math.sin(rad)
    matrix[0][2] = math.sin(rad)
    matrix[2][2] = math.cos(rad)
    return matrix

def make_rotZ( theta ):
    rad =math.radians(theta)
    matrix = new_matrix()
    ident(matrix)
    matrix[0][0] = math.cos(rad)
    matrix[1][0] = -math.sin(rad)
    matrix[0][1] = math.sin(rad)
    matrix[1][1] = math.cos(rad)
    return matrix

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
    x=0;
    while x < len(matrix):
        y=0
        while y <len(matrix[x]):
            matrix[x][y]=0
            y+=1
                
        matrix[x][x]=1
        x+=1
    return matrix


def scalar_mult( matrix, s ):

    for x in range(0, len(matrix)):
        for y in range(0,len(matrix[x])):
            matrix[x][y]*=s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m=m2
    if len(m1) != len(m2[0]):
        #print len(m1)
        #print len(m2[0])
        #print "Not multipliable"
        return Null
    for x in range(0, len(m)):
        for y in range(0, len(m[x])):
            s=0
            for i in range(0, len(m2[x])):
                s+=m1[i][y]*m2[x][i]
            m[x][y]=s
    return m
'''
m= new_matrix()
t= make_translate(10,20,30)
s= make_scale(10,11,12)
x= make_rotX(90)
y= make_rotY(90)
z= make_rotZ(90)
print "Translate"
print_matrix(t)
print "Scale"
print_matrix(s)
print "RotX"
print_matrix(x)
print "RotY"
print_matrix(y)
print "RotZ"
print_matrix(z)

i=ident(new_matrix())
print "Identity"
print_matrix(i)
scalar_mult(i,2)
print "Identity *2"
print_matrix(i)

tester= [[1,2,0,1],[2, 5,2,1]]
print_matrix(tester)
mult = matrix_mult(t,tester)
print_matrix(mult)
'''
