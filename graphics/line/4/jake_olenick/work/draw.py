from display import *
from matrix import *
import math

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color):
    x = 0
    while (x < len(matrix)):
        draw_line(screen, matrix[x][0],matrix[x][1],matrix[x+1][0],matrix[x+1][1],color)
        x += 2
    

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):

    if(x1 >= x0):

        Dx = x1 - x0
        Dy = y1 - y0
        A = 2 * Dy
        B = -2 * Dx
        y = y0
        x = x0
        if(Dy <= Dx):
            if (Dy >= 0): #octant 1
                d = A + B/2
                while(x <= x1):
                    plot(screen,color,x,y)
                    if (d > 0):
                        y += 1
                        d+=B
                    x += 1
                    d += A
            elif (abs(Dy) < Dx): #octant 8
                d = A - B/2
                while(x <= x1):
                    plot(screen,color,x,y)
                    if (d > 0):
                        y -= 1
                        d+=B
                    x += 1
                    d -= A                  
            else: #octant 7
                d = A/2 - B
                while(y >= y1):
                    plot(screen,color,x,y)
                    if (d > 0):
                        x += 1
                        d+=A
                    y -= 1
                    d -=B
        else: #octant 2
            d = A/2 + B
            while(y <= y1):
                plot(screen,color,x,y)
                if (d < 0):
                    x += 1
                    d+=A
                y += 1
                d+=B
    else:
        draw_line(screen,x1,y1,x0,y0,color)
