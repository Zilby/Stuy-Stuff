from display import *
from matrix import *
from math import cos, sin, pi

MAX_STEPS = 100

def add_polygon( polygons, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(polygons, x0, y0, z0)
    add_point(polygons, x1, y1, z1)
    add_point(polygons, x2, y2, z2)
    
def draw_polygons( polygons, screen, color ):
    if len( polygons ) < 3:
        print "Need at least 3 points to draw a triangle"
        
    p = 0
    while p < len( polygons ) - 2:
        vA = [polygons[p + 1][0] - polygons[p][0], polygons[p + 1][1] - polygons[p][1], polygons[p + 1][2] - polygons[p][2]]
        vB = [polygons[p + 2][0] - polygons[p + 1][0], polygons[p + 2][1] - polygons[p + 1][1], polygons[p + 2][2] - polygons[p + 1][2]]
        vN = [vA[1] * vB[2] - vA[2] * vB[1], vA[2] * vB[0] - vA[0] * vB[2], vA[0] * vB[1] - vA[1] * vB[0]]
        v = [0, 0, -1]
        if (vN[0] * v[0] + vN[1] * v[1] + vN[2] * v[2] < 0):
            draw_line( screen, polygons[p][0], polygons[p][1],
                       polygons[p+1][0], polygons[p+1][1], color )
            draw_line(screen, polygons[p + 1][0], polygons[p + 1][1],
                      polygons[p + 2][0], polygons[p + 2][1], color)
            draw_line(screen, polygons[p + 2][0], polygons[p + 2][1],
                      polygons[p][0], polygons[p][1], color)
        p+= 3

def add_box( polygons, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    add_polygon(polygons, x, y, z, x, y1, z, x1, y1, z)
    add_polygon(polygons, x, y1, z1, x, y, z1, x1, y, z1)
    add_polygon(polygons, x, y, z1, x, y, z, x1, y, z)
    add_polygon(polygons, x, y1, z1, x, y1, z1, x1, y1, z1)
    add_polygon(polygons, x, y, z1, x, y1, z1, x, y1, z)
    add_polygon(polygons, x, y1, z, x, y, z, x, y, z1)
    add_polygon(polygons, x1, y, z, x1, y, z1, x, y, z1)
    add_polygon(polygons, x1, y, z, x1, y1, z, x1, y1, z1)
    add_polygon(polygons, x1, y1, z, x1, y, z, x, y, z)
    add_polygon(polygons, x1, y1, z1, x1, y1, z, x, y1, z)
    add_polygon(polygons, x1, y1, z1, x1, y, z1, x1, y, z)
    add_polygon(polygons, x1, y, z1, x1, y1, z1, x, y1, z1)

def add_sphere( polygons, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps

    pts = []

    n = num_steps
    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:
            
            i = lat * (n + 1) + longt
            #index2 = lat * num_steps + (longt + 1)
            #index3 = lat * num_steps + (longt - 1)
            #if (longt > 0):
            #    add_edge( points, temp[index3][0], temp[index3][1], temp[index3][2], temp[index][0], temp[index][1], temp[index][2] )
            #add_edge( points, temp[index][0], temp[index][1], temp[index][2], temp[index2][0], temp[index2][1], temp[index2][2] )
            #pts.append(temp[index])
            a = i + n
            b = i + n + 1
            c = i + 1
            d = longt
            e = longt + 1 #shorthand vars to make easier below
            
            if lat == lat_stop - 1: #edge-case
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[d][0], temp[d][1], temp[d][2], temp[e][0], temp[e][1], temp[e][2])
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[e][0], temp[e][1], temp[e][2], temp[c][0], temp[c][1], temp[c][2])
            else:
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[a][0], temp[a][1], temp[a][2], temp[b][0], temp[b][1], temp[b][2])
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[b][0], temp[b][1], temp[b][2], temp[c][0], temp[c][1], temp[c][2])
                
            longt+= 1
        #pts.append(0)
        lat+= 1

    #n = lat_stop
    #for i in range(len(pts)):
     #   if (i + n < len(pts)):
      #      a = i + n
       # else:
        #    a = i + n - len(pts)
        #if (i + n + 1 < len(pts)):
        #    b = i + n + 1
        #else:
        #    b = i + n + 1 - len(pts)
        #if (i + 1 < len(pts)):
        #    c = i + 1
        #else:
        #    c = 0
        #if (i + n + 1 < len(pts) and (i + 1) % n != 0):

    #longs = []
    #a = 0
    #for i in range(len(pts)):
    #    if (pts[i] == 0):
    #        longs.append(pts[a:i])
    #        a = i + 1

    #for i in range(len(longs)):
    #    for j in range(len(longs[i])):
    #        if (i + 1 < len(longs) and j + 1 < len(longs[i])):
    #            add_polygon(polygons, longs[i][j][0], longs[i][j][1], longs[i][j][2], longs[i + 1][j][0], longs[i + 1][j][1], longs[i + 1][j][2], longs[i + 1][j + 1][0], longs[i + 1][j + 1][1], longs[i + 1][j + 1][2])
    #            add_polygon(polygons, longs[i][j][0], longs[i][j][1], longs[i][j][2], longs[i + 1][j + 1][0], longs[i + 1][j + 1][1], longs[i + 1][j + 1][2], longs[i][j + 1][0], longs[i][j + 1][1], longs[i][j + 1][2])
    #print(longs)

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
        
def add_torus( polygons, cx, cy, cz, r0, r1, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_torus( temp, cx, cy, cz, r0, r1, step )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps

    pts = []

    n = num_steps
    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:

            i = lat * (n + 1) + longt
            #pts.append(temp[index])
            a = i + n
            b = i + n + 1
            c = i + 1
            d = longt
            e = longt + 1 #shorthand vars to make easier below
            
            if lat == lat_stop - 1: #edge-case
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[d][0], temp[d][1], temp[d][2], temp[e][0], temp[e][1], temp[e][2])
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[e][0], temp[e][1], temp[e][2], temp[c][0], temp[c][1], temp[c][2])
            else:
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[a][0], temp[a][1], temp[a][2], temp[b][0], temp[b][1], temp[b][2])
                add_polygon(polygons, temp[i][0], temp[i][1], temp[i][2], temp[b][0], temp[b][1], temp[b][2], temp[c][0], temp[c][1], temp[c][2])
                
            longt+= 1
        #pts.append(0)
        lat+= 1

    #n = lat_stop
    #for i in range(len(pts)):
    #    if (i + n < len(pts)):
    #        a = i + n
    #    else:
    #        a = i + n - len(pts)
    #    if (i + n + 1 < len(pts)):
    #        b = i + n + 1
    #    else:
    #        b = i + n + 1 - len(pts)
    #    if (i + 1 < len(pts)):
    #        c = i + 1
    #    else:
    #       c = 0
    
    #    add_polygon(polygons, pts[i][0], pts[i][1], pts[i][2], pts[a][0], pts[a][1], pts[a][2], pts[b][0], pts[b][1], pts[b][2])
    #    add_polygon(polygons, pts[i][0], pts[i][1], pts[i][2], pts[b][0], pts[b][1], pts[b][2], pts[c][0], pts[c][1], pts[c][2])
        
def generate_torus( points, cx, cy, cz, r0, r1, step ):

    rotation = 0
    rot_stop = MAX_STEPS
    circle = 0
    circ_stop = MAX_STEPS

    while rotation < rot_stop:
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

