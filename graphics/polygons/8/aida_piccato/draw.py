from display import *
from matrix import *
from math import cos, sin, pi

MAX_STEPS = 100


def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points, x0, y0, z0)
    add_point(points, x1, y1, z1)
    add_point(points, x2, y2, z2)

def get_cross_prod(a, b):
    v = []
    v.append(a[1]*b[2] - a[2]*b[1])
    v.append(a[2]*b[0] - a[0]*b[2])
    v.append(a[0]*b[1] - a[1]*b[0])
    return v

def get_cosine( p1, p2, p3 ):
    print p1, p2
    a_vector = [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    b_vector = [p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]]
    print a_vector
    n = get_cross_prod(a_vector, b_vector)
    v = [0, 0, -1]
    return n[0]*v[0] + n[1]*v[1] + n[2]*v[2]

def draw_polygons( points, screen, color ):
    if (len(points)< 3):
        print "Need at least three points to draw a polygon"
    i = 0
    while i < len(points):
        p1 = points[i]
        p2 = points[i+1]
        p3 = points[i+2]
        if get_cosine(p1, p2, p3) < 0:
            draw_line(screen, p1[0], p1[1], p2[0], p2[1], color)
            draw_line(screen, p2[0], p2[1], p3[0], p3[1], color)
            draw_line(screen, p3[0], p3[1], p1[0], p1[1], color)
        i += 3


def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth
    add_polygon(points, x, y, z, x, y1, z, x1, y, z)
    add_polygon(points, x1, y, z, x, y1, z, x1, y1, z)

    add_polygon(points, x1, y, z, x1, y1, z, x1, y, z1)
    add_polygon(points, x1, y, z1, x1, y1, z, x1, y1, z1)

    
    add_polygon(points, x, y, z, x, y, z1, x, y1, z)
    add_polygon(points, x, y, z1, x, y1, z1, x, y1, z)

    add_polygon(points, x1, y, z1, x, y1, z1, x, y, z1)
    add_polygon(points, x, y1, z1, x, y, z1, x1, y, z1)

    add_polygon(points, x, y, z1, x, y, z, x1, y, z1)
    add_polygon(points, x1, y, z1, x, y, z, x1, y, z)

    add_polygon(points, x, y1, z, x, y1, z1, x1, y1, z1)
    add_polygon(points, x, y, z, x1, y1, z1, x, y1, z)
def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )
    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    while lat <= lat_stop:
        longt = 0
        while longt < longt_stop:
            index = lat * num_steps + longt
            p1 = temp[index]
            p2 = temp[index + num_steps]
            p3 = temp[index + num_steps + 1]
            p4 = temp[index + 1]
            add_polygon( points,
                        p1[0],p1[1],p1[2],
                        p2[0], p2[1], p2[2],
                        p3[0], p3[1],p3[2] )
            add_polygon( points,
                         p1[0],p1[1],p1[2],
                         p3[0], p3[1],p3[2],
                         p4[0], p4[1], p4[2] )
            longt+= 1
        lat+= 1

def generate_sphere( points, cx, cy, cz, r, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation <= rot_stop:
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
    
    while lat <= lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt
            p1 = temp[index]
            p2 = temp[index + num_steps]
            p3 = temp[index + num_steps + 1]
            add_polygon( points,
                        p1[0],p1[1],p1[2],
                        p2[0], p2[1], p2[2],
                        p3[0], p3[1],p3[2] )
            add_polygon( points,
                         p1[0],p1[1],p1[2],
                         p3[0], p3[1],p3[2],
                         p2[0], p2[1], p2[2] )
            longt+= 1
        lat+= 1

def generate_torus( points, cx, cy, cz, r0, r1, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation <= rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        while circle <= circ_stop:
            
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

