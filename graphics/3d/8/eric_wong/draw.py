from display import *
from matrix import *
import math

def add_box( points, x, y, z, w, h, d ):
    #front
    add_edge(points, x, y, z, x, y, z)
    add_edge(points, x+w, y, z, x+w, y, z)
    add_edge(points, x+w, y+h, z, x+w, y+h, z)
    add_edge(points, x, y+h, z, x, y+h, z)
    #back
    add_edge(points, x, y, z+d, x, y, z+d)
    add_edge(points, x+w, y, z+d, x+w, y, z+d)
    add_edge(points, x+w, y+h, z+d, x+w, y+h, z+d)
    add_edge(points, x, y+h, z+d, x, y+h, z+d)

def add_sphere( points, cx, cy, r ):
    spin = 0
    while (spin<=math.pi):
        circle = 0
        while (circle<=2*math.pi):
            x = cx + r*math.cos(2*math.pi*circle)
            y = cy + r*math.sin(2*math.pi*circle)*math.cos(math.pi*spin)
            z = r*math.sin(2*math.pi*circle)*math.cos(math.pi*spin)
            add_edge(points, x, y, z, x, y, z)
            circle = circle + .01
        spin = spin + .01

def add_torus( points, cx, cy, r1, r2 ):
    spin = 0
    while (spin<=2*math.pi):
        circle = 0
        while (circle<=2*math.pi):
            x = cx + math.cos(2*math.pi*spin)*(r1*math.cos(2*math.pi*circle)+r2)
            y = cy + r1*math.sin(2*math.pi*circle)
            z = math.sin(2*math.pi*spin)*(r1*math.cos(2*math.pi*circle)+r2)
            add_edge(points, x, y, z, x, y, z)
            circle = circle + .01
        spin = spin + .01

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r
    y0 = cy
    z0 = cz
    t=0
    while (t<=1.000001):
        x = r * math.cos(2*math.pi*t) + cx
        y = r * math.sin(2*math.pi*t) + cy
        z = z0
        add_edge(points, x0, y0, z0, x, y, z)
        x0 = x
        y0 = y
        z0 = z
        t = t + step

def cal_point(t, coef):
    return (coef[0][0]*t*t*t) + (coef[0][1]*t*t) + (coef[0][2]*t) + (coef[0][3])
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    if curve_type == "hermite":
        dxi = x1 - x0
        dxf = x3 - x2
        x_coef = generate_curve_coefs(x0, x2, dxi, dxf, curve_type)
        dyi = y1 - y0
        dyf = y3 - y2
        y_coef = generate_curve_coefs(y0, y2, dyi, dyf, curve_type)

    elif curve_type == "bezier":
        x_coef = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        y_coef = generate_curve_coefs(y0, y1, y2, y3, curve_type)

    while (t <= 1.0000001):
        x = cal_point(t, x_coef)
        y = cal_point(t, y_coef)
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t = t + step

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

