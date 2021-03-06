from display import *
from matrix import *
import math

def add_box( points, x, y, z, width, height, depth ):
    add_edge(points, x,y,z, x,y,z)
    add_edge(points, x,y+height,z, x,y+height,z)
    add_edge(points, x,y,z+depth, x,y,z+depth)
    add_edge(points, x+width,y,z, x+width,y,z)
    add_edge(points, x+width,y+height,z, x+width,y+height,z)
    add_edge(points, x+width,y,z+depth, x+width,y,z+depth)
    add_edge(points, x+width,y+height,z+depth, x+width,y+height,z+depth)
    add_edge(points, x,y+height,z+depth, x,y+height,z+depth)
    
def add_sphere( points, cx, cy, radius):
    p = 0
    c = 0
    while(p<1):
        while(c<1):
            x = radius*math.cos(2*math.pi*c) + cx
            y = radius*math.sin(2*math.pi*c)*math.cos(math.pi*p) + cy
            z = radius*math.sin(2*math.pi*c)*math.sin(math.pi*p) #+ cz
            add_edge(points, x,y,z, x,y,z)
            c+=.05
        p+=.05
        c = 0

def add_torus( points, cx, cy, radius1, radius2 ):
    p = 0
    c = 0
    while(p<1):
        while(c<1):
            x = math.cos(2*math.pi*p)*(radius1*math.cos(2*math.pi*c) + radius2) + cx
            y = radius1*math.sin(2*math.pi*c) + cy
            z = math.sin(2*math.pi*p) * (radius1*math.cos(2*math.pi*c) + radius2) #+ cz
            add_edge(points, x,y,z, x,y,z)
            c+=.05
        p+=.05
        c = 0
            
def add_circle( points, cx, cy, cz, r, step ):
    
    x0 = cx +r
    y0 = cy
    t = step
    while( t < 1.00001):
        x = r*math.cos(2*math.pi*t) + cx
        y = r*math.sin(2*math.pi*t) + cy

        add_edge(points, x0, y0, cz, x, y, cz )
        x0 = x
        y0 = y
            
        t += step
        
    
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    
    coefficients = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    ##print_matrix(coefficients)
    ax= coefficients[0][0]
    bx= coefficients[0][1]
    cx= coefficients[0][2]
    dx= coefficients[0][3]
    coefficients = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    ay= coefficients[0][0]
    by= coefficients[0][1]
    cy= coefficients[0][2]
    dy= coefficients[0][3]

    xt = x0
    yt = y0
    t = step
    while (t<1):
            
        x = ax*t*t*t + bx*t*t + cx*t + dx
        y = ay*t*t*t + by*t*t + cy*t + dy
        add_edge(points, xt, yt, 0, x, y, 0 )
        t+= step
        yt = y
        xt= x


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

