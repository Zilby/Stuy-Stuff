import math


def makeBezier():
    t = new_matrix()
    t = ident(t)
    t[0] = [-1, 3, -3, 1]
    t[1] = [3, -6, 3, 0]
    t[2] = [-3, 3, 0, 0]
    t[3] = [1, 0, 0, 0]
    return t


def makeHermite():
    t = new_matrix()
    t = ident(t)
    t[0] = [2, -3, 0, 1]
    t[1] = [-2, 3, 0, 0]
    t[2] = [1, -2, 1, 0]
    t[3] = [1, -1, 0, 0]
    return t


def generateCurveCoefs(p1, p2, p3, p4, t):
    if t == "bezier":
        m = matrix_mult(makeBezier(), [[p1, p2, p3, p4]])
    elif t == "hermite":
        m = matrix_mult(makeHermite(), [[p1, p2, p3, p4]])
    return m


def translate( x, y, z ):
    matrix = ident(new_matrix())
    matrix[3][0] = x
    matrix[3][1] = y
    matrix[3][2] = z
    return matrix

def scale( x, y, z ):
    matrix = ident(new_matrix())
    matrix[0][0] = x
    matrix[1][1] = y
    matrix[2][2] = z
    return matrix

def rotateX( theta ):
    matrix = ident(new_matrix())
    angle = math.radians(theta)

    matrix[1][1] = math.cos(angle)
    matrix[2][1] = -math.sin(angle)
    matrix[1][2] = math.sin(angle)
    matrix[2][2] = math.cos(angle)
    return matrix

def rotateY( theta ):
    matrix = ident(new_matrix())
    angle = math.radians(theta)

    matrix[0][0] = math.cos(angle)
    matrix[0][2] = -math.sin(angle)
    matrix[2][0] = math.sin(angle)
    matrix[2][2] = math.cos(angle)
    return matrix

def rotateZ( theta ):
    matrix = ident(new_matrix())
    angle = math.radians(theta)

    matrix[0][0] = math.cos(angle)
    matrix[0][1] = -math.sin(angle)
    matrix[1][0] = math.sin(angle)
    matrix[1][1] = math.cos(angle)
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
    n = len(matrix)
    return [[1 if i==j else 0 for i in range(n)] for j in range(n)]


def scalar_mult( matrix, x ):
    return [[i*x for i in j] for j in matrix]


def matrix_mult(m1, m2):
    t = new_matrix(4, 1)
    for c in range(len(m2)):
        for r in range(4):
            t[0][r] = m2[c][r]
        for r in range(4):
            m2[c][r] = m1[0][r] * t[0][0] + m1[1][r] * t[0][1] + m1[2][r] * t[0][2] + m1[3][r] * t[0][3]
    return m2
