from display import *
from matrix import *
from gmath import calculate_dot, z_normal
from math import cos, sin, pi
import random

MAX_STEPS = 100

def get_lighting(p0, p1, p2, a, d, s):
    #Ambient lighting
    Ir = a[0]
    Ig = a[1]
    Ib = a[2]
    N = z_normal(p0, p1, p2)

    #Diffuse lighting
    for l in d: #For each light in the diffuse lighting
        #l contains an array of two values (first is RGB intensity, second is direction)
        r = l[0][0]
        g = l[0][1]
        b = l[0][2]
        if (N != [0, 0, 0]):
            scalar_mult([N], 1 / math.sqrt(N[0] ** 2 + N[1] ** 2 + N[2] ** 2)) #Normalize
        v = l[1]
        if (v != [0, 0, 0]):
            scalar_mult([v], 1 / math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2))
        k = N[0] * v[0] + N[1] * v[1] + N[2] * v[2] #Dot product
        if k > 0:
            Ir = Ir + r * k
            Ig = Ig + g * k
            Ib = Ib + b * k

    #Specular lighting
    for l in s:
        r = l[0][0]
        g = l[0][1]
        b = l[0][2]
        #Multiplier: (2N(N . L) - L) . V    V is [0, 0, -1]
        if (N != [0, 0, 0]):
            scalar_mult([N], 1 / math.sqrt(N[0] ** 2 + N[1] ** 2 + N[2] ** 2)) #Normalize
        v = l[1]
        if (v != [0, 0, 0]):
            scalar_mult([v], 1 / math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2))
        k1 = N[0] * v[0] + N[1] * v[1] + N[2] * v[2] #Dot product # 1
        Norig = z_normal(p0, p1, p2)
        scalar_mult([Norig], 2 * k1)
        Norig[0] = Norig[0] - l[1][0]
        Norig[1] = Norig[1] - l[1][1]
        Norig[2] = Norig[2] - l[1][2]
        view = [0, 0, -1]
        scalar_mult([view], 1 / math.sqrt(view[0] ** 2 + view[1] ** 2 + view[2] ** 2))
        if (Norig != [0, 0, 0]):
            scalar_mult([Norig], 1 / math.sqrt(Norig[0] ** 2 + Norig[1] ** 2 + Norig[2] ** 2))
        k = Norig[0] * view[0] + Norig[1] * view[1] + Norig[2] * view[2] #Dot product # 2
        if k > 0:
            k = k ** 8
            Ir = Ir + r * k
            Ig = Ig + g * k
            Ib = Ib + b * k

    #Set limits
    if Ir > 255:
        Ir = 255
    if Ig > 255:
        Ig = 255
    if Ib > 255:
        Ib = 255
    print([Ir, Ig, Ib])
    return [int(Ir), int(Ig), int(Ib)] #Must be int values for it to work

