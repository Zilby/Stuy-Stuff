from display import *
from matrix import *
import math

def add_box( points, x, y, z, w, h, d ): #(x y z) = top left front corner
    add_edge(points, x, y, z, x, y, z) #for some reason must be edges not points
    add_edge(points, x, y-h, z, x, y-h, z)
    add_edge(points, x+w, y-h, z, x+w, y-h, z)
    add_edge(points, x+w, y, z, x+w, y, z)
    add_edge(points, x, y, z+d, x ,y, z+d)
    add_edge(points, x, y-h, z+d, x, y-h, z+d)
    add_edge(points, x+w, y-h, z+d, x+w, y-h, z+d)
    add_edge(points, x+w, y, z+d, x+w, y, z+d)

def add_sphere( points, cx, cy, r ):
    p = 0
    while p <= 1.00000001:
        t = 0
        while t <= 1.00000001:
            theta = 2 * math.pi * t
            phi = math.pi * p #this brings back odd memories
            x = cy + r * math.cos(theta)
            y = cy + r * math.sin(theta) * math.cos(phi)
            z = r * math.sin(theta) * math.sin(phi)
            add_edge(points, x, y, z, x, y, z)
            t += 0.025
        p += 0.025
            
def add_torus( points, cx, cy, r1, r2 ):
    p = 0
    while p <= 1.00000001:
        t = 0
        while t <= 1.00000001:
            theta = 2 * math.pi * t
            phi = 2 * math.pi * p
            x = cx + math.cos(phi) * (r1 * math.cos(theta) + r2)
            y = cy + r1 * math.sin(theta)
            z = math.sin(phi) * (r1 * math.cos(theta) + r2)
            add_edge(points, x, y, z, x, y, z)
            t += 0.025
        p += 0.025

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r
    y0 = cy
    t = 0
    while t <= 1.00000001:
        theta = 2 * math.pi * t
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        add_edge(points, x0, y0, cz, x, y, cz)
        x0 = x
        y0 = y
        t += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    # ok time to actually do this
    # decide what curve type it is
    #x_coef = 0
    #y_coef = 0
    if curve_type == "hermite":
        x_coef = generate_curve_coefs(x0, x2, x1-x0, x3-x2, curve_type)
        y_coef = generate_curve_coefs(y0, y2, y1-y0, y3-y2, curve_type)
    elif curve_type == "bezier":
        x_coef = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        y_coef = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    t = 0
    cx = x0
    cy = y0
    while t <= 1.00000001:
        xco = x_coef[0]
        yco = y_coef[0]
        x = xco[0] * t**3 + xco[1] * t**2 + xco[2] * t + xco[3]
        y = yco[0] * t**3 + yco[1] * t**2 + yco[2] * t + yco[3]
        add_edge(points, cx, cy, 0, x, y, 0)
        cx = x
        cy = y
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

