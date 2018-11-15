from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while i < len(matrix):
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color)
        i+=2
        
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
    #check for direction of drawing
    if x1 < x0: #endpoint to the left
        xa = x1
        ya = y1
        xb = x0
        yb = y0
    else: #endpoint to the right
        xa = x0
        ya = y0
        xb = x1
        yb = y1
        
    A = 2 * (yb-ya)
    B = -2 * (xb-xa)

    #slope
    m = float(yb-ya)/float(xb-xa)

    # m >= 0
    if m >= 0:
        #fraction
        if m < 1:
            d = A + B/2
            while xa <= xb: ##
                plot(screen, color, xa, ya);
                if d > 0:
                    ya += 1
                    d += B
                xa += 1
                d += A
        #1 or greater
        else:
            d = A/2 + B
            while ya <= yb:
                plot(screen, color, xa, ya);
                if d < 0:
                    xa += 1
                    d += A
                ya += 1
                d += B
    #m <= 0
    else:
        #fraction
        if m >= -1:
            d = A - B/2
            while xa <= xb:
                plot(screen, color, xa, ya);
                if d < 0:
                    ya -= 1
                    d -= B
                xa += 1
                d += A
        #-1 or less
        else:
            d = A/2 - B ##
            while ya >= yb:
                plot(screen, color, xa, ya);
                if d > 0:
                    xa += 1
                    d += A
                ya -= 1
                d -= B
