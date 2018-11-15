from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while (t < 1.00000000000000000000001):
        x0 = cx + r*math.cos(t*2*(math.pi))
        y0 = r*math.sin(t*2*(math.pi)) - cy + 500
        t += step
        x1 = cx + r*math.cos(t*2*(math.pi))
        y1 = r*math.sin(t*2*(math.pi)) - cy + 500
        add_edge( points, x0, y0, 0, x1, y1, 0 )
    return
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    if (curve_type == "hermite"):
        mx = generate_curve_coefs( x0, x1-x0, x2, x3-x2, curve_type )[0]
        my = generate_curve_coefs( y0, y1-y0, y2, y3-y2, curve_type )[0]
    elif (curve_type == "bezier"):
        mx = generate_curve_coefs( x0, x1, x2, x3, curve_type )[0]
        my = generate_curve_coefs( y0, y1, y2, y3, curve_type )[0]
    xa = mx[0]
    xb = mx[1]
    xc = mx[2]
    xd = mx[3]
    ya = my[0]
    yb = my[1]
    yc = my[2]
    yd = my[3]
    while (t < 1.0000000000000000000001):
        p0x = xa*t**3 + xb*t**2 + xc*t + xd
        p0y = ya*t**3 + yb*t**2 + yc*t + yd
        t += step
        p1x = xa*t**3 + xb*t**2 + xc*t + xd
        p1y = ya*t**3 + yb*t**2 + yc*t + yd
        add_edge( points, p0x, p0y, 0, p1x, p1y, 0 )
    return

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

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

