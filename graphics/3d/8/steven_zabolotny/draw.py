from display import *
from matrix import *
import math

def add_box(points, x, y, z, width, height, depth):
    #This makes the box with lines
    #add_edge(points, x, y, z, x + width, y, z)
    #add_edge(points, x, y, z, x, y + height, z)
    #add_edge(points, x, y, z, x, y, z + depth)
    #add_edge(points, x + width, y, z, x + width, y + height, z)
    #add_edge(points, x + width, y, z, x + width, y, z + depth)
    #add_edge(points, x, y + height, z, x + width, y + height, z)
    #add_edge(points, x, y + height, z, x, y + height, z + depth)
    #add_edge(points, x, y, z + depth, x + width, y, z + depth)
    #add_edge(points, x, y, z + depth, x, y + height, z + depth)
    #add_edge(points, x + width, y + height, z + depth, x, y + height, z + depth)
    #add_edge(points, x + width, y + height, z + depth, x + width, y, z + depth)
    #add_edge(points, x + width, y + height, z + depth, x + width, y + height, z)
    add_edge(points, x, y, z, x, y, z)
    add_edge(points, x + width, y, z, x + width, y, z)
    add_edge(points, x, y + height, z, x, y + height, z)
    add_edge(points, x, y, z + depth, x, y, z + depth)
    add_edge(points, x + width, y + height, z, x + width, y + height, z)
    add_edge(points, x + width, y, z + depth, x + width, y, z + depth)
    add_edge(points, x, y + height, z + depth, x, y + height, z + depth)
    add_edge(points, x + width, y + height, z + depth, x + width, y + height, z + depth)

def add_sphere(points, cx, cy, r):
    p = 0
    c = 0
    while (p <= 1):
        c = 0
        while (c <= 1):
            x = r * math.cos(2 * math.pi * c) + cx
            y = r * math.sin(2 * math.pi * c) * math.cos(math.pi * p) + cy
            z = r * math.sin(2 * math.pi * c) * math.sin(math.pi * p)
            add_edge(points, x, y, z, x, y, z)
            c = c + 0.01
        p = p + 0.01

def add_torus(points, cx, cy, r1, r2):
    p = 0
    c = 0
    while (p <= 1):
        c = 0
        while (c <= 1):
            x = math.cos(2 * math.pi * p) * (r1 * math.cos(2 * math.pi * c) + r2) + cx
            y = r1 * math.sin(2 * math.pi * c) + cy
            z = -math.sin(2 * math.pi * p) * (r1 * math.cos(2 * math.pi * c) + r2)
            add_edge(points, x, y, z, x, y, z)
            c = c + 0.01
        p = p + 0.01
    
def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    z0 = 0
    t = 0.0
    while t < 100:
        x = r * math.cos(t) + cx
        y = r * math.sin(t) + cy
        z = 0
        add_edge(points, x0, y0, z0, x, y, z)
        x0 = x
        y0 = y
        z0 = z
        t = t + step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if (curve_type == "bezier"):
        c = generate_curve_coefs([x0, y0, 0, 1], [x1, y1, 0, 1], [x2, y2, 0, 1], [x3, y3, 0, 1], 0)
        cx = c[0][0]
        cy = c[1][0]
        t = 0
        while (t < 1):
            x = cx[0] * math.pow(t, 3) + cx[1] * math.pow(t, 2) + cx[2] * t + cx[3]
            y = cy[0] * math.pow(t, 3) + cy[1] * math.pow(t, 2) + cy[2] * t + cy[3]
            add_edge(points, x0, y0, 0, x, y, 0)
            x0 = x
            y0 = y
            t = t + 0.01
    elif (curve_type == "hermite"):
        c = generate_curve_coefs([x0, y0, 0, 1], [x1, y1, 0, 1], [x2, y2, 0, 1], [x3, y3, 0, 1], 1)
        cx = c[0][0]
        cy = c[1][0]
        t = 0
        while (t < 1):
            x = cx[0] * math.pow(t, 3) + cx[1] * math.pow(t, 2) + cx[2] * t + cx[3]
            y = cy[0] * math.pow(t, 3) + cy[1] * math.pow(t, 2) + cy[2] * t + cy[3]
            add_edge(points, x0, y0, 0, x, y, 0)
            x0 = x
            y0 = y
            t = t + 0.01
            
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

