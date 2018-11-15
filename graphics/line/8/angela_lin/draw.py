from display import *
from matrix import *

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    p = [ x, y, z, 1]
    matrix.append(p)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while (i < len(matrix)):
        p1 = matrix[i]
        p2 = matrix[i+1]
        draw_line(screen, p1[0], p1[1], p2[0], p2[1], color)
        i += 2

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x0 > x1):
        #since we always assume we're drawing L->R, switch
        draw_line(screen, x1, y1, x0, y0, color)
    else:
        x = x0
        y = y0
        a = 2*(y1-y0)
        b = (-2)*(x1-x0)
        if (float(x1-x0) == 0):
            #vertical line
            if (y0 > y1):
                y = y1
                y1 = y0
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
        else:
            m = float(y1-y0)/float(x1-x0)
            #Octant I and V
            if (m >= 0 and m < 1):
                d = a + b/2
                while (x <= x1):
                    plot(screen, color, x, y)
                    if (d > 0):
                        y += 1
                        d += b
                    x += 1
                    d += a
            #Octant II and VI
            elif (m >= 1):
                d = a/2 + b
                while (y <= y1):
                    plot(screen, color, x, y)
                    if (d < 0):
                        x += 1
                        d += a
                    y += 1
                    d += b
            #Octant III and VII
            elif ( m <= -1 ):
                d = a/2 - b
                while (y >= y1):
                    plot(screen, color, x, y)
                    if d > 0:
                        x += 1
                        d += a
                    y -= 1
                    d -= b
            #Octant IV and VIII
            elif ( 0 > m and m >= -1):
                d = a - b/2
                while (x <= x1):
                    plot(screen, color, x, y)
                    if (d < 0):
                        y -= 1
                        d -= b
                    x += 1
                    d += a

if __name__ == "__main__":
    screen = new_screen()
    color = [ 0, 255, 0 ]
    matrix = []
    z = 0
    draw_line(screen, 500, 500, 0, 0, color)
    save_ppm(screen, "test")
    #print_matrix(matrix)

    
