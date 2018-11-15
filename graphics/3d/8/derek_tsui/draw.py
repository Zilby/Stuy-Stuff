from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r
    y0 = cy
    t = 0
    while (t <= 1.01):
        theta = (2 * t * math.pi)
        x1 = cx + r * math.cos(theta)
        y1 = cy + r * math.sin(theta)
        add_edge(points, x0, y0, 0, x1, y1, 0)
        x0 = x1
        y0 = y1
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    xs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    ys = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    while (t <= 1.01):
        #at^3 + bt^2 + ct + d
        x = xs[0]*math.pow(t, 3) + xs[1]*math.pow(t, 2) + xs[2]*t + xs[3]
        y = ys[0]*math.pow(t, 3) + ys[1]*math.pow(t, 2) + ys[2]*t + ys[3]
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step

def add_prism( points, x, y, z, w, h, d ):
    add_edge(points, x, y, z, x, y, z)
    add_edge(points, x+w, y, z, x+w, y, z)
    add_edge(points, x, y+h, z, x, y+h, z)
    add_edge(points, x, y, z+d, x, y, z+d)
    add_edge(points, x+w, y+h, z, x+w, y+h, z)
    add_edge(points, x+w, y, z+d, x+w, y, z+d)
    add_edge(points, x, y+h, z+d, x, y+h, z+d)
    add_edge(points, x+w, y+h, z+d, x+w, y+h, z+d)

def add_sphere( points, x, y, r):
    t1 = 0 #sphere
    cx = x
    cy = y
    while (t1 <= 1):
        t2 = 0 #circle
        while (t2 <= 1):
            rad_p = math.pi * t1
            rad_c = 2 * math.pi * t2
            x = cx + r  * math.cos(rad_c)
            y = cy + r * math.sin(rad_c) * math.cos(rad_p)
            z = r * math.sin(rad_c) * math.sin(rad_p)
            add_edge(points,x,y,z,x,y,z)
            t2 += 0.01
        t1 += 0.01

def add_torus( points, x, y, r1, r2):
    t1 = 0
    cx = x
    cy = y
    while (t1 <= 1):
        t2 = 0
        while (t2 <= 1):
            rad_p = 2 * math.pi * t1   #rotate
            rad_c = 2 * math.pi * t2   #make
            x = cx + math.cos(rad_p) * (r1 * math.cos(rad_c) + r2)
            y = cy + r1 * math.sin(rad_c)
            z = math.sin(rad_p) * (r1 * math.cos(rad_c) + r2)
            add_edge(points,x,y,z,x,y,z)
            t2 += 0.01
        t1 += 0.01

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
