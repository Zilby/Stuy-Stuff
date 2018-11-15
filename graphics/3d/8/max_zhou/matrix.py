from rgbpoints import *
import line
from writer import *
import math
import time
from param import *

seed = time.time

#pt_matrix = []
master = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]
identity = [[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]


def add_edge(matrix, x1, y1, x2, y2, color=WHITE, color2=None, z1=0, z2=0):
    matrix.append(Point(x1, y1, z1, color))
    matrix.append(Point(x2, y2, z2, color2))

def plot_edge_lines(matrix, screen):
    for x in xrange(0, len(matrix), 2):
        pt1 = matrix[x]
        pt2 = matrix[x+1]
        line.plot_line(pt1.x, pt1.y, pt2.x, pt2.y, screen, pt1.color, pt2.color)
    

def mirror_matrix():
    for x in pt_matrix:
        pt_matrix_array.append(pt_to_matrix(x))
        print pt_to_matrix(x)
    return pt_matrix_array

def mirror_reverse(): #replace all this with function m_mult code with Points!
    new = []
    for x in pt_matrix_array:
        new.append(Point(x[0][0], x[1][0], x[2][0]))
    return new

def random_color():
    return [random.randint(127,255), random.randint(127,255), random.randint(127,255)]

def random_color2():
    return [random.randint(127,255), random.randint(127,255), random.randint(127,255)]


'''~~~~~~~MATH SECTION~~~~~~~~'''
def m_mult(m1, m2):
    height1 = len(m1)
    height2 = len(m2)
    width1 = len(m1[0])
    width2 = len(m2[0])
    if width1 != height2:
        print 0/0
    resultant = [ [0 for x in xrange(width2)] for y in xrange(height1)]
    for col in xrange(width2):
        for row in xrange(height1): #loop through every cell of the resulant matrix
            part = 0
            for x in xrange(width1):
                part += m1[row][x] * m2[x][col]
            resultant[row][col] = part
    return resultant

def m_mult_pt(t_matrix, pt):
    #print pt
    pt_matrix_coords = pt_to_matrix(pt)
    #print 'testing' + str(pt_matrix_coords)
    new_coords = m_mult(t_matrix, pt_matrix_coords)
    new_pt = pt
    new_pt.x = new_coords[0][0]
    new_pt.y = new_coords[1][0]
    new_pt.z = new_coords[2][0]
    #print new_pt.z
    return new_pt

def pt_to_matrix(point):
    resultant = [[point.x], [point.y], [point.z], [1]]
    #print resultant
    return resultant

def translation(dx, dy, dz):
    resultant = [[1, 0, 0, dx],
                 [0, 1, 0, dy],
                 [0, 0, 1, dz],
                 [0, 0, 0, 1]]
    #print resultant
    return resultant

def rot_x(theta):
    theta = math.radians(theta)
    resultant = [[1, 0, 0, 0,],
                 [0, math.cos(theta), -math.sin(theta), 0],
                 [0, math.sin(theta), math.cos(theta), 0],
                 [0, 0, 0, 1]]
    return resultant

def rot_y(theta):
    theta = math.radians(theta)
    resultant = [[math.cos(theta), 0, -math.sin(theta), 0],
                 [0, 1, 0, 0],
                 [math.sin(theta), 0, math.cos(theta), 0],
                 [0, 0, 0, 1]]
    return resultant

def rot_z(theta):
    theta = math.radians(theta)
    resultant = [[math.cos(theta), -math.sin(theta), 0, 0,],
                 [math.sin(theta), math.cos(theta), 0, 0,],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]]
    return resultant

def scale(scale_x, scale_y, scale_z):
    resultant = [[scale_x, 0, 0, 0],
                 [0, scale_y, 0, 0],
                 [0, 0, scale_z, 0],
                 [0, 0, 0, 1]]
    return resultant

def apply_transformations(pmatrix, t_matrix):
    resultant = []
    print t_matrix
    for x in pmatrix:
        resultant.append(m_mult_pt(t_matrix, x))

    #print 'resultant:' + str(resultant)
    #print resultant[5].z
    for p in resultant:
        p.round_coords()
    return resultant


if __name__ == "__main__":
    add_circle(200, 200, 100, pt_matrix, random_color(), random_color())

    #print pt_matrix
    t = translation(3,4,5)
    r = rot_x(60)
    s= scale(5,6,7)
    r2 = rot_y(60)
    t2 = translation(50,50,50)
    add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "HERMITE", random_color(), random_color()) #endpoint is 400, 100
    add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 300, 300
    add_curve(40, 100, 0, 0, 300, 300, 400, 100, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 400, 100
    master = m_mult(master, t)
    master = m_mult(master, s)
    master = m_mult(master, r)
    master = m_mult(master, t2)
    master = m_mult(master, r2)
    #print 'master:' + str(master)
    pt_matrix = apply_transformations()
    screen = [ [Point(x,y) for x in xrange(500)] for y in xrange(500)]
    plot_edge_lines(pt_matrix, screen)
    f = open('testing.ppm', 'wb')
    f.write("P3\n{0} {1}\n 255\n".format(500, 500)) #header
    plot_screen(f, screen)
    #print 'I hate this framework I built and didn\'t feel like making a parser right now =/ \nWhy did I even make Point objects terrible idea 0/10 would not do again\nI don\'t even get to keep the color data I put into point since I have to convert into array for the matrix'
    print 'Done!'
    f.close()
