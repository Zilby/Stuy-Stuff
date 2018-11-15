from display import *
from matrix import *

#Go through matrix 2 entries at a time and call draw_line on each pair of points
def draw_lines(matrix,screen,color):
    print "drawing lines for ", matrix
    x = 0
    while x < len(matrix):
        draw_line(screen,matrix[x][0],matrix[x][1],matrix[x+1][0],matrix[x+1][1],color)
        x = x + 2

#Add the edge (x0,y0,z0) - (x1,y1,z1) to matrix
def add_edge(matrix,x0,y0,z0,x1,y1,z1):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    return matrix

#add the point (x,y,z) to matrix
def add_point(matrix,x,y,z=0):
    matrix.append([x,y,z,1])
    return matrix

#Plot all the pixels needed to draw line (x0,y0) - (x1,y1) to screen with color
def draw_line(screen,x0,y0,x1,y1,color):
    if x1 == x0:
        slope = 999999
    else:
        slope = float(y1-y0)/(x1-x0)
    #print "Slope is %d"%slope
    if slope>0 and slope<1:
        #print "Plotting in Octant 1"
        if (x1<x0):
            draw_line(screen,x1,y1,x0,y0,color)
        xi = x0
        yi = y0
        a = 2*(y1-y0)
        b = -2*(x1-x0)
        d = a + (b/2)
        while (xi<=x1):
            #print "Plotting in Octant 1"
            #print "Plotting (%d,%d)"%(xi,yi)
            plot(screen,color,xi,yi)
            if d>=0:
                yi = yi+1
                d = d+b
            xi = xi+1
            d = d+a
    elif slope>=1:
        #print "Plotting in Octant 2"
        if (y1<y0):
            draw_line(screen,x1,y1,x0,y0,color)
        xi = x0
        yi = y0
        a = 2*(y1-y0)
        b = -2*(x1-x0)
        d = (a/2) + b
        while (yi<=y1):
            #print "Plotting in Octant 2"
            #print "Plotting (%d,%d)"%(xi,yi)
            plot(screen,color,xi,yi)
            if d<=0:
                xi = xi+1
                d = d+a
            yi = yi+1
            d = d+b
    elif slope <=-1:
        #print "Plotting in Octant 3"
        if (y1<y0):
            draw_line(screen,x1,y1,x0,y0,color)
        xi = x0
        yi = y0
        a = 2*(y1-y0)
        b = -2*(x1-x0)
        d = (-a/2) + b
        while (yi<=y1):
            #print "Plotting in Octant 3"
            #print "Plotting (%d,%d)"%(xi,yi)
            plot(screen,color,xi,yi)
            if d>=0:
                xi = xi-1
                d = d-a
            yi = yi+1
            d = d+b
    else:
        #print "Plotting in Octant 4"
        if (x0<x1):
            draw_line(screen,x1,y1,x0,y0,color)
        xi = x0
        yi = y0
        a = 2*(y1-y0)
        b = -2*(x1-x0)
        d = -a + (b/2)
        while (xi>=x1):
            #print "Plotting in Octant 4"
            #print "Plotting (%d,%d)"%(xi,yi)
            plot(screen,color,xi,yi)
            if d<=0:
                yi = yi+1
                d = d+b
            xi = xi-1
            d = d-a
        
