from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step):
    t = step
    x0 = r * math.cos(0 * 2 * math.pi) + cx
    y0 = r * math.sin(0 * 2 * math.pi) + cy
    z0 = cz
    while t <= 1.0 + step:
	x = r * math.cos(t * 2 * math.pi) + cx
	y = r * math.sin(t * 2 * math.pi) + cy
	z = cz
	add_edge (points, x0, y0, z0, x, y, z)
	x0 = x
	y0 = y
	z0 = z
        t += step
                         


def add_box (points, x, y, z, width, height, depth):
    w = width
    h = height
    d = depth
    add_edge (points, x, y, z, x, y, z)
    add_edge (points, x + w, y, z, x + w, y, z)
    add_edge (points, x + w, y + h, z, x + w, y + h, z)
    add_edge (points, x + w, y + h, z + d, x + w, y + h, z + d)
    add_edge (points, x + w, y, z + d, x + w, y, z + d)
    add_edge (points, x, y + h, z, x, y + h, z)
    add_edge (points, x, y + h, z + d, x, y + h, z + d)
    add_edge (points, x, y, z + d, x, y, z + d)

def add_sphere (points, cx, cy, r):
    t = 0
    q = 0
    step = 0.01
    while q <= 1.0:
        t = 0
        while t <= 1.0:
            x = r * math.cos(t * 2 * math.pi) + cx
            y = r * math.sin(t * 2 * math.pi)* math.cos(q * math.pi) + cy
            z = r * math.sin(t * 2 * math.pi)* math.sin(q * math.pi) 
            add_edge (points, x, y, z, x, y, z)
            t = t + step

        q = q + step

def add_torus (points, cx, cy, radius1, radius2):
    t = 0
    q = 0
    step = 0.01
    while q <= 1.0:
        t = 0
        while t <= 1.0:
            x = math.cos(q * 2 * math.pi) *(radius1 * math.cos(t * 2 * math.pi) + radius2)  + cx
            y = radius1 * math.sin(t * 2 * math.pi) + cy
            z =  -math.sin(q * 2 * math.pi)* (radius1 * math.cos(t * 2 * math.pi) + radius2)
            add_edge (points, x, y, z, x, y, z)
            t += step

        q += step
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    x = []
    if curve_type == 'bezier':
        x = generate_curve_coefs (x0, x1, x2, x3, 'b')
        y = generate_curve_coefs (y0, y1, y2, y3, 'b')

        while t <= 1.0:
            dx = x[0][0] *t **3 + x[0][1] * t **2 + x[0][2] * t + x[0][3]
            dy = y[0][0] *t **3 + y[0][1] * t **2 + y[0][2] * t + y[0][3]
            add_edge (points,x0, y0, 0, dx, dy, 0)
            x0 = dx
            y0 = dy

            t += step
        
    elif curve_type == 'hermite':
        x = generate_curve_coefs (x0, x2, x1 - x0, x3 - x2, 'h')
        y = generate_curve_coefs (y0, y2, y1 -y0, y3 - y2, 'h')
        while t <= 1.0:
            dx = x[0][0] *t **3 + x[0][1] * t **2 + x[0][2] * t + x[0][3]
            dy = y[0][0] *t **3 + y[0][1] * t **2 + y[0][2] * t + y[0][3]
            add_edge (points, x0, y0, 0, dx, dy, 0)
            x0 = dx
            y0 = dy
            t += step
    else:
        print "Curve not valid"
    

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

