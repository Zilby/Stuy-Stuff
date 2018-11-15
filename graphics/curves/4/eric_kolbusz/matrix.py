import math
import random

def make_translate(x, y, z):
    m = new_matrix()
    ident(m)
    l = [x,y,z]
    for i in range(len(m)-1):
        m[len(m)-1][i] = l[i]
    return m

def make_scale(x, y, z):
    m = new_matrix()
    for r in range(len(m)):
        m[r] = [[x,y,z,1][i] if i == r else 0 for i in range(len(m[r]))]
    return m

def make_rotX(theta):
    return make_rot(theta,[0,1,1,0],[0,-1,1,0],1)

def make_rotY(theta):
    return make_rot(theta,[1,0,1,0],[1,0,-1,0],2)

def make_rotZ(theta):
    return make_rot(theta,[1,1,0,0],[-1,1,0,0],3)

def make_rot(theta, l, l2, n):
    m = new_matrix()
    for r in range(len(m)):
        m[r] = [math.cos(math.radians(theta)) if (i == r and l[i] != 0) \
                else 1 if (i == r and l[i] == 0) \
                else l2[i]*math.sin(math.radians(theta)) if (i+r == len(m[r])-n and l2[i] != 0) \
                else 0 for i in range(len(m[r]))]
    return m

def make_bezier(): #im not doing a list comprehension thingy for this no way
    return [[-1, 3,-3, 1],
            [ 3,-6, 3, 0],
            [-3, 3, 0, 0],
            [ 1, 0, 0, 0]]

def make_hermite():
    return [[ 2,-3, 0, 1],
            [-2, 3, 0, 0],
            [ 1,-2, 1, 0],
            [ 1,-1, 0, 0]]

def generate_curve_coefs(p1, p2, p3, p4, t):
    if t == 'b':
        #matx, maty = make_bezier() actually gives an error because its too much work in one line lol
        matx = make_bezier()
        maty = make_bezier()
        x = [[p1[0], p2[0], p3[0], p4[0]]]
        y = [[p1[1], p2[1], p3[1], p4[1]]]
    if t == 'h':
        #matx, maty = make_hermite() same here
        matx = make_hermite()
        maty = make_hermite()
        x = [[p1[0], p3[0], p2[0]-p1[0], p4[0]-p3[0]]]
        y = [[p1[1], p3[1], p2[1]-p1[1], p4[1]-p3[1]]] 
    matrix_mult(matx,x)
    matrix_mult(maty,y)
    return [x,y]

def new_matrix(rows = 4, cols = 4):
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
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident(matrix):
    for r in range(len(matrix)):
        matrix[r] = [1 if i == r else 0 for i in range(len(matrix[r]))]

def scalar_mult(matrix, x):
    for r in range(len(matrix)):
        matrix[r] = [x*i for i in matrix[r]]

def fill_rand(matrix):
    for r in range(len(matrix)):
        matrix[r] = [random.randrange(1, 15) for i in range(len(matrix[r]))]

#m1 * m2 -> m2
'''
def matrix_mult(m1, m2):
    if len(m1) == len(m2[0]):
        ret = new_matrix(len(m1[0]), len(m2))
        for i in range(len(ret)):
            for j in range(len(ret[i])):
                msum = 0
                for k in range(len(m1[0])):
                    #print i, j, k
                    msum += m1[k][j] * m2[i][k]
                ret[i][j] = msum
    return ret
'''

def matrix_mult(m1, m2):
    #rip my code you will be missed
    t = new_matrix(4, 1)
    for c in range(len(m2)):        
        for r in range(4):
            t[0][r] = m2[c][r]
        for r in range(4):
            m2[c][r] = m1[0][r] * t[0][0] + m1[1][r] * t[0][1] + m1[2][r] * t[0][2] + m1[3][r] * t[0][3]

'''
m1 = new_matrix()
m2 = new_matrix()
fill_rand(m1)
fill_rand(m2)
print_matrix(m1)
print_matrix(m2)
m2 = matrix_mult(m1, m2)
print_matrix(m2)
'''

'''
m1 = new_matrix()
fill_rand(m1)
print_matrix(m1)
scalar_mult(m1, 2)
print_matrix(m1)
'''

'''
m1 = new_matrix()
fill_rand(m1)
print_matrix(m1)
ident(m1)
print_matrix(m1)
'''

'''
m1 = make_translate(8,32,13)
m2 = new_matrix(4,1)
fill_rand(m2)
m2[0][3] = 1
print_matrix(m1)
print_matrix(m2)
m2 = matrix_mult(m1, m2)
print_matrix(m2)
'''

'''
m1 = make_scale(8,32,13)
print_matrix(m1)
'''

'''              
m1 = make_rotX(30)
print_matrix(m1)
'''

'''
m1 = make_rotY(30)
print_matrix(m1)
'''

'''
m1 = make_rotZ(30)
print_matrix(m1)
#'''


