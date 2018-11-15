from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while i in range(len(matrix)):
        one = matrix[i]
        two = matrix[i+1]
        draw_line(screen, one[0], one[1], two[0], two[1], color)
        i+=2

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])
    
#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):

    if x0 < x1:
        xi = x0
        yi = y0
        xf = x1
        yf = y1
    else:
        xi = x1
        yi = y1
        xf = x0
        yf = y0
    dx = xf - xi
    dy = yf - yi
    if dx==0:
        m = "undefined"
    else:
        m = dy/dx
    A = 2*dy
    B = -2*dx

    #Octant 1    
    if m >= 0 and m <= 1:
        d = A + B/2
        
        while (xi<=xf):
            plot(screen, color, xi, yi)
            if (d>=0):
                yi+=1
                d+=B
            xi+=1
            d+=A

    #Octant 2
    elif m > 1 or m == "undefined":
        d = A/2 + B

        while (yi<=yf):
            plot(screen, color, xi, yi)
            if (d<=0):
                xi+=1
                d+=A
            yi+=1
            d+=B

    #Octant 3
    elif m < -1:
        d = A/2 - B

        while (yi>=yf):
            plot(screen, color, xi, yi)
            if (d<=0):
                xi+=1
                d+=A
            yi-=1
            d-=B
        
    #Octant 4
    elif m < 0 and m >= -1:
        d = A - B/2

        while(xi<=xf):
            plot(screen, color, xi, yi)
            if (d>=0):
                yi-=1
                d-=B
            xi+=1
            d+=A
   

