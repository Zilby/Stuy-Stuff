from display import *
from matrix import *
import math

def add_torus( points, cx, cy, r1, r2, step ):
    p = 0
    c = 0
    cz = 0
    rn = int(1/step)
    for p in range(rn):
        for c in range(rn):
            x = math.cos(2*math.pi*p*step)*(r1*math.cos(2*math.pi*c*step)+r2)+cx
            y = r1*math.sin(2*math.pi*c*step) + cy
            z = -math.sin(2*math.pi*p*step)*(r1*math.cos(2*math.pi*c*step)+r2)+cz
            add_edge(points, x, y, z, x, y, z) 

def add_box( points, x, y, z, h, w, d, step):
    add_edge(points, x, y, z, x, y, z)
    add_edge(points, x+w, y, z, x+w, y, z)
    add_edge(points, x+w, y-h, z, x+w, y-h, z)
    add_edge(points, x, y-h, z, x, y-h, z)
    add_edge(points, x, y-h, z-d, x, y-h, z-d)
    add_edge(points, x, y, z-d, x, y, z-d)
    add_edge(points, x+w, y, z-d, x+w, y, z-d)
    add_edge(points, x+w, y-h, z-d, x+w, y-h, z-d)

def add_sphere( points, cx, cy, r, step ):
    p = 0
    c = 0
    cz = 0
    rn = int(1/step)
    for p in range(rn):
        for c in range(rn):
            x = r*math.cos(2*math.pi*c*step) + cx
            y = r*math.sin(2*math.pi*c*step)*math.cos(math.pi*p*step)+cy
            z = r*math.sin(2*math.pi*c*step)*math.sin(math.pi*p*step)+cz
            add_edge(points, x, y, z, x, y, z)

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    x = cx + math.cos(t)*r
    y = cy + math.sin(t)*r
    while t <= (1.0/step):
        x0 = x
        y0 = y
        x = cx + math.cos(2*math.pi*t*step)*r
        y = cy + math.sin(2*math.pi*t*step)*r
        add_edge(points, x0, y0, cz, x, y, cz)
        t += 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    z = 0
    
    xcoef = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoef = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    while t <= 1.0:
        x = xcoef[0] * t**3 + xcoef[1] * t**2 + xcoef[2] * t + xcoef[3]
        y = ycoef[0] * t**3 + ycoef[1] * t**2 + ycoef[2] * t + ycoef[3]
        add_edge(points, x0, y0, z, x, y, z)
        x0 = x
        y0 = y
        t+=step

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

