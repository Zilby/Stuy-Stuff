import math


def make_bezier():
    m = new_matrix()
    ident(m)
    m[0] = [-1, 3, -3, 1]
    m[1] = [3, -6, 3, 0]
    m[2] = [-3, 3, 0, 0]
    m[3] = [1, 0, 0, 0]
    return m


def make_hermite():
    m = new_matrix()
    ident(m)
    m[0] = [2, -2, 1, 1]
    m[1] = [-3, 3, -2, -1]
    m[2] = [0, 0, 1, 0]
    m[3] = [1, 0, 0, 0]
    return m


def generate_curve_coefs(p1, p2, p3, p4, t):
    if t == "bezier":
        m = make_bezier()
        matrix_mult(m, [[p1, p4, p2, p3]])
        return m
    elif t == "hermite":
        # Should use r0 and r1
        m = make_hermite()
        matrix_mult(m, [[p1, p2, p3, p4]])
        return m
    else:
        print "Bad curve type"


def make_translate(x, y, z):
    m = new_matrix()
    ident(m)
    m[3][0] = x
    m[3][1] = y
    m[3][2] = z
    return m


def make_scale(x, y, z):
    m = new_matrix()
    ident(m)
    m[0][0] = x
    m[1][1] = y
    m[2][2] = z
    return m


def make_rotX(theta):
    m = new_matrix()
    ident(m)
    m[1][1] = math.cos(theta)
    m[2][1] = -math.sin(theta)
    m[1][2] = math.sin(theta)
    m[2][2] = math.cos(theta)
    return m


def make_rotY(theta):
    ry = new_matrix()
    ident(ry)
    ry[0][0] = math.cos(theta)
    ry[2][0] = -math.sin(theta)
    ry[0][2] = math.sin(theta)
    ry[2][2] = math.cos(theta)
    return ry


def make_rotZ(theta):
    m = new_matrix()
    ident(m)
    m[0][0] = math.cos(theta)
    m[1][0] = -math.sin(theta)
    m[0][1] = math.sin(theta)
    m[1][1] = math.cos(theta)
    return m


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


def ident(matrix):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0


def scalar_mult(matrix, x):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            matrix[c][r] *= x


# m1 * m2 -> m2
def matrix_mult(m1, m2):
    product = new_matrix(4, 1)

    for c in range(len(m2)):
        for r in range(4):
            product[0][r] = m2[c][r]

        for r in range(4):
            m2[c][r] = m1[0][r] * product[0][0] + \
                m1[1][r] * product[0][1] + \
                m1[2][r] * product[0][2] + \
                m1[3][r] * product[0][3]
