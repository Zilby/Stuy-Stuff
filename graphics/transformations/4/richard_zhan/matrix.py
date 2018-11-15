import math

def cos(x):
    return math.cos(math.radians(x))
def sin(x):
    return math.sin(math.radians(x))

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def identity():
    #nondestructive????
    return [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]
def translate(x,y,z):
    return [[0,0,0,x],
            [0,0,0,y],
            [0,0,0,z],
            [0,0,0,1]]
def scale(x,y,z):
    return [[x,0,0,0],
            [0,y,0,0],
            [0,0,z,0],
            [0,0,0,1]]
def rotz(t):
    return [[cos(t),-sin(t),0,0],
            [sin(t), cos(t),0,0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]
def roty(t):
    return [[cos(t),0,-sin(t),0],
            [0,1,0,0],
            [sin(t),0,cos(t),0],
            [0,0,0,1]]
def rotx(t):
    return [[1,0,0,0],
            [0,cos(t),-sin(t),0],
            [0,sin(t),cos(t),0],
            [0,0,0,1]]


def scalmult(c,m1):
    return [ [c * y for y in x] for x in m1 ]
def matmult(m1,m2):
    if len(m1[0]) != len(m2):
        print "Error: M1 row does not match M2 col"
    matrix = []
    for x in m1:
        place = []
        r = 0
        while r < len(m2[0]):
            total = 0
            c = 0
            while c < len(m2):
                total+=(x[c] * m2[c][r])
                c+=1
            place.append(total)
            r+=1
        matrix.append(place)
    return matrix
    

def matadd(m1,m2):
    return [[sum(y) for y in zip(x[0],x[1])] for x in zip(m1,m2)]



def print_matrix( matrix ):
    for x in matrix:
        s = str(x)
        s += ","
        print s
    


if __name__ == "__main__":
    m1 = [[3, 0, 4,0],
          [2, 7, 1,0],
          [6, 5, 1,0],
          [3, 4, 1,1]]
    m2 = [[2],[2],[2],[1]]
    matmult(m1,m2)
    m3 = [[1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]]
    print_matrix(m1)
    print_matrix(scalmult(4,m1))
