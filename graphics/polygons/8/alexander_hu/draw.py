from display import *
from matrix import *
from math import cos, sin, pi

MAX_STEPS = 100

def cross(a,b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def vect_subtract(a,b):
    return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]

def surface(a,b,c):
    v1 = vect_subtract(b,a)
    v2 = vect_subtract(c,a)
    return cross(v1,v2)

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points, x0,y0,z0)
    add_point(points, x1,y1,z1)
    add_point(points, x2,y2,z2)
    
def draw_polygons( points, screen, color ):

    view = [0,0,-1]

    if len(points) < 3:
        print "Need at least 3 points to draw a polygon"
    
    run = 0
    while run < len(points) - 2:
        p0 = points[run]
        p1 = points[run+1]
        p2 = points[run+2]

        print dot(surface(p0,p1,p2),view)
        
        if dot(surface(p0,p1,p2),view) > 0:

            draw_line(screen, p0[0], p0[1],
                      p1[0], p1[1], color )
            draw_line(screen, p1[0], p1[1],
                      p2[0], p2[1], color )
            draw_line(screen, p2[0], p2[1],
                      p0[0], p0[1], color )

        run += 3

def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y + height
    z1 = z + depth

    def add_face(a0,b0,c0,a1,b1,c1,a2,b2,c2,a3,b3,c3):
        add_polygon(points,a0,b0,c0,a1,b1,c1,a2,b2,c2)
        add_polygon(points,a0,b0,c0,a2,b2,c2,a3,b3,c3)

    add_face(x,y,z, x,y1,z, x1,y1,z,  x1,y,z) #front
    add_face(x,y,z, x,y,z1, x,y1,z1, x,y1,z ) #left
    add_face(x,y,z1, x1,y,z1, x1,y1,z1, x,y1,z1) #back
    add_face(x1,y,z1, x1,y,z, x1,y1,z, x1,y1,z1) #right
    add_face(x,y,z, x1,y,z, x1,y,z1, x,y,z1) #top
    #add_face(x,y1,z, x,y1,z1, x1,y1,z1, x1,y1,z) #bottom

def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    
    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt            
            add_edge( points, temp[index][0], temp[index][1], temp[index][2], temp[index][0], temp[index][1], temp[index][2] )
            
            longt+= 1
        lat+= 1

def generate_sphere( points, cx, cy, cz, r, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle <= circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = r * cos( pi * circ ) + cx
            y = r * sin( pi * circ ) * cos( 2 * pi * rot ) + cy
            z = r * sin( pi * circ ) * sin( 2 * pi * rot ) + cz
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step

def add_torus( points, cx, cy, cz, r0, r1, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    
    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt
            add_edge( points, temp[index][0], temp[index][1], temp[index][2], temp[index][0], temp[index][1], temp[index][2] )
            
            longt+= 1
        lat+= 1

def generate_torus( points, cx, cy, cz, r0, r1, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle < circ_stop:
            
            circ = float(circle) / MAX_STEPS
            x = (cos( 2 * pi * rot ) *
                 (r0 * cos( 2 * pi * circ) + r1 ) + cx)
            y = r0 * sin(2 * pi * circ) + cy
            z = (sin( 2 * pi * rot ) *
                 (r0 * cos(2 * pi * circ) + r1))
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step



def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy

    t = step
    while t<= 1:
        
        x = r * cos( 2 * pi * t ) + cx
        y = r * sin( 2 * pi * t ) + cy

        add_edge( points, x0, y0, cz, x, y, cz )
        x0 = x
        y0 = y
        t+= step
    add_edge( points, x0, y0, cz, cx + r, cy, cz )

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xcoefs = generate_curve_coefs( x0, x1, x2, x3, curve_type )
    ycoefs = generate_curve_coefs( y0, y1, y2, y3, curve_type )
        
    t =  step
    while t <= 1:
        
        x = xcoefs[0][0] * t * t * t + xcoefs[0][1] * t * t + xcoefs[0][2] * t + xcoefs[0][3]
        y = ycoefs[0][0] * t * t * t + ycoefs[0][1] * t * t + ycoefs[0][2] * t + ycoefs[0][3]

        add_edge( points, x0, y0, 0, x, y, 0 )
        x0 = x
        y0 = y
        t+= step

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

