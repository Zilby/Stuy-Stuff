from display import *
from matrix import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of points
def draw_lines( matrix, screen, color ):
    for i in xrange(0,len(matrix),2):
        pt1 = matrix[i]
        pt2 = matrix[i+1]
        draw_line( screen, pt1[0], pt1[1], pt2[0], pt2[1], color)     

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    #flip in the negative half
    if x0 > x1:
        return draw_line(screen, x1, y1, x0, y0, color)
    x = x0
    y = y0
    dx = x1-x0
    dy = y1-y0
    A = 2*dy
    B = -2*dx
    if dx == 0:
        m = 42 #can't divide by 0, vertical
        if y > y1:
            tmp = y1
            y1 = y
            y = tmp
        while(y <= y1):
            plot(screen, color, x, y)
            y+=1
    else:
        m = float(dy)/dx
    if m >= 0 and m <= 1:
        #octant 1 
        d = A + B/2
        while(x <= x1):
            plot(screen, color, x, y)
            if d > 0:
                y+=1
                d+=B
            x+=1
            d+=A
    elif m > 1:
        #octant 2
        d = A/2 + B
        while(y <= y1):
            plot(screen, color, x, y)
            if d < 0:
                x+=1
                d+=A
            y+=1
            d+=B
    elif m < 0 and m > -1:
        #octant 8
        d = A - B/2
        while(x <= x1):
            plot(screen, color, x, y)
            if d > 0:
                y-=1
                d+=B
            x+=1
            d-=A
    else:
        #octant 7
        d = A/2 - B
        while(y >= y1):
            plot(screen, color, x, y)
            if d > 0:
                x+=1
                d+=A
            y-=1
            d-=B
