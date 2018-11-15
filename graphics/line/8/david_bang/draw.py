from display import *
from matrix import *

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x1>= x0):
        xa = x0
        xb = x1
        ya = y0
        yb = y1
    else:
        xa = x1
        xb = x0
        ya = y1
        yb = y0
    a = 2* (yb-ya)
    b = -2 * (xb-xa)
    if (float(xb-xa) == 0):
        m = 1
        
    else:
        m = float(yb - ya)/float(xb - xa)
    if (yb >= ya):
        if xa != xb and m <= 1:
            d = a + b/2
            while (xa <= xb):
                plot(screen,color,xa,ya)
                if d > 0:
                    ya += 1
                    d += b
                xa += 1
                d += a
        else:
            d = a/2 + b
            while (ya <= yb):
                plot(screen,color,xa,ya)
                if d < 0:
                    xa += 1
                    d += a
                ya += 1
                d += b
    else:
        if xa != xb and m >= -1:
            d = a - b/2
            while (xa <= xb):
                plot(screen,color,xa,ya)
                if d < 0:
                    ya -= 1
                    d -= b
                xa += 1
                d += a
        else:
            d = a/2 - b
            while (ya >= yb):
                plot(screen,color,xa,ya)
                if d > 0:
                    xa += 1
                    d += a
                ya -= 1
                d -= b
    return screen
                                                
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point (matrix, x0, y0, z0)
    add_point (matrix, x1, y1, z1)
    return matrix
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append ([x,y,z,1])
    return matrix

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for x in range(len(matrix))[::2]:
        draw_line(screen, matrix[x][0], matrix[x][1], matrix[x + 1][0], matrix[x + 1][1], color)
            
    
        
