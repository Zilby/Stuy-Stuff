from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for i in range(len(matrix))[::2]:
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color)
        
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
    if (x1 >= x0):
        x = x0
        y = y0
        a = 2*(y1 - y0)
        b = -2*(x1 - x0)
        if (y1 >= y0):
            if x0 != x1 and 1. * (y1 - y0)/(x1 - x0) <= 1:
                d = a + b/2
                while (x <= x1):
                    plot(screen,color,x,y)
                    if d > 0:
                        y += 1
                        d += b
                    x += 1
                    d += a
            else:
                d = a/2 + b
                while (y <= y1):
                    plot(screen,color,x,y)
                    if d < 0:
                        x += 1
                        d += a
                    y += 1
                    d += b
        else:
            if x0 != x1 and 1. * (y1 - y0)/(x1 - x0) >= -1:
                d = a - b/2
                while (x <= x1):
                    plot(screen,color,x,y)
                    if d < 0:
                        y -= 1
                        d -= b
                    x += 1
                    d += a
            else:
                d = a/2 - b
                while (y >= y1):
                    plot(screen,color,x,y)
                    if d > 0:
                        x += 1
                        d += a
                    y -= 1
                    d -= b
    else:
        draw_line(screen,x1,y1,x0,y0,color)        
