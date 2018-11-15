from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while(i + 1 < len(matrix)):
        draw_line(screen, matrix[i][0], matrix[i][1], matrix[i + 1][0], matrix[i + 1][1], color)
        #print("Point 1: (%d,%d)")%(matrix[i][0],matrix[i][1])
        #print("Point 2: (%d,%d)")%(matrix[i+1][0],matrix[i+1][1])
        i = i + 2

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
    x = x0
    y = y0
    if (x1 - x != 0):
        m = float(y1 - y) / float(x1 - x)
    else:
        m = 10
    if (x1 < x0):
        x = x1
        y = y1
        x1 = x0
        y1 = y0
    #print(m)
    if (m >= 0 and m <= 1):
        A = 2 * (y1 - y)
        B = -2 * (x1 - x)
        d = A + B * 0.5
        while(x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y = y + 1
                d = d + B
            x = x + 1
            d = d + A
    elif (m > 1):
        A = 2 * (y1 - y)
        B = -2 * (x1 - x)
        d = A * 0.5 + B
        while(y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x = x + 1
                d = d + A
            y = y + 1
            d = d + B
    elif (m < 0 and m >= -1):
        A = 2 * (y1 - y)
        B = -2 * (x1 - x)
        d = A + B * 0.5
        while(x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y = y - 1
                d = d - B
            x = x + 1
            d = d + A
    elif (m < -1):
        A = 2 * (y1 - y)
        B = -2 * (x1 - x)
        d = A + B * 0.5
        while(y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x = x + 1
                d = d + A
            y = y - 1
            d = d - B
