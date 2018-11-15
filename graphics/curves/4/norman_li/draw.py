from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    # Inital Variables
    x0 = cx + r
    y0 = cy

    t = step

    # Loop
    for i in range( int(10.0 / step) ):
        # Points to Draw
        x1 = circle_param_x( cx, r, t )
        y1 = circle_param_y( cy, r, t )

        # Add to Edge Matrix
        add_edge( points, x0, y0, cz, x1, y1, cz )

        # Set Variables
        x0 = x1
        y0 = y1
        t += step

# Circle X-Coordinate Parametric Function
def circle_param_x(cx, r, t):
    return cx + math.cos( 2 * math.pi * t ) * r

# Circle Y-Corrdinate Parametric Function
def circle_param_y(cy, r, t):
    return cy + math.sin( 2 * math.pi * t ) * r

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    # Intialize Variables
    if ( curve_type == "bezier" ):
        x_cofs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
        y_cofs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]
    else:
        x_cofs = generate_curve_coefs(x0, x2, x1 - x0, x3 - x2, curve_type)[0]
        y_cofs = generate_curve_coefs(y0, y2, y1 - y0, y3 - y2, curve_type)[0]

    t = step

    # Loop
    for i in range( int(10.0 / step) + 1 ):
        x1 = ( x_cofs[0] * (t ** 3) ) + ( x_cofs[1] * (t ** 2) ) + ( x_cofs[2] * t ) + x_cofs[3]
        y1 = ( y_cofs[0] * (t ** 3) ) + ( y_cofs[1] * (t ** 2) ) + ( y_cofs[2] * t ) + y_cofs[3]

        add_edge( points, x0, y0, 0, x1, y1, 0 )

        x0 = x1
        y0 = y1
        t += step

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p += 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

