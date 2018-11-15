from display import *
from matrix import *
from math import cos, sin, pi

MAX_STEPS = 100

#### HELP FUNCTIONS
def surface_normal (points, index):
    p0 = points[index]
    p1 = points[index+1]
    p2 = points[index+2]
    a = [p1[0]-p0[0], 
         p1[1]-p0[1], 
         p1[2]-p0[2]]
    b = [p2[0]-p0[0],
         p2[1]-p0[1], 
         p1[2]-p0[2]]
    return [a[1]*b[2]-a[2]*b[1],
           a[2]*b[0]-a[0]*b[2],
           a[0]*b[1]-a[1]*b[0]]

#cos theta?
def dot_product (a, b):
    n = 0
    for i in range (3):
        n += (a[i]*b[i])
    return n

def front (points, index, b):
    a = surface_normal(points, index)
    cos = dot_product(a, b)
    return cos < 0

### POLYGON FUNCTIONS
def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points, x0, y0, z0)
    add_point(points, x1, y1, z1)
    add_point(points, x2, y2, z2)
    
def draw_polygons( points, screen, color ):
    if len( points ) < 3:
        print "not enough points"
        
    p = 0
    while p < len( points ):
        if front(points, p, [0, 0, -1]):
            draw_line( screen, 
                       points[p][0], 
                       points[p][1],
                       points[p+1][0], 
                       points[p+1][1], 
                       color )
            draw_line( screen, 
                       points[p+1][0], 
                       points[p+1][1],
                       points[p+2][0], 
                       points[p+2][1], 
                       color )
            draw_line( screen, 
                       points[p+2][0], 
                       points[p+2][1],
                       points[p][0], 
                       points[p][1], color )
        p+= 3

#### ADDING SHIT
def add_box( points, x, y, z, width, height, depth ):

    x1 = x + width
    y1 = y - height
    z1 = z - depth

    add_polygon( points, x, y, z, x, y1, z, x1, y1, z)
    add_polygon( points, x1, y1, z, x1, y, z,  x, y, z)
    add_polygon( points, x1, y, z, x1, y1, z, x1, y1, z1)
    add_polygon( points, x1, y1, z1, x1, y, z1, x1, y, z) 
    add_polygon( points, x1, y, z1, x1, y1, z1, x, y1, z1) 
    add_polygon( points, x, y1, z1, x, y, z1, x1, y, z1) 
    add_polygon( points, x, y, z1, x, y1, z1,  x, y1, z)
    add_polygon( points, x, y1, z, x, y, z, x, y, z1)   
    add_polygon( points, x, y, z1, x, y, z, x1, y, z)
    add_polygon( points, x1, y, z, x1, y, z1, x, y, z1)
    add_polygon( points, x, y1, z, x, y1, z1, x1, y1, z1)
    
    """
     add_edge( points, 
              x, y, z, 
              x, y, z )
    add_edge( points, 
              x, y1, z, 
              x, y1, z )
    add_edge( points, 
              x1, y, z, 
              x1, y, z )
    add_edge( points, 
              x1, y1, z, 
              x1, y1, z )
    add_edge( points, 
              x, y, z1, 
              x, y, z1 )
    add_edge( points, 
              x, y1, z1, 
              x, y1, z1 )
    add_edge( points, 
              x1, y, z1, 
              x1, y, z1 )
    add_edge( points, 
              x1, y1, z1, 
              x1, y1, z1 )
    """

def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step + 1
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    
    while lat < lat_stop -1:
        longt = 0
        while longt < longt_stop-1:
            
            index = lat * num_steps + longt
            #add_edge( points, temp[index][0], temp[index][1], temp[index][2], temp[index][0], temp[index][1], temp[index][2] )
            
            add_polygon( points, 
                    temp[index][0],
                         temp[index][1], 
                         temp[index][2], 
                         temp[index+num_steps][0],
                         temp[index+num_steps][1], 
                         temp[index+num_steps][2], 
                         temp[index+num_steps+1][0], 
                         temp[index+num_steps+1][1],
                         temp[index+num_steps+1][2] )
            add_polygon( points, 
                         temp[index][0], 
                         temp[index][1], temp[index][2], 
                         temp[index+num_steps+1][0],
                         temp[index+num_steps+1][1], 
                         temp[index+num_steps+1][2], 
                         temp[index+1][0], 
                         temp[index+1][1], 
                         temp[index+1][2] )
            longt+= 1
        lat+= 1


def add_torus( points, cx, cy, cz, r0, r1, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps
    l = len(temp)
    
    while lat <= lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt
            #add_edge( points, temp[index][0], temp[index][1], temp[index][2], temp[index][0], temp[index][1], temp[index][2] )

            add_polygon( points, 
                         temp[index][0], 
                         temp[index][1], 
                         temp[index][2], 
                         temp[(index)%l+1][0], 
                         temp[(index)%l+1][1], 
                         temp[(index)%l+1][2], 
                         temp[(index+num_steps)%l+1][0], 
                         temp[(index+num_steps)%l+1][1], 
                         temp[(index+num_steps)%l+1][2] )
            add_polygon( points, 
                         temp[index][0], temp[index][1], 
                         temp[index][2], 
                         temp[(index+num_steps)%l+1][0], 
                         temp[(index+num_steps)%l+1][1],
                         temp[(index+num_steps)%l+1][2], 
                         temp[(index+num_steps)%l][0],
                         temp[(index+num_steps)%l][1], 
                         temp[(index+num_steps)%l][2] )
            
            longt+= 1
        lat+= 1

#### GENERATIONS FUNCTIONS
def generate_sphere( points, cx, cy, cz, r, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation <= rot_stop:
        circle = 0
        rot = float(rotation) / MAX_STEPS
        i = 0
        while circle <= circ_stop:
            i+=1
            circ = float(circle) / MAX_STEPS
            x = r * cos( pi * circ ) + cx
            y = r * sin( pi * circ ) * cos( 2 * pi * rot ) + cy
            z = r * sin( pi * circ ) * sin( 2 * pi * rot ) + cz
            
            add_point( points, x, y, z )

            circle+= step
        rotation+= step



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


### BASE FUNCTIONS
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
