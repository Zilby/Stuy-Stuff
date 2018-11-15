from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while i < len(matrix):
        draw_line(screen,
                  matrix[i][0],
                  matrix[i][1],
                  matrix[i + 1][0],
                  matrix[i + 1][1],
                  color)
        i += 2

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0)
    add_point(matrix, x1, y1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):    #display.plot( screen, color, x0, y0 )
    if (x0 < x1): #make sure that everything is in the right order
        draw_line(screen, x1, y1, x0, y0, color)
    dy = y1 - y0
    dx = x1 - x0
    m = (dy + 0.0)/ dx #make it a double
    x = x0
    y = y0
    A = 2 * dy
    B = -2 * dx
    ##OCTANTS I AND IV
    if (y1 > y0 and m >= 0 and m <= 1):
        d = A + (B/2)
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += B # we add A later
            x += 1
            d += A
    ##OCTANTS II AND VI
    elif ( y1 > y0 and m > 1):
        d = (A/2) + B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += A
            y += 1
            d += B
    ##OCTANTS IV AND VIII
    elif (y0 > y1 and m < 0 and m >= -1):
        d = A - (B/2)
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= B
            x += 1
            d += A
    ##OCTANTS III AND VII
    elif (y0 > y1 and m < -1):
        d = (A/2) - B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += A
            y -= 1
            d -= B
    else: #something happened
        pass










