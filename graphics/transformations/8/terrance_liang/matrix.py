import math

def make_translate(x, y, z):
    translate = []
    translate.append([1,0,0,0])
    translate.append([0,1,0,0])
    translate.append([0,0,1,0])
    translate.append([x,y,z,1])
    return translate

def make_scale(x, y, z):
    dilate = []
    dilate.append([x,0,0,0])
    dilate.append([0,y,0,0])
    dilate.append([0,0,z,0])
    dilate.append([0,0,0,1])
    return dilate

def make_rotX(theta):
    rotateX = []
    angle = math.radians(theta)
    rotateX.append([1,0,0,0])
    rotateX.append([0,math.cos(angle),math.sin(angle),0])
    rotateX.append([0,-1*math.sin(angle),math.cos(angle),0])
    rotateX.append([0,0,0,1])
    return rotateX

def make_rotY(theta):
    rotateY = []
    angle = math.radians(theta)
    rotateY.append([math.cos(angle),0,math.sin(angle),0])
    rotateY.append([0,1,0,0])
    rotateY.append([-1*math.sin(angle),0,math.cos(angle),0])
    rotateY.append([0,0,0,1])
    return rotateY

def make_rotZ(theta):
    rotateZ = []
    angle = math.radians(theta)
    rotateZ.append([math.cos(angle),math.sin(angle),0,0])
    rotateZ.append([-1*math.sin(angle),math.cos(angle),0,0])
    rotateZ.append([0,0,1,0])
    rotateZ.append([0,0,0,1])
    return rotateZ

def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m

def print_matrix(matrix):
    s = ''
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            s += str(matrix[c][r]) + ' '
        s += '\n'
    print s
    return s
  
def ident(matrix):
    matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    return matrix
    
def scalar_mult(matrix, x):
    temp = matrix
    for i in matrix:
        for j in i:
            temp[i][j]=matrix[i][j]*x
    matrix = temp
    return matrix
    
#m1 * m2 -> m2
def matrix_mult (m1, m2):
    if (len(m1) != len(m2[0])):
        print "MATRIX ERROR"
        return
    temp = new_matrix(len(m1[0]),len(m2))
    for b in range(len(m1[0])):
        for a in range(len(m1)):
            for c in range(len(m2)):
                temp[c][b] += m1[a][b] * m2[c][a]
    m2 = temp
    return m2

translate = make_translate(1,2,3)
rotate = make_rotY(90)
print_matrix(translate)
matrix = [1,2,3,1],[2,3,1,1]
result = matrix_mult(translate,matrix)
print_matrix(result)
