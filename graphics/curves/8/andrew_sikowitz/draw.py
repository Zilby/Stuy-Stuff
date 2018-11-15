from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    x0 = cx + r #Starting point, cos(0)=1, sin(0) = 0
    y0 = cy

    for t in range(100001):
        theta = 2*t*math.pi
        x = r*math.cos(theta/10000.0) + cx;
        y = r*math.sin(theta/10000.0) + cy;
        add_edge(points, x0, y0, cz, x, y, cz)
        x0 = x
        y0 = y

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == "hermite":
        dx0 = x1-x0
        dy0 = y1-y0
        dx1 = x3-x2
        dy1 = y3-y2
        cox = generate_curve_coefs(x0,x2,dx0,dx1,curve_type)
        coy = generate_curve_coefs(y0,y2,dy0,dy1,curve_type)
    elif curve_type == "bezier":
        cox = generate_curve_coefs(x0,x1,x2,x3,curve_type)
        coy = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    c = 10000.0
    for t in range(int(c)+1):
        #print t,c,t/c,cox[0]
        x = math.pow(t/c,3)*cox[0]+math.pow(t/c,2)*cox[1]+(t/c)*cox[2] + cox[3]
        y = math.pow(t/c,3)*coy[0]+math.pow(t/c,2)*coy[1]+(t/c)*coy[2] + coy[3]
        add_edge(points, x0,y0,0, x,y,0)
        x0 = x
        y0 = y

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

