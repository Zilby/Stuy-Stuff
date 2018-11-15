from display import *
from matrix import *
from gmath import *
from math import cos, sin, pi

MAX_STEPS = 100
zbuffer = []

def new_buffer():
    global zbuffer
    for y in range(500):
        zbuffer.append([])
        for x in range(500):
            zbuffer[y].append(10000000)
    
new_buffer()

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )

def ambient( color, k ):
    temp = []
    for i in range(3):
        temp.append(float(color[i] * k))
    return temp

def diffuse( color, k, points, p, l ):
    temp = []
    dot = calculate_light_dot( points, p, l )
    for i in color:
        temp.append(float(i) * k * dot)
    return temp

def specular( color, k, points, p, l, v ):
    temp = []
    multiplier = []
    n1 = get_norm( points, p )
    n2 = calculate_light_dot( points, p, l )
    
    for i in range(3):
        multiplier.append(2 * n1[i] * n2)
        multiplier[i] = ( multiplier[i] - l[i] )
        
    multiplier= dot_prod( multiplier, v )
    for i in range(3):
        temp.append(float(color[i]) * k * multiplier**10)
    return temp

def get_light( color, points, p, l, v ):
    ka = 0.5
    kd = 0.3
    ks = 0.3

    iamb = ambient( color, ka )
    idif = diffuse( color, kd, points, p, l )
    ispec = specular( color, ks, points, p, l, v )

    light = []
    for i in range(3):
        a = int(iamb[i] + idif[i] + ispec[i])
        if a > 255:
            light.append(255)
        elif a < 0:
            light.append(0)
        else:
            light.append(a)
    print light
    return light
    
    


def scanline_convert( screen, color, p0, p1, p2 ):
    points = [p0, p1, p2]
    points.sort(key=lambda tup: tup[1])
    
    xb = round(points[0][0])
    xm = round(points[1][0])
    xt = round(points[2][0])
    
    yb = round(points[0][1])
    ym = round(points[1][1])
    yt = round(points[2][1])
    
    z = min(round(points[0][2]),round(points[1][2]),round(points[2][2]))
    
    if (yt == yb):
        d0 = 0
    else:
        d0 = (xt - xb) / (yt - yb)

    if (ym == yb):
        d1 = 0
    else:
        d1 = (xm - xb) / (ym - yb)

    if (yt == ym):
        d2 = 0
    else:
        d2 = (xt - xm) / (yt - ym)

    xl = xb
    xr = xb
    if (ym == yb):
        xr = xm
    while (yb < yt):
        xl = xl + d0
        yb = yb + 1
        if (yb <= ym):
            xr = xr + d1
        else:
            xr = xr + d2
        draw_line( screen, xl, yb, z, xr, yb, z, color)
        
def draw_polygons( points, screen, color ):
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return
    p = 0
    while p < len( points ) - 2:

        if calculate_dot( points, p ) >= 0:
            l = [ 15, 15, -5 ]
            v = [ 0, 0, -1 ]
            lcolor = get_light( color, points, p, l, v )
            
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                       points[p+1][0], points[p+1][1], points[p+1][2], lcolor )
            draw_line( screen, points[p+1][0], points[p+1][1], points[p+1][2],
                       points[p+2][0], points[p+2][1], points[p+2][2], lcolor )
            draw_line( screen, points[p+2][0], points[p+2][1], points[p+2][2],
                       points[p][0], points[p][1], points[p][2], lcolor )
            scanline_convert( screen, lcolor, points[p], points[p+1], points[p+2] )
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
                   matrix[p+1][0], matrix[p+1][1], matrix[p+1][2], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0,z0, x1, y1, z1, color ):
    global zbuffer
    dx = x1 - x0
    dy = y1 - y0
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
                plot(screen, color, x, y)
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
                plot(screen, color, x, y)
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
                plot(screen, color, x, y)
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
                plot(screen, color, x, y)
                zbuffer[int(y)][int(x)] = z
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

