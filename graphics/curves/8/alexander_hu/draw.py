from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    last = [cx + r, cy , cz]
    while t <= 1.000001:
        add_point(points, last[0], last[1], last[2])
        t += step
        theta = 2 * t * math.pi
        last = [cx + r*math.cos(theta), cy + r*math.sin(theta), cz]
        add_point(points, last[0], last[1], last[2])

    
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    x,y,t = x0,y0,0
    xlist = []
    ylist = []
    if curve_type == 'bezier':
        xlist = generate_curve_coefs( x0, x1, x2, x3, curve_type )[0]
        ylist = generate_curve_coefs( y0, y1, y2, y3, curve_type )[0]
    elif curve_type == 'hermite':
        cx1 = x1 - x0
        cx2 = x3 - x2
        cy1 = y1 - y0
        cy2 = y3 - y2
        xlist = generate_curve_coefs( x0, x2, cx1, cx2, curve_type )[0]
        ylist = generate_curve_coefs( y0, y2, cy1, cy2, curve_type )[0]

    
        
    while t < 1.0000001:
        t += step
        add_point(points, x, y, 0)
        x = t*t*t*xlist[0] + t*t*xlist[1] + t*xlist[2] + xlist[3]
        y = t*t*t*ylist[0] + t*t*ylist[1] + t*ylist[2] + ylist[3]
        add_point(points, x, y, 0)
   
    

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

