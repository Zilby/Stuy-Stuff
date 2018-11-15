from display import *
from matrix import *
from gmath import *
import random
from math import cos, sin, pi

MAX_STEPS = 100


zbuffer = []
for y in xrange(500):
        zbuffer.append([])
        for x in xrange(500):
            zbuffer[y].append(2147483647)

def new_zbuffer():
    global zbuffer
    zbuffer = []
    for y in xrange(500):
        zbuffer.append([])
        for x in xrange(500):
            zbuffer[y].append(2147483647) 
            #something with the way z-coords work requires zbuffers to be flipped? smaller zs are shown


def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )


    
def scanline_convert(screen, v0, v1, v2, color):
    vertices = [[v0[0], v0[1], v0[2]],
                [v1[0], v1[1], v1[2]],
                [v2[0], v2[1], v2[2]]]
    vertices.sort(key=lambda x:x[1])
    bx = round(vertices[0][0])
    by = round(vertices[0][1])
    bz = round(vertices[0][2])
    mx = round(vertices[1][0])
    my = round(vertices[1][1])
    mz = round(vertices[1][2])
    tx = round(vertices[2][0])
    ty = round(vertices[2][1])
    tz = round(vertices[2][2])

    x1 = bx
    x2 = bx
    y = by

    #color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    if ty - by == 0:
        delta0 = 0
    else:
        delta0 = ((tx - bx))/(ty-by)
    
    if ty - my == 0:
        delta1 = 0
    else:
        delta1 = float(tx - mx)/(ty - my)

    if my - by == 0:
        delta2 = 0
    else:
        delta2 = float(mx - bx) / (my - by)

    while (y < ty):        
        
        if y == my:
            x2 = mx

        if y >= my:
            delta = delta1            
        else:
            delta = delta2
        
        x1 += delta0
        x2 += delta
        y += 1
        z = min(bz, mz, tz)
        draw_line(screen,int(x1), int(y), z, int(x2), int(y), z, color)

        
def draw_polygons( points, screen, color ):

    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return
    #color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    p = 0
    while p < len( points ) - 2:
        if calculate_dot( points, p ) >= 0:
            #Shading stuff
            #I = IA * KA + IP * KD * (L . N) + Ip * Ks * [( 2N * (N . L) - L ) . V ]^n
            #print color
            ia = color 
            #hardcoded constants + light stuff for now
            ka = 0.5
            kd = 0.5
            ks = 0.2
            ip = [255, 255, 255]
            l = [15, 15, -5]
            v = [0, 0, -1]

            iaR = ia[0] * ka
            iaG = ia[1] * ka
            iaB = ia[2] * ka
            
            dpl = dot_prod_light(points, p, l)
            idR = ip[0] * kd * dpl
            idG = ip[1] * kd * dpl
            idB = ip[2] * kd * dpl

            isR = ip[0] * ks * spec_light(points, p, l, v)
            isG = ip[1] * ks * spec_light(points, p, l, v)
            isB = ip[2] * ks * spec_light(points, p, l, v)
            
            r = iaR + idR + isR
            g = iaG + idG + isG
            b = iaB + idB + isB

            # is this how we do? idk
            i = [int(r), int(g), int(b)]
            if i[0] > 255:
                i[0] = 255
            if i[0] < 0:
                i[0] = 0
            if i[1] > 255:
                i[1] = 255
            if i[1] < 0:
                i[1] = 0
            if i[2] > 255:
                i[2] = 255
            if i[2] < 0:
                i[2] = 0
                
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                       points[p+1][0], points[p+1][1], points[p+1][2], i )
            draw_line( screen, points[p+1][0], points[p+1][1], points[p+1][2],
                       points[p+2][0], points[p+2][1], points[p+2][2], i )
            draw_line( screen, points[p+2][0], points[p+2][1], points[p+2][2],
                       points[p][0], points[p][1], points[p][2], i )
            scanline_convert(screen, points[p],points[p+1], points[p+2], i) 
        p+= 3

def spec_light(points, p, l, v):
    #return 0
    #[( 2N * (N . L) - L ) . V ]^n
    n = get_norm(points, p)
    nl = dot_prod_light(points, p, l)
    #print "nl: " + str(nl)
    #print "n: " + str(n)
    i = [2 * x * nl for x in n]
    i[0] = i[0] - l[0]
    i[1] = i[1] - l[1]
    i[2] = i[2] - l[2]
    i = dot_prod(i, v) 
    return i ** 3
    

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
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, z0, x1, y1, z1, color ):
    global zbuffer
    dx = x1 - x0
    dy = y1 - y0
    z = z0
    dz = z1 - z0
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
            if zbuffer[int(y)][int(x0)] > z:
                plot(screen, color,  x0, y)
                zbuffer[int(y)][int(x0)] = z

            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            if zbuffer[int(y0)][int(x)] > z:
                plot(screen, color,  x, y0)
                zbuffer[int(y0)][int(x)] = z
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            if zbuffer[int(y)][int(x)] > z:
                plot(screen, color,  x, y)
                zbuffer[int(y)][int(x)] = z
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
            if zbuffer[int(y)][int(x)] > z:
                plot(screen, color,  x, y)
                zbuffer[int(y)][int(x)] = z
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
            if zbuffer[int(y)][int(x)] > z:
                plot(screen, color,  x, y)
                zbuffer[int(y)][int(x)] = z
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
            if zbuffer[int(y)][int(x)] > z:
                plot(screen, color,  x, y)
                zbuffer[int(y)][int(x)] = z
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

