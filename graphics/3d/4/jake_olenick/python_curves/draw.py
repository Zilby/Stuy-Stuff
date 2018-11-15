from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ): #points is the point matrix?
    t = 0
    x0 = cx + r
    y0 = cy
    t = 1
    while t <= (1.0 / step):
        x1 = cx + r*math.cos(2*math.pi*t*step)
        y1 = cy + r*math.sin(2*math.pi*t*step)
        add_edge(points,x0,y0,cz,x1,y1,cz)
        x0 = x1
        y0 = y1
        t += 1
                  

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    x_coefs = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    y_coefs = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    X0 = x0
    Y0 = y0
    t = 1
    while t <= (1.0/step):
        t = t * step
        X1 = x_coefs[0][0] * t**3 + x_coefs[0][1] * t**2 + x_coefs[0][2] * t + x_coefs[0][3]
        Y1 = y_coefs[0][0] * t**3 + y_coefs[0][1] * t**2 + y_coefs[0][2] * t + y_coefs[0][3]
        add_edge(points,X0,Y0,0,X1,Y1,0)
        X0 = X1
        Y0 = Y1
        t = t / step
        t += 1
        print t
    t = t * step
    print x_coefs[0][0] * t**3  + x_coefs[0][1] * t**2 + x_coefs[0][2] * t + x_coefs[0][3]
    print y_coefs[0][0] * t**3 + y_coefs[0][1] * t**2 + y_coefs[0][2] * t + y_coefs[0][3]   

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

