from display import *
from matrix import *
from gmath import *
from math import cos, sin, pi
import random
MAX_STEPS = 100

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )
def draw_polygons( points, screen, color ):

    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len( points ) - 2:
        ## If polygon is visible
        if calculate_dot( points, p ) >= 0:
            draw_line( screen, points[p][0], points[p][1],
                       points[p+1][0], points[p+1][1], color )
            draw_line( screen, points[p+1][0], points[p+1][1],
                       points[p+2][0], points[p+2][1], color )
            draw_line( screen, points[p+2][0], points[p+2][1],
                       points[p][0], points[p][1], color )
            scanline_convert(screen, color, points[p][0],points[p][1],points[p+1][0],points[p+1][1],points[p+2][0], points[p+2][1])
        p+= 3

def ambient_light(ia, ka):
    return [c*ka for c in ia]

def diffuse_light(ip, kd, points, p, lv):
    dot_prod = calculate_light_dot(points, p, lv )
    return [kd*ip[i]*dot_prod for i in range(3)]
    
def specular_light(ip, ks,points, p, lv,vv):
    prod = calculate_light_dot(points, p, lv)
    normal = calculate_normal_b(points, p)
    result = [(2*prod*normal[i]) - lv[i] for i in range(3)]
    result = normalize(result,magnitude(result))
    prod = calculate_vectors_dot(result, vv)
    return [ks*ip[i]*(prod**70) for i in range(3)]

def draw_polygons( points, screen, color ):
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return
    p = 0
    while p < len( points ) - 2:
        base_color = [100,145,230]
        light_vector = [15,15,-5]
        view_vector = [0,0,-1]
        ka = .5
        kd = .6
        ks = .7
        amb = ambient_light(base_color, ka)
        if calculate_dot( points, p ) >= 0:
            diff = diffuse_light([155,155,155],kd, points, p, light_vector)
            spec = specular_light([250,250,0],ks,points,p,light_vector,view_vector)
            color =  [int(amb[i]+diff[i]+spec[i]) for i in range(3)] 
            
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                       points[p+1][0], points[p+1][1], points[p+1][2],color )
            draw_line( screen, points[p+1][0], points[p+1][1], points[p+1][2],
                        points[p+2][0], points[p+2][1], points[p+2][2], color )
            draw_line( screen, points[p+2][0], points[p+2][1],points[p+2][2],
                       points[p][0], points[p][1], points[p][2], color )
            scanline_convert(screen, color, points[p][0],points[p][1],points[p][2],points[p+1][0],points[p+1][1],points[p+1][2],points[p+2][0], points[p+2][1],points[p+2][2])

        p+= 3
def scanline_convert(screen, color, x0, y0, z0, x1, y1, z1, x2, y2, z2):
    points = [(x0,y0,z0), (x1, y1,z1), (x2, y2,z2)]
    points = sorted(points, key=lambda tup: tup[1])
    xb = round(points[0][0])
    yb = round(points[0][1])
    zb = round(points[0][2])
    xm = round(points[1][0])
    ym = round(points[1][1])
    zm = round(points[1][2])
    xt = round(points[2][0])
    yt = round(points[2][1])
    zt = round(points[2][2])
    if (-.001 < (yt - yb) < .001):
        dx0 = 0
    else:
        dx0 = (xt-xb)/(yt-yb)

    if (-.001 < (xt - xb) < .001):
        dz0 = 0
    else:
        dz0 = (zt-zb)/(xt-xb)

    if (-.001 < (xm - xb) < .001):
        dz1 = 0
    else:
        dz1 = (zm-zb)/(xm-xb)

    x0 = xb
    x1 = xb
    y = yb
    z0 = zb
    z1 = zb

    if (-.001 <= (ym - yb) <= .001):
        dx1 = 0
        x1 = xm
        z1 = zm
    else:
        dx1 = (xm-xb)/(ym-yb)

    while (y < ym):
        draw_line(screen, x0, y, z0, x1, y, z1, color)
        x0 += dx0
        z0 += dz0
        z1 += dz1
        x1 += dx1
        y += 1

    if (-.001 < (yt - ym) < .001):
        dx1 = 0
    else:
        dx1 = (xt-xm)/(yt-ym)

    if (-.001 < (xt - xm) < .001):
        dz1 = 0
    else:
        dz1 = (zt-zm)/(xt-xm)

    while (y < yt):
        draw_line(screen, x0, y,z0, x1, y, z1,color)
        x0 += dx0
        x1 += dx1
        z0 += dz0
        z1 += dz1
        y += 1
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
                   matrix[p+1][0], matrix[p+1][1], matrix[p+1][2], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, z0, x1, y1, z1, color ): 
    if (x0 > x1 or (x0 ==  x1 and y0 > y1)):
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
        tmp = z0
        z0 = z1
        z1 = tmp
    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0
    x = x0
    y = y0
    z = z0
    if dx:
        m = dy / float(dx)
    else:
        m = 200
    if dx:
        dzdx = dz/dx
    if dy:
        dzdy = dz/dy
    else:
        dzdy = 0

    A = 2*dy
    B = -2*dx
    C = 2*dz

    if (0 <= m < 1):
        d = A + B/2
        while(x <= x1):
            plot(screen, color, x, y, z)
            if (d > 0):
                y += 1
                d += B
            x += 1
            z += dzdx
            d += A
    elif(-1 <= m < 0):
        d = A - B/2
        while(x <= x1):
            plot(screen, color, x, y, z)
            if (d < 0):
                y -= 1
                d -= B
            x += 1
            z += dzdx
            d += A
    elif(m < -1):
        d = A/2 + B
        while (y >= y1):
            plot(screen, color, x, y,z)
            if (d > 0):
                x += 1
                d += A 
            y -= 1
            z -= dzdy
            d -= B
    else:
        d = A/2 + B
        while(y <= y1):
            plot(screen, color, x, y,z)
            if (d < 0):
                x += 1
                d += A
            y += 1
            z += dzdy
            d += B

