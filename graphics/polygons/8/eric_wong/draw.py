from display import *
from matrix import *
from math import cos, sin, pi

MAX_STEPS = 100

def add_box( points, x, y, z, w, h, d ):

    x1 = x+w
    y1 = y-h
    z1 = z-d

    #front
    add_polygon(points, x, y, z, x, y1, z, x1, y, z)
    add_polygon(points, x1, y, z, x, y1, z, x1, y1, z) 
    #right
    add_polygon(points, x1, y, z, x1, y1, z, x1, y, z1)
    add_polygon(points, x1, y, z1, x1, y1, z, x1, y1, z1)
    #top
    add_polygon(points, x, y, z1, x, y, z, x1, y, z1)
    add_polygon(points, x1, y, z1, x, y, z, x1, y, z)
    #bottom
    add_polygon(points, x, y1, z, x, y1, z1, x1, y1, z)
    add_polygon(points, x1, y1, z, x, y1, z1, x1, y1, z1)
    #back
    add_polygon(points, x1, y, z1, x1, y1, z1, x, y, z1)
    add_polygon(points, x, y, z1, x1, y1, z1, x, y1, z1)
    #left
    add_polygon(points, x, y, z1, x, y1, z1, x, y, z)
    add_polygon(points, x, y, z, x, y1, z1, x, y1, z)
    
def add_sphere( points, cx, cy, cz, r, step=1 ):

    steps = MAX_STEPS / step
    temp = []
    make_sphere( temp, cx, cy, cz, r, step )

    lat = 0
    while (lat <= steps):

        lon = 0
        while (lon <= steps):

            index = lat * steps + lon

            add_polygon( points, 
                         temp[index][0], temp[index][1], temp[index][2],
                         temp[index+steps][0], temp[index+steps][1], temp[index+steps][2], 
                         temp[index+steps+1][0], temp[index+steps+1][1], temp[index+steps+1][2] )            
            add_polygon( points, 
                         temp[index][0], temp[index][1], temp[index][2],
                         temp[index+steps+1][0], temp[index+steps+1][1], temp[index+steps+1][2], 
                         temp[index+1][0], temp[index+1][1], temp[index+1][2] )

            lon+= 1
        lat+= 1        

def make_sphere( points, cx, cy, cz, r, step=1 ):

    spin = 0
    while (spin<=MAX_STEPS):

        circle = 0
        while (circle<=MAX_STEPS):

            x = cx + r * cos( 2 * pi * circle )
            y = cy + r * sin( 2 * pi * circle ) * cos( pi * spin )
            z = r * sin( 2 * pi * circle ) * cos( pi * spin )

            add_point( points, x, y, z)

            circle+= step
        spin+= step

def add_torus( points, cx, cy, r1, r2, step=1 ):

    steps = MAX_STEPS / step
    temp = []
    make_torus( temp, cx, cy, r1, r2, step )

    lat = 0
    while (lat <= steps):

        lon = 0
        while (lon <= steps):

            index = lat * steps + lon
            
            try:
                add_polygon(points,
                            temp[index][0], temp[index][1], temp[index][2],
                            temp[index+steps][0], temp[index+steps][1], temp[index + steps][2],
                            temp[index+steps+1][0], temp[index+steps+1][1], temp[index+steps+1][2] )
            except:
                if index >= len(temp):
                    index = 0
                if index+steps+1 >= len(temp):
                    index = longt

                add_polygon(points,
                            temp[index][0], temp[index][1], temp[index][2],
                            temp[index+steps][0],temp[index+steps][1],temp[index+steps][2],
                            temp[index+steps+1][0],temp[index+steps+1][1],temp[index+steps+1][2] )
            try:
                add_polygon(points,
                            temp[index][0], temp[index][1], temp[index][2],
                            temp[index+steps+1][0], temp[index+steps+1][1], temp[index+steps+1][2],
                            temp[index+1][0], temp[index+1][1], temp[index+1][2] )
            except:
                if index+1 >= len(temp):
                    index = 0
                if index+steps+1 >= len(temp):
                    index = longt

                add_polygon(points,
                            temp[index][0], temp[index][1], temp[index][2],
                            temp[index+steps+1][0], temp[index+steps+1][1], temp[index+steps+1][2],
                            temp[index+1][0], temp[index+1][1], temp[index+1][2] )

            lon+= 1
        lat+= 1  

def make_torus( points, cx, cy, r1, r2, step ):

    spin = 0
    while (spin<=MAX_STEPS):

        circle = 0
        while (circle<=MAX_STEPS):

            x = cx + cos( 2 * pi * spin ) * ( r1 * cos( 2 * pi * circle ) + r2 )
            y = cy + r1 * sin( 2 * pi * circle )
            z = sin( 2 * pi * spin ) * ( r1 * cos( 2 * pi * circle ) + r2 )

            add_point( points, x, y, z )

            circle+= step
        spin+= step

def add_circle( points, cx, cy, cz, r, step=0.1 ):
    x0 = cx + r
    y0 = cy
    z0 = cz
    t=0
    while (t<=1.000001):
        x = r * math.cos(2*math.pi*t) + cx
        y = r * math.sin(2*math.pi*t) + cy
        z = z0
        add_edge(points, x0, y0, z0, x, y, z)
        x0 = x
        y0 = y
        z0 = z
        t = t + step

def cal_point(t, coef):
    return (coef[0][0]*t*t*t) + (coef[0][1]*t*t) + (coef[0][2]*t) + (coef[0][3])
        
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    t = 0
    if curve_type == "hermite":
        dxi = x1 - x0
        dxf = x3 - x2
        x_coef = generate_curve_coefs(x0, x2, dxi, dxf, curve_type)
        dyi = y1 - y0
        dyf = y3 - y2
        y_coef = generate_curve_coefs(y0, y2, dyi, dyf, curve_type)

    elif curve_type == "bezier":
        x_coef = generate_curve_coefs(x0, x1, x2, x3, curve_type)
        y_coef = generate_curve_coefs(y0, y1, y2, y3, curve_type)

    while (t <= 1.0000001):
        x = cal_point(t, x_coef)
        y = cal_point(t, y_coef)
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t = t + step

def cal_angle( p0, p1, p2 ):

    a = [ p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2] ]
    b = [ p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2] ]
    n = [ a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0] ]
    v = [ 0, 0, -1 ]

    return n[0] * v[0] + n[1] * v[1] + n[2] * v[2]

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def draw_polygons( matrix, screen, color ):
    if len( matrix ) < 3:
        print "Need at least 3 points to draw a polygon"
    p = 0
    while p < len( matrix ):

        p0 = matrix[p]
        p1 = matrix[p+1]
        p2 = matrix[p+2]

        if (cal_angle( p0, p1, p2 ) < 0 ):
            draw_line (screen, p0[0], p0[1], p1[0], p1[1], color )
            draw_line (screen, p1[0], p1[1], p2[0], p2[1], color )
            draw_line (screen, p2[0], p2[1], p0[0], p0[1], color )

        p+= 3
        
def add_polygon( matrix, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )
    add_point( matrix, x2, y2, z2 )
    
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

