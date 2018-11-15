from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix), 2):
        a = matrix[i]
        b = matrix[i+1]
        draw_line(screen, a[0], a[1], b[0], b[1], color)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0)
    add_point(matrix,x1,y1)
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    m = [x,y,z,1]
    matrix.append(m)

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x1 < x0):
        draw_line (screen, x1, y1, x0, y0, color)
    dy = y1-y0
    dx = x1-x0
    if (dx != 0):
        m = (dy + 0.0)/dx
        x = x0
        y = y0
        A = 2 * dy
        B = -2 * dx
        if (y1 > y0 and 0 < m and m <= 1):
            d = A + (B/2)
            while (x <= x1 ):
                plot (screen, color, x, y)
                if ( d > 0 ):
                    y += 1
                    d+=B
                x += 1
                d+= A
        elif (y1 > y0 and 1 < m):
            d = (A/2) + B
            while (y <= y1):
                plot( screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += A
                y += 1
                d += B
        elif (y0 > y1 and 0 > m and m >= -1):
            d = A - (B/2)
            while (x <= x1):
                plot (screen, color, x, y)
                if (d<0):
                    y -= 1
                    d -= B
                x += 1
                d += A
        elif (y0 > y1 and -1 > m):
            d = (A/2) - B
            while (y >= y1):
                plot (screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += A
                y -= 1
                d -= B
