from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while (i<len(matrix)):
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color)
        i += 2

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])
    #print_matrix(matrix)

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    #reverse points if needed
    if (x1 < x0):
        draw_line (screen, x1, y1, x0, y0, color)

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    if (B != 0):
        m = (y+0.0-y1)/(x-x1)
        #octant 1/5
        if (m >= 0 and m <= 1):
            d = A + (B/2)
            while (x <= x1):
                plot( screen, color, x, y)
                if (d > 0):
                    y+=1
                    d+=B
                x+=1
                d+=A
        #octant 2/6
        elif (m > 1):
            d = A - (B/2)
            while ( y <= y1 ):
                plot( screen, color, x, y)
                if (d < 0):
                    x+=1
                    d+=A
                y+=1
                d+=B
        #octant 3/7
        elif (m < -1):
            d = (A/2) - B
            while (y >= y1):
                plot (screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += A
                y -= 1
                d -= B
        #octant 4/8
        elif (m >= -1):
            d = A - (B/2)
            while (x <= x1):
                plot (screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= B
                x += 1
                d += A
    else:
        if (y0 > y1):
            y = y1
            y1 = y0
        while (y <= y1):
            plot(screen, color, x, y)
            y += 1
