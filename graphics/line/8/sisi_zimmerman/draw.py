from display import *
from matrix import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while( i < len(matrix) -1):
        draw_line(screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color)
        i+=2
    
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix , x0, y0, z0)
    add_point(matrix , x1, y1, z1)
        
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if(x0 > x1): #swap points
        xtemp = x0
        ytemp = y0
        x0 = x1
        y0 = y1
        x1 = xtemp
        y1 = ytemp

    octant = 0
    if( x0 == x1):
        octant = 2
    else:
        slope = float(y1 - y0) / float(x1-x0)
        if (slope >= 0 and slope <= 1):
            octant = 1
        elif (slope > 1):
            octant = 2
        elif ( slope < 0 and slope >= -1):
            octant = 8
        elif (slope < -1):
            octant = 7

    A = 2 * (y1 - y0)
    B = 2 * (x0 - x1)
    x = x0
    y = y0
    if( octant == 1):
        d = A + B/2
        while( x <= x1):
            plot(screen, color, x, y)
            if (d > 0) :
                y+=1
                d+= B 
            x+=1
            d += A
    elif (octant == 2):
        d = A/2 + B
        while( y <= y1 ):
            plot(screen, color, x, y)
            if(d < 0):
                x+=1
                d += A
            y+=1
            d+=B
    elif(octant == 8) :
        d = A - B/2
        while( x <= x1):
            plot(screen, color, x, y)
            if (d < 0) :
                y-=1
                d -= B
            x+=1
            d += A
    elif(octant == 7):
        d = A/2 + B
        while( y >= y1 ):
            plot(screen, color, x, y)
            if(d > 0):
                x+=1
                d += A
            y-=1
            d-=B
    

