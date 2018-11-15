from display import *
from matrix import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i = 0
    while ( i < len(matrix) ):
        draw_line( screen,
                   matrix[i][0],
                   matrix[i][1],
                   matrix[i+1][0],
                   matrix[i+1][1],
                   color )
        i += 2


#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append( [ x, y, z, 1 ] )

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    slope = ( 1.0 * ( y1 - y0 ) ) / ( x1 - x0 )
    if ( slope > 0 and slope <= 1 ):
        octant_one( screen, x0, y0, x1, y1, color )
    elif ( slope > 1 ):
        octant_two( screen, x0, y0, x1, y1, color )
    elif ( slope < -1 ):
        octant_three( screen, x0, y0, x1, y1, color )
    else:
        octant_four( screen, x0, y0, x1, y1, color )

#def octant_one(x0,y0,x1,y1):
def octant_one( screen, x0, y0, x1, y1, color ):
    A = 2 * ( y1 - y0 )
    B = -2 * ( x1 - x0 )
    d = A + B/2
    x = x0
    y = y0
    while ( x <= x1 ):
        #print "(" + str(x) + ", " + str(y) + ")\n"
        plot( screen, color, x, y )
        if ( d > 0 ):
            y += 1
            d += B
        x += 1
        d += A

#def octant_two(x0,y0,x1,y1):
def octant_two( screen, x0, y0, x1, y1, color ):
    A = 2 * ( y1 - y0 )
    B = -2 * ( x1 - x0 )
    d = A/2 + B
    x = x0
    y = y0
    while ( y <= y1 ):
        #print "(" + str(x) + ", " + str(y) + ")\n"
        plot( screen, color, x, y )
        if ( d < 0 ):
            x += 1
            d += A
        y += 1
        d += B

#def octant_three(x0,y0,x1,y1):
def octant_three( screen, x0, y0, x1, y1, color ):
    A = 2 * ( y1 - y0 )
    B = -2 * ( x1 - x0 )
    d = A/2 - B
    x = x0
    y = y0
    while ( y >= y1 ):
        #print "(" + str(x) + ", " + str(y) + ")\n"
        plot( screen, color, x, y )
        if ( d > 0 ):
            x += 1
            d += A
        y -= 1
        d -= B

#def octant_four(x0,y0,x1,y1):
def octant_four( screen, x0, y0, x1, y1, color ):
    A = 2 * ( y1 - y0 )
    B = -2 * ( x1 - x0 )
    d = A - B/2
    x = x0
    y = y0
    while ( x <= x1 ):
        #print "(" + str(x) + ", " + str(y) + ")\n"
        plot( screen, color, x, y )
        if ( d < 0 ):
            y -= 1
            d -= B
        x += 1
        d += A


#### TESTING ####
'''
print "o1\n"
octant_one( 0, 0, 8, 4 )
print "o2\n"
octant_two( 0, 0, 4, 8 )
print "o3\n"
octant_three( 0, 0, 4, -8 )
print "o4\n"
octant_four( 0, 0, 8, -4 )
'''