from display import *
from matrix import *
import math


def add_torus (points, cx, cy, r1, r2, step):
    c = 0
    p = 0
    for i in range (int (1.0 / step) ):
        for j in range (int (1.0 / step )):
            x = math.cos(2 * math.pi * p) * ( r1 * math.cos(2 * math.pi * c) + r2) + cx
            y = r1 * math.sin(2 *  math.pi * c) + cy
            z = -math.sin(2 *  math.pi * p) * ( r1 * math.cos ( 2 *  math.pi * c) + r2)
            add_edge(points, x, y, z)
            c += step
        c = 0
        p+= step


def add_prism (points, x, y, z, w, h, d):
    add_edge(points, x, y, z)
    add_edge(points, x+w, y, z)
    add_edge(points, x, y-h, z)
    add_edge(points, x+w, y-h, z)
    add_edge(points, x, y, z-d)
    add_edge(points, x+w, y, z-d)
    add_edge(points, x, y-h, z-d)
    add_edge(points, x+w, y-h, z-d)


def add_sphere( points, cx, cy, cz, r, step ):
    c = 0
    p = 0
    for i in range (int (1.0 / step) ):
        for j in range (int (1.0 / step) ):
            x = r * math.cos(2 * math.pi * c) + cx
            y = r * math.sin(2 * math.pi * c) * math.cos(math.pi * p) + cy
            z = r * math.sin(2 * math.pi * c) * math.sin(math.pi * p) + cz
            add_edge(points, x, y, z)
            c += step
        c = 0
        p += step

def add_circle( points, cx, cy, cz, r, step ):
    t = step
    x0 = cx + r
    y0 = cy
    
    for i in range (int (1.0 / step) ):
        x = r * math.cos(2 * math.pi * t) + cx
        y = r * math.sin(2 * math.pi * t) + cy
        add_edge (points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step


def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == 'hermite':
        dx0 = x1 - x0
        dx1 = x3 - x2
        dy0 = y1 - y0
        dy1 = y3 - y0
        cx = generate_curve_coefs(x0, x2, dx0, dx1, curve_type)
        cy = generate_curve_coefs(y0, y2, dy0, dy1, curve_type)
    if curve_type == 'bezier':
        cx = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        cy = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    t = step
    for i in range ( int (1.0/step) ):
        x = param(t, cx)
        y = param (t, cy)
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step

def param ( t, cs ):
    a = cs[0]
    b = cs[1]
    c = cs[2]
    d = cs[3]
    return ( (a * math.pow(t,3)) + (b * math.pow(t,2)) + (c * t) + d )


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


def add_edge (matrix, x, y, z):
    add_point(matrix, x, y, z)
    add_point(matrix, x, y, z)

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

