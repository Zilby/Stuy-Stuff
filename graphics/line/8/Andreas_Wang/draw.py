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
    if (x0 > x1):
        draw_line(screen, x1, y1, x0, y0, color)
    else: 
        if (x0 == x1):
            for i in range(y0, y1 + 1):
                plot(screen, color, x0, i)
        else:
            A = 2 * (y1 - y0)
            B = -2 * (x1 - x0)
            m = -1.0 * A / B
            x = x0
            y = y0
                
#Octant I

            if ( m <= 1 and m >= 0):
                #print "Octant 1"
                #print x
                #print y
                d = A +  B/2
                while(x <= x1):
                    plot(screen, color, x,y)
                    if d > 0: 
                        y = y + 1
                        d  +=  B
                    x = x + 1
                    d = d + A

#Octant II
            elif ( m >= 1 ):
                d = A/2 + B
                while (y <= y1):
                    plot(screen, color, x, y)
                    if d < 0:
                        x += 1
                        d += A
                    y += 1
                    d += B
#Octant VII
            elif ( m <= -1 ):
                d = A/2 - B
                while (y >= y1):
                    plot(screen, color, x, y)
                    if d > 0:
                        x += 1
                        d += A
                    y -= 1
                    d -= B
#Octant VIII
            elif ( m > -1 and m < 0 ):
                d = A - B/2
                while (x <= x1): 
                    plot(screen, color, x, y)
                    if d < 0:
                        y -= 1
                        d -= B
                    x += 1
                    d += A
        
    




            

