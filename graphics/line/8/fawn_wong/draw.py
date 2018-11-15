from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for x in range(len(matrix))[::2]:
        draw_line(screen, matrix[x][0], matrix[x][1], matrix[x + 1][0], matrix[x + 1][1], color)

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
    xi = x0
    xf = x1
    yi = y0
    yf = y1
    # other half, swap x and y
    if ( xi > xf ):
        xi = x1
        xf = x0
        yi = y1
        yf = x0
    A = 2 * (yf - yi)
    B = -2 * (xf - xi)
    if (float(xf - xi) == 0):
        #vertical
        m = 2
    else:
        m = float(yf - yi) / float(xf - xi)
    # Octant I
    if ( m < 1 and m >= 0 ):
        d = A + B/2
        while (xi <= xf): 
            plot(screen, color, xi, yi)
            if d > 0:
                yi += 1
                d += B
            xi += 1
            d += A
    # Octant II
    elif ( m >= 1 ):
        d = A/2 + B
        while (yi <= yf):
            plot(screen, color, xi, yi)
            if d < 0:
                xi += 1
                d += A
            yi += 1
            d += B
    # Octant VII
    elif ( m <= -1 ):
        d = A/2 - B
        while (yi >= yf):
            plot(screen, color, xi, yi)
            if d > 0:
                xi += 1
                d += A
            yi -= 1
            d -= B
    # Octant VIII
    elif ( m > -1 and m <= 0 ):
        d = A - B/2
        while (xi <= xf): 
            plot(screen, color, xi, yi)
            if d < 0:
                yi -= 1
                d -= B
            xi += 1
            d += A
        
    
        

