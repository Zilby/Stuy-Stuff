from rgbpoints import *
from line import *
from writer import *
import math

pt_matrix = []
pt_matrix_array = []
master = [[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]]

def add_edge(matrix, x1, y1, x2, y2, color=WHITE, z1=0, z2=0):
    matrix.append(Point(x1, y1, z1, color))
    matrix.append(Point(x2, y2, z2, color))

def plot_edge_lines(matrix, screen):
    for x in xrange(0, len(matrix), 2):
        pt1 = matrix[x]
        pt2 = matrix[x+1]
        plot_line(pt1.x, pt1.y, pt2.x, pt2.y, screen)

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


'''~~~~~~~MATH SECTION~~~~~~~~'''
def m_mult(m1, m2):
    height1 = len(m1)
    height2 = len(m2)
    width1 = len(m1[0])
    width2 = len(m2[0])
    #print 'height1:' + str(height1)
    #print 'height2:' + str(height2)
    #print 'width1:' + str(width1)
    #print 'width2:' + str(width2)
    if width1 != height2:
        print 0/0 #throws exception
    resultant = [ [0 for x in xrange(width2)] for y in xrange(height1)]
    #print 'resultant: ' + str(resultant)
    for col in xrange(width2):
        for row in xrange(height1): #loop through every cell of the resulant matrix
            part = 0
            for x in xrange(width1):
                #print 'x: ' + str(x)
                #print 'col: ' + str(col)
                #print 'row: ' + str(row)
                part += m1[row][x] * m2[x][col]
            resultant[row][col] = part
            #print 'resultant: ' + str(resultant)
    return resultant

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

def apply_transformations():
    resultant = []
    for x in pt_matrix_array:
        resultant.append(m_mult(master, x))

    for x in resultant:
        for i in x:
            i[0] = int(round(i[0]))
    return resultant

if __name__ == "__main__":
    add_edge(pt_matrix, 0, 0, 20, 20)
    add_edge(pt_matrix, 0, 20, 20, 0)
    add_edge(pt_matrix, 20, 0, 20, 0)
    add_edge(pt_matrix, 0, 20, 0, 20)
    add_edge(pt_matrix, 20, 0, 0, 20)
    add_edge(pt_matrix, 0, 0, 20, 0)
    add_edge(pt_matrix, 0, 0, 0, 20)
    add_edge(pt_matrix, 0, 20, 20, 20)
    add_edge(pt_matrix, 20, 0, 20, 20)

    #print pt_matrix
    pt_matrix_array = mirror_matrix()
    #print pt_matrix_array
    t = translation(3,4,5)
    r = rot_x(60)
    s = scale(5,6,7)
    r2 = rot_y(60)
    t2 = translation(50,50,50)
    master =  m_mult(master, t)
    master = m_mult(master, s)
    master = m_mult(master, r)
    master = m_mult(master, t2)
    master = m_mult(master, r2)
    print master
    
    
    
    pt_matrix_array = apply_transformations()
    #print pt_matrix_array
    
    screen = [ [Point(x,y) for x in xrange(500)] for y in xrange(500)]
    pt_matrix = mirror_reverse()
    #print pt_matrix
    #print pt_matrix_array
    plot_edge_lines(pt_matrix, screen)
    #print screen
    f = open('testing.ppm', 'wb')
    f.write("P3\n{0} {1}\n 255\n".format(500, 500)) #header
    plot_screen(f, screen)
    print 'I hate this framework I built and didn\'t feel like making a parser right now =/ \nWhy did I even make Point objects terrible idea 0/10 would not do again\nI don\'t even get to keep the color data I put into point since I have to convert into array for the matrix'
    print 'Done!'
    f.close()
