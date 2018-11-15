import math
from rgbpoints import *
import line
import matrix

def add_sphere(cx, cy, r, pmatrix, color=WHITE, color2=None):
    step = 5
    lim = 300
    p = 0
    c = 0
    if color2 != None:
        dred = color2[0] - color[0]
        dblue = color2[1] - color[1]
        dgreen = color2[2] - color[2]
        def colorf():
            delt = lim ** 2
            cur = float(p * c) / float(delt) * delt
             
            return [int((cur/delt) * dred + color[0]), int((cur/delt) * dblue + color[1]), int((cur/delt) * dgreen + color[2])]
    else:
        colorf = lambda: color

    while p <= lim:
    #for p in xrange(0, 100, step):
        #print 'hi'
        while c <= lim:
            x=r * math.cos(math.pi* 2/lim * c) + cx
            y=r * math.sin(math.pi* 2/lim * c) * math.cos(math.pi * 1/lim * p)+cy
            z=r * math.sin(math.pi* 2/lim * c) * math.sin(math.pi * 1/lim * p)
            #print y
            #matrix.pt_matrix.append(Point(x, y, z, color))
            matrix.add_edge(pmatrix,x,y,x,y,colorf(),z1=z,z2=z)
            #print "p: " + str(p)
            #print "c: " + str(c)
            c+=step
        p+=step
        c=0

def add_torus(cx, cy, cr, tr, pmatrix, color=WHITE, color2=None):
    step = 3
    lim = 300
    p = 0
    c = 0
    if color2 != None:
        dred = color2[0] - color[0]
        dblue = color2[1] - color[1]
        dgreen = color2[2] - color[2]
        def colorf():
            delt = lim ** 2
            cur = float(p * c) / float(delt) * delt
             
            return [int((cur/delt) * dred + color[0]), int((cur/delt) * dblue + color[1]), int((cur/delt) * dgreen + color[2])]
    else:
        colorf = lambda: color

    while p <= lim:
        while c <= lim:
            x = (cr * math.cos(math.pi* 2/lim * c) + tr) * math.cos(math.pi* 2/lim * p)  + cx
            y = (cr * math.sin(math.pi * 2/lim * c)) + cy
            z = (cr * math.cos(math.pi* 2/lim * c) + tr)* -math.sin(math.pi* 2/lim * p)
            matrix.add_edge(pmatrix,x,y,x,y,colorf(),z1=z,z2=z)
            c+=step
        p+=step
        c=0

def add_box(x,y,z,w,h,d, pmatrix, color=WHITE, color2=None):
    matrix.add_edge(pmatrix, x, y, x+w, y, color, color2, z, z) #bottom h line
    matrix.add_edge(pmatrix, x, y+h, x+w, y+h, color, color2, z, z) #top h line
    matrix.add_edge(pmatrix, x, y+h, x+w, y+h, color, color2, z-d, z-d) #top rear h line
    matrix.add_edge(pmatrix, x, y, x+w, y, color, color2, z-d, z-d) #bottom rear h line
    matrix.add_edge(pmatrix, x, y, x, y+h, color, color2, z, z) #left v line
    matrix.add_edge(pmatrix, x+w, y, x+w, y+h, color, color2, z, z) #right v line
    matrix.add_edge(pmatrix, x, y, x, y+h, color, color2, z-d, z-d) #left rear v line
    matrix.add_edge(pmatrix, x+w, y, x+w, y+h, color, color2, z-d, z-d) #right rear v line
    matrix.add_edge(pmatrix, x,y,x,y, color, color2, z, z-d) #lower left depth line
    matrix.add_edge(pmatrix, x+w,y,x+w,y, color, color2, z, z-d) #lower right dpeth line
    matrix.add_edge(pmatrix, x+w,y+h,x+w,y+h, color, color2, z, z-d) #upper right dpeth line
    matrix.add_edge(pmatrix, x,y+h,x,y+h, color, color2, z, z-d) #upper left dpeth line
