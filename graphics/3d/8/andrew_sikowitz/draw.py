from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    step = 10000
    x0 = cx + r #Starting point, cos(0)=1, sin(0) = 0
    y0 = cy
    
    for t in range(step+1):
        theta = 2*t*math.pi
        x = r*math.cos(theta/float(step)) + cx;
        y = r*math.sin(theta/float(step)) + cy;
        add_edge(points, x0, y0, cz, x, y, cz)
        x0 = x
        y0 = y

def add_prism(points, px, py, pz, w, h, d):
    for i in [0,w]:
        for j in [0,h]:
            for k in [0,d]:
                add_point(points, px+i,py+j,pz+k)
                add_point(points, px+i,py+j,pz+k)
                
def add_sphere(points, sx, sy, r):
    step = int(r*2)
    for t in range(step+1):
        theta = 2*t*math.pi
        for t2 in range(step+1):
            phi = 2*t2*math.pi
            x = r*math.cos(theta/float(step)) + sx
            y = r*math.sin(theta/float(step))*math.cos(phi/float(step)) + sy
            z = r*math.sin(theta/float(step))*math.sin(phi/float(step))
            add_point(points, x,y,z)
            add_point(points, x,y,z)

def add_torus(points, tx, ty, r1, r2):
    step = 50
    for t in range(step+1):
        theta = 2*t*math.pi
        for t2 in range(step+1):
            phi = 2*t2*math.pi
            x = math.cos(phi/float(step))*(r1*math.cos(theta/float(step))+r2) + tx
            y = r1*math.sin(theta/float(step)) + ty
            z = -math.sin(phi/float(step))*(r1*math.cos(theta/float(step))+r2)
            add_point(points, x,y,z)
            add_point(points, x,y,z)
            
            
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

