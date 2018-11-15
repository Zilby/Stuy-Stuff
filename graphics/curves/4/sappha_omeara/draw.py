from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    t = step
    x0 = cx + r
    y0 = cy
    for i in range(int (1.0 / step)):
        x1 = r * math.cos(2 * math.pi * t) + cx
        y1 = r * math.sin(2 * math.pi * t) + cy
        add_edge(points, x0, y0, 0, x1, y1, 0)
        x0 = x1
        y0 = y1
        t += step

def param(t, c):
    A = c[0]
    B = c[1]
    C = c[2]
    D = c[3]
    return ((A * math.pow(t, 3)) + (B * math.pow(t, 2)) + (C * t) + D)

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == 'hermite':
        dx0 = x1 - x0
        dx1 = x3 - x2
        dy0 = y1 - y0
        dy1 = y3 - y2
        cox = generate_curve_coefs(x0, x2, dx0, dx1, curve_type)
        coy = generate_curve_coefs(y0, y2, dy0, dy1, curve_type)
    if curve_type == 'bezier':
        cox = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        coy = generate_curve_coefs(y0, y1, y2, y3, curve_type)

    t = step
    for i in range(int (1.0/step)):
        x = param(t, cox)
        y = param(t, coy)
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step


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