def scanline_convert(screen, x0, y0, z0, x1, y1, z1, x2, y2, z2, color):
    y = [[y0, x0, z0], [y1, x1, z1], [y2, x2, z2]]
    y.sort()
    #print y
    yb = y[0][0]
    xb = y[0][1]
    zb = y[0][2]
    ym = y[1][0]
    xm = y[1][1]
    zm = y[1][2]
    yt = y[2][0]
    xt = y[2][1]
    zt = y[2][2]
    xb2 = xb
    xb1 = xb
    i = yb + 1
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    #draw_line(screen, xb1, i - 1, xb2, i - 1, color)
    while (ym >= i):
        diff1 = ((i - yb) / (yt - yb)) * (zt - zb)
        diff2 = ((i - yb) / (ym - yb)) * (zm - zb)
        xb1 = xb + float(xt - xb) / (yt - yb) * (i - yb)
        xb2 = xb + float(xm - xb) / (ym - yb) * (i - yb)
        draw_line(screen, xb1, i, zb + diff1, xb2, i, zb + diff2, color)
        i = i + 1
    #draw_line(screen, xb1, i, xb2, i, color)
    while (yt >= i):
        diff1 = ((i - yb) / (yt - yb)) * (zt - zb)
        diff2 = ((i - ym) / (yt - ym)) * (zt - zm)
        xb1 = xb + float(xt - xb) / (yt - yb) * (i - yb)
        xb2 = xm + float(xt - xm) / (yt - ym) * (i - ym)
        draw_line(screen, xb1, i, zb + diff1, xb2, i, zm + diff2, color)
        i = i + 1
    #draw_line(screen, xb1, i, xb2, i, color)
    """del1 = 0
    del0 = 0
    xb2 = 0
    if (yt - yb == 0.0):
        del0 = 0
        xb2 = xb
        if (ym - yb == 0.0 and yt - ym !=0):
            del1 = (xt - xm) / (yt - ym)
            xb2 = xm
        else:
            if (ym - yb != 0.0):
                del1 = (xm - xb) / (ym - yb)
                xb2 = xb
            else:
                xb2 = xm
    else:
        del0 = (xt - xb) / (yt - yb)
        if (ym - yb == 0.0):
            del1 = (xt - xm) / (yt - ym)
            xb2 = xm
        else:
            del1 = (xm - xb) / (ym - yb)
            xb2 = xb
    xb1 = xb
    while (ym >= yb):
        xb1 = xb1 + del0
        xb2 = xb2 + del1
        yb = yb + 1
        draw_line(screen, xb1, yb, xb2, yb, color)
    if (yt - ym == 0):
        del1 = 0
    else:
        del1 = (xt - xm) / (yt - ym)
    while (yt >= yb):
        xb1 = xb1 + del0
        xb2 = xb2 + del1
        yb = yb + 1
        draw_line(screen, xb1, yb, xb2, yb, color)"""

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )
    
def draw_polygons( points, screen, color, a, d, s ):

    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len( points ) - 2:

        if calculate_dot( points, p ) >= 0:
            #color = get_lighting(points[p], points[p + 1], points[p + 2], a, d, s)
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                       points[p+1][0], points[p+1][1], points[p + 1][2], color )
            draw_line( screen, points[p+1][0], points[p+1][1], points[p + 1][2],
                       points[p+2][0], points[p+2][1], points[p + 2][2], color )
            draw_line( screen, points[p+2][0], points[p+2][1], points[p + 2][2],
                       points[p][0], points[p][1], points[p][2], color )
            scanline_convert(screen, points[p][0], points[p][1], points[p][2], points[p + 1][0], points[p + 1][1], points[p + 1][2], points[p + 2][0], points[p + 2][1], points[p + 2][2], color)
        p+= 3



