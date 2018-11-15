from display import *
from matrix import *
import math

#xyz represent top-left-front vertex
def add_rect_prism(points, x, y, z, width, height, depth):
    add_point(points, x, y, z) #top-left-front
    add_point(points, x, y+height, z)
    add_point(points, x, y, z+depth)
    add_point(points, x, y+height, z)
    add_point(points, x+width, y+height, z)
    add_point(points, x+width, y+height, z+height)
    add_point(points, x+width, y, z)
    add_point(points, x+width, y, z+height)

def add_sphere( points, cx, cy, r):
    step = 0.1
    p = 0
    while (p <= 1.001):
        t = 0
        while (t <= 1.001):
            theta = 2 * math.pi * t
            thetap = math.pi * p
            x = cx + r  * math.cos(theta)
            y = cy + r * math.sin(theta) * math.cos(thetap)
            z = r * math.sin(theta) * math.sin(thetap)
            add_point( points, x, y, z )
            t += 0.01
        p += 0.01

def add_torus(points, cx, cy, r1, r2):
    p = 0
    while (p <= 1.001):
        t = 0
        while (t <= 1.001):
            thet = 2 * math.pi * t
            thep = 2 * math.pi * p
            x = cx + math.cos(thep) * (r1 * math.cos(thet) + r2)
            y = cy + r1 * math.sin(thet)
            z = math.sin(thep) * (r1 * math.cos(thet) + r2)
            add_point(points, x, y, z)
            t += 0.01
        p += 0.01
  
#adds circle to edge matrix
def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    x = cx + r #prevent awkward line
    y = cy
    z = 0
    while (t <= 1.00001):
        theta = (2 * t * math.pi)
        x1 = cx + r * math.cos(theta)
        y1 = cy + r * math.sin(theta)
        add_point(points, x, y, z)
        x = x1
        y = y1
        t += .00001
            
#if h: add a hermite curve to edge matrix
#if b: add a bezier curve to edge matrix
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    z = 0
    if curve_type == "hermite":
        d_x1 = x1 - x0
        d_x2 = x3 - x2
        d_y1 = y1 - y0
        d_y2 = y3 - y2
        xs = generate_curve_coefs(x0, x2, d_x1, d_x2, curve_type)
        ys = generate_curve_coefs(y0, y2, d_y1, d_y2, curve_type)
   
    elif curve_type == "bezier":
        xs = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        ys = generate_curve_coefs(y0, y1, y2, y3, curve_type)

    xs = xs[0]
    ys = ys[0]
   
    while (t <= 1.0001):
        x = xs[0]*math.pow(t, 3) + xs[1]*math.pow(t, 2) + xs[2]*t + xs[3]
        y = ys[0]*math.pow(t, 3) + ys[1]*math.pow(t, 2) + ys[2]*t + ys[3]
        add_edge(points, x0, y0, z, x, y, z)
        x0 = x
        y0 = y
        t += 0.001

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

