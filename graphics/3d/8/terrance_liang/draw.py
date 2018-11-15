from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    while (t <= 1.000001):
        x = cx + r*math.cos(2*math.pi*t) 
        y = cy + r*math.sin(2*math.pi*t)
        if (t>0):
            add_edge(points, x0, y0, cz, x, y, cz)
        x0 = x
        y0 = y
        t += step

def par_coor(t, coef):
    return t*t*t*coef[0]+t*t*coef[1]+t*coef[2]+coef[3]

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == "hermite":
        xcoef = generate_curve_coefs(x0,x2,x1-x0,x3-x2,curve_type)
        ycoef = generate_curve_coefs(y0,y2,y1-y0,y3-y2,curve_type)
    elif curve_type == "bezier":
        xcoef = generate_curve_coefs(x0,x1,x2,x3,curve_type)
        ycoef = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    else:
        print "Invalid curve type \n"
        return 
    t = 0
    xc = x0
    yc = y0
    while (t <= 1.000001):
        x = par_coor(t,xcoef[0]) 
        y = par_coor(t,ycoef[0])
        add_edge(points, xc, yc, 0, x, y, 0)
        xc = x
        yc = y
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

def add_box(points,x,y,z,w,h,d):
    add_edge(points,x,y,z,x,y,z)
    add_edge(points,x+w,y,z,x+w,y,z)
    add_edge(points,x+w,y,z-d,x+w,y,z-d)
    add_edge(points,x,y,z-d,x,y,z-d)
    add_edge(points,x,y-h,z,x,y-h,z)
    add_edge(points,x+w,y-h,z,x+w,y-h,z)
    add_edge(points,x+w,y-h,z-d,x+w,y-h,z-d)
    add_edge(points,x,y-h,z-d,x,y-h,z-d)

def add_sphere(points,cx,cy,r,step):
    p = 0
    while p < 1:
        c = 0
        while c < 1:
            x = cx + r*math.cos(2*math.pi*c) 
            y = cy + r*math.sin(2*math.pi*c)*math.cos(math.pi*p)
            z = r*math.sin(2*math.pi*c)*math.sin(math.pi*p)
            c = c + step
            add_edge(points,x,y,z,x,y,z)
        p = p + step

def add_torus(points,cx,cy,r1,r2,step):
    p = 0
    while p < 1:
        c = 0
        while c < 1:
            x = cx + math.cos(2*math.pi*p)*(r1*math.cos(2*math.pi*c)+r2) 
            y = cy + r1*math.sin(2*math.pi*c)
            z = math.sin(2*math.pi*p)*(r1*math.cos(2*math.pi*c)+r2)
            c = c + step
            add_edge(points,x,y,z,x,y,z)
        p = p + step