def add_box( points, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon( points, 
                 x, y, z, 
                 x, y1, z,
                 x1, y1, z)
    add_polygon( points, 
                 x1, y1, z, 
                 x1, y, z,
                 x, y, z)
    #back
    add_polygon( points, 
                 x1, y, z1, 
                 x1, y1, z1,
                 x, y1, z1)
    add_polygon( points, 
                 x, y1, z1, 
                 x, y, z1,
                 x1, y, z1)
    #top
    add_polygon( points, 
                 x, y, z1, 
                 x, y, z,
                 x1, y, z)
    add_polygon( points, 
                 x1, y, z, 
                 x1, y, z1,
                 x, y, z1)
    #bottom
    add_polygon( points, 
                 x1, y1, z1, 
                 x1, y1, z,
                 x, y1, z)
    add_polygon( points, 
                 x, y1, z, 
                 x, y1, z1,
	         x1, y1, z1)
    #right side
    add_polygon( points, 
                 x1, y, z, 
                 x1, y1, z,
                 x1, y1, z1)
    add_polygon( points, 
                 x1, y1, z1, 
                 x1, y, z1,
                 x1, y, z)
    #left side
    add_polygon( points, 
                 x, y, z1, 
                 x, y1, z1,
                 x, y1, z)
    add_polygon( points, 
                 x, y1, z, 
                 x, y, z,
                 x, y, z1) 


def add_sphere( points, cx, cy, cz, r, step ):
    
    num_steps = MAX_STEPS / step
    temp = []

    generate_sphere( temp, cx, cy, cz, r, step )
    num_points = len( temp )

    lat = 0
    lat_stop = num_steps
    longt = 0
    longt_stop = num_steps

    num_steps += 1

    while lat < lat_stop:
        longt = 0
        while longt < longt_stop:
            
            index = lat * num_steps + longt

            px0 = temp[ index ][0]
            py0 = temp[ index ][1]
            pz0 = temp[ index ][2]

            px1 = temp[ (index + num_steps) % num_points ][0]
            py1 = temp[ (index + num_steps) % num_points ][1]
            pz1 = temp[ (index + num_steps) % num_points ][2]
            
            if longt != longt_stop - 1:
                px2 = temp[ (index + num_steps + 1) % num_points ][0]
                py2 = temp[ (index + num_steps + 1) % num_points ][1]
                pz2 = temp[ (index + num_steps + 1) % num_points ][2]
            else:
                px2 = temp[ (index + 1) % num_points ][0]
                py2 = temp[ (index + 1) % num_points ][1]
                pz2 = temp[ (index + 1) % num_points ][2]
                
            px3 = temp[ index + 1 ][0]
            py3 = temp[ index + 1 ][1]
            pz3 = temp[ index + 1 ][2]
      
            if longt != 0:
                add_polygon( points, px0, py0, pz0, px1, py1, pz1, px2, py2, pz2 )

            if longt != longt_stop - 1:
                add_polygon( points, px2, py2, pz2, px3, py3, pz3, px0, py0, pz0 )
            
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
    num_points = len(temp)

    lat = 0
    lat_stop = num_steps
    longt_stop = num_steps
    
    while lat < lat_stop:
        longt = 0

        while longt < longt_stop:
            index = lat * num_steps + longt

            px0 = temp[ index ][0]
            py0 = temp[ index ][1]
            pz0 = temp[ index ][2]

            px1 = temp[ (index + num_steps) % num_points ][0]
            py1 = temp[ (index + num_steps) % num_points ][1]
            pz1 = temp[ (index + num_steps) % num_points ][2]

            if longt != num_steps - 1:            
                px2 = temp[ (index + num_steps + 1) % num_points ][0]
                py2 = temp[ (index + num_steps + 1) % num_points ][1]
                pz2 = temp[ (index + num_steps + 1) % num_points ][2]

                px3 = temp[ (index + 1) % num_points ][0]
                py3 = temp[ (index + 1) % num_points ][1]
                pz3 = temp[ (index + 1) % num_points ][2]
            else:
                px2 = temp[ ((lat + 1) * num_steps) % num_points ][0]
                py2 = temp[ ((lat + 1) * num_steps) % num_points ][1]
                pz2 = temp[ ((lat + 1) * num_steps) % num_points ][2]

                px3 = temp[ (lat * num_steps) % num_points ][0]
                py3 = temp[ (lat * num_steps) % num_points ][1]
                pz3 = temp[ (lat * num_steps) % num_points ][2]


            add_polygon( points, px0, py0, pz0, px1, py1, pz1, px2, py2, pz2 );
            add_polygon( points, px2, py2, pz2, px3, py3, pz3, px0, py0, pz0 );        
            
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
        draw_line( screen, matrix[p][0], matrix[p][1], matrix[p][2],
                   matrix[p+1][0], matrix[p+1][1], matrix[p][2], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, z0, x1, y1, z1, color ):
    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0
    dz1 = 0
    dz2 = 0
    z = z0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    if x1 != x0:
        dz1 = float(z1 - z0) / (x1 - x0)
    if y1 != y0:
        dz2 = float(z1 - z0) / (y1 - y0)

    if dx == 0:
        y = y0

        while y <= y1:
            plot(screen, color,  x0, y, z)
            y = y + 1
            z = z + dz2
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0, z)
            x = x + 1
            z = z + dz1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        z = z0
        while x <= x1:
            plot(screen, color, x, y, z)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
            z = z + dz1
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        z = z0
        while y <= y1:
            plot(screen, color, x, y, z)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
            z = z + dz2
            
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        z = z0
        while x <= x1:
            plot(screen, color, x, y, z)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
            z = z + dz1
            
    else:
        d = 0
        x = x0
        y = y0
        z = z0
        while y <= y1:
            plot(screen, color, x, y, z)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx
            z = z + dz2
        
