from display import *
from matrix import *
import math

def param_x(t,r,x):
    return round(r * math.cos(2*math.pi*t) + x)
def param_y(t,r,y):
    return round(r * math.sin(2*math.pi*t) + y)
def param_z(t,r,z):
    return "Hi"

def add_circle( points, cx, cy, cz, r, step ):
    cy = YRES - cy
    t = 0
    x = 0
    x0= param_x(t-step,r,cx)
    y = 0
    y0= param_y(t-step,r,cy)
    while (t <= 1):
        x = param_x(t,r,cx)
        y = param_y(t,r,cy)
        add_edge(points,x0,y0,0,x,y,0)
        x0 = x
        y0 = y
        t+=step

def cb(x):
    return x * x * x
def sq(x):
    return x * x
    
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    y0 = YRES - y0
    y1 = YRES - y1
    y2 = YRES - y2
    y3 = YRES - y3
    if curve_type == "hermite":
        t = 0
        coef= generate_curve_coefs([x0,y0],[x1,y1],[x2,y2],[x3,y3],curve_type)
        while (t <= 1.01):
            #at^3 + bt^2 + ct + d 
            x = round(coef[0][0][0]*cb(t) + coef[0][0][1]*sq(t) + coef[0][0][2]*t + coef[0][0][3])
            y = round(coef[1][0][0]*cb(t) + coef[1][0][1]*sq(t) + coef[1][0][2]*t + coef[1][0][3])
            add_edge(points,x0,y0,0,x,y,0)
            x0=x
            y0=y
            t+=step
    elif curve_type == "bezier":
        t = 0
        coef= generate_curve_coefs([x0,y0],[x1,y1],[x2,y2],[x3,y3],curve_type)
        while (t <= 1.01):
            #a(1-t)^3 + 3ct(1-t)^2 + 3dt^2(1-t) + bt^3
            # x = coef[0][0][0]*cb(1-t) + coef[0][0][1]*t*sq(1-t) + coef[0][0][2]*sq(t)*(1-t) + coef[0][0][3]*cb(t)
            # y = coef[1][0][0]*cb(1-t) + coef[1][0][1]*t*sq(1-t) + coef[1][0][2]*sq(t)*(1-t) + coef[1][0][3]*cb(t)
            
            x = round(coef[0][0][0]*cb(t) + coef[0][0][1]*sq(t) + coef[0][0][2]*t + coef[0][0][3])
            y = round(coef[1][0][0]*cb(t) + coef[1][0][1]*sq(t) + coef[1][0][2]*t + coef[1][0][3])

            add_edge(points,x0,y0,0,x,y,0)
            x0=x
            y0=y
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

