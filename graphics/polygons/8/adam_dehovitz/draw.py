from display import *
from matrix import *
import math


def add_rect( points, x0, y0, z0, h, w, d):
    add_edge(points, x0, y0, z0, x0, y0, z0)
    add_edge(points, x0, y0 - h, z0, x0, y0 - h, z0)
    add_edge(points, x0, y0, z0 - d, x0, y0, z0 - d)
    add_edge(points, x0, y0 - h, z0 - d, x0, y0 - h, z0 - d)
    add_edge(points, x0 + w, y0 - h, z0, x0 + w, y0 - h, z0)
    add_edge(points, x0 + w, y0 - h, z0 - d,x0 + w, y0 - h, z0 - d)
    add_edge(points, x0 + w, y0, z0, x0 + w, y0, z0)
    add_edge(points, x0 + w, y0, z0 - d, x0 + w, y0, z0 - d)

def add_sphere( points, cx, cy, r):
    step = 0.1
    t1 = 0
    while (t1 <= 1.00000001):
        t2 = 0
        while (t2 <= 1.00000001):
            theta1 = math.pi * t1
            theta2 = 2 * math.pi * t2
            
            x = cx + r  * math.cos(theta1)
            y = cy + r * math.sin(theta1) * math.cos(theta2)
            z = r * math.sin(theta1) * math.sin(theta2)
            add_point( points, x, y, z )
            t2 += 0.01
        t1 += 0.01

def add_torus(points, cx, cy, r1, r2):
    t1 = 0
    while (t1 <= 1.001):
        t2 = 0
        while (t2 <= 1.001):
            theta1 = 2 * math.pi * t1
            theta2 = 2 * math.pi * t2
            x = cx + math.cos(theta1) * (r1 * math.cos(theta2) + r2)
            y = cy + r1 * math.sin(theta2)
            z = math.sin(theta1) * (r1 * math.cos(theta2) + r2)
            add_point(points, x, y, z)
            t2 += 0.01
        t1 += 0.01

def add_circle( points, cx, cy, cz, r, step ):
     x0 = cx + r
     y0 = cy
     z0 = cz
     t=0
     while ( t<=1.0001) :
         x = r * math.cos( 2 * math.pi * t ) + cx
         y = r * math.sin( 2 * math.pi * t ) + cy
         z = cz
         #print( str(x) + ", " + str(y) )
         add_edge (points, x0, y0, z0, x, y, z)
         x0 = x
         y0 = y
         z0 = z
         t= t+ step
             
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    xco = generate_curve_coefs(x0, x1, x2, x3, curve_type)
    yco = generate_curve_coefs(y0, y1, y2, y3, curve_type)
    while (t <= 1.0001):
        x = xco[0]*math.pow(t,3) + xco[1]*math.pow(t,2) + xco[2]*(t)+xco[3]
        y = yco[0]*math.pow(t,3) + yco[1]*math.pow(t,2) + yco[2]*(t)+yco[3]
        add_edge( points, x0, y0, 0, x, y, 0)
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

