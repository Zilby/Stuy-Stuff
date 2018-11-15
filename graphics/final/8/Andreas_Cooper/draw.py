from display import *
from matrix import *
from gmath import calculate_dot
from math import cos, sin, pi

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
        if calculate_dot( points, p ) >= 0:
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                      points[p+1][0], points[p+1][1], points[p+1][2], color )
            draw_line( screen, points[p+1][0], points[p+1][1], points[p+1][2],
                        points[p+2][0], points[p+2][1], points[p+2][2], color )
            draw_line( screen, points[p][0], points[p][1], points[p][2],
                          points[p+1][0], points[p+1][1], points[p+1][2], color )
            scanline_convert(screen,points[p][0],points[p][1],points[p][2],
                             points[p+1][0],points[p+1][1],points[p+1][2],
                             points[p+2][0],points[p+2][1],points[p+2][2],
                             color)
        p+= 3

def scanline_convert(screen, x0, y0, z0, x1, y1, z1, x2, y2, z2, color):
    lowest = []
    middle = []
    highest = []
    x0 = round(x0)
    x1 = round(x1)
    x2 = round(x2)
    y0 = round(y0)
    y1= round(y1)
    y2 = round(y2)
    if y0 == min(y0,y1,y2):
        lowest = [x0,y0,z0]
        if y1 == min(y1,y2):
            middle = [x1,y1,z1]
            highest = [x2,y2,z2]
        else:
            middle = [x2,y2,z2]
            highest = [x1,y1,z1]
    elif y1 == min(y0,y1,y2):
        lowest = [x1,y1,z1]
        if y0 == min(y0,y2):
            middle = [x0,y0,z0]
            highest = [x2,y2,z2]
        else:
            middle = [x2,y2,z2]
            highest = [x0,y0,z0]
    else:
        lowest = [x2,y2,z2]
        if y0 == min(y0,y1):
            middle = [x0,y0,z0]
            highest = [x1,y1,z1]
        else:
            middle = [x1,y1,z1]
            highest = [x0,y0,z0]
        #this variable is the x coord on the line from lowest to highest with the same y coord as the middle point
        #not fun to coordinate bash
    if (round(highest[1] - lowest[1]) == 0):
        tmpx = highest[0]
        tmpz = highest[2]
    else:
        tmpx = round(lowest[0] + round(middle[1] - lowest[1]) * round(highest[0] - lowest[0]) / round(highest[1] - lowest[1]))
    #and round two for z-buffering
        tmpz = round(lowest[2] + round(middle[1] - lowest[1]) * round(highest[2] - lowest[2]) / round(highest[1] - lowest[1]))

    if (round(middle[1] - lowest[1]) > 0):
        for i in range(0,int(middle[1] -lowest[1])):
            numy = round(middle[1] - lowest[1]) 
            xi = round(lowest[0] + (tmpx - lowest[0]) * i / numy)
            xf = round(lowest[0] + (middle[0] - lowest[0]) * i / numy)
            zi = round(lowest[2] + (tmpz - lowest[2]) * i / numy)
            zf = round(lowest[2] + (middle[2] - lowest[2]) * i / numy)
            draw_line(screen, xi, i + int(lowest[1]),zi, xf, i + int(lowest[1]),zf, color)
    if (round(highest[1]- middle[1]) >0):
        for i in range(0, int(highest[1] - middle[1])):
            numy = round(highest[1] - lowest[1])
            xi = round(tmpx + (highest[0] - tmpx) * i / numy)
            xf = round(middle[0] + (highest[0] - middle[0]) * i / numy)
            zi = round(tmpz + (highest[2] - tmpz) * i / numy)
            zf = round(middle[2] + (highest[2] - middle[2]) * i / numy)
            draw_line(screen, xi, i + int(middle[1]), zi,xf, i + int(middle[1]),zf, color)

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

def add_point( matrix, x, y, z=-1000000000 ):
    matrix.append( [x, y, z, 1] )


def draw_line( screen, x0, y0, z0, x1, y1, z1, color ):
    if x0 > x1 or (x0 == x1 and y0 > y1):
        xtmp,ytmp,ztmp = x0,y0,z0
        x0,y0,z0 = x1,y1,z1
        x1,y1,z1 = xtmp,ytmp,ztmp
    
    if x0 != x1:
        m = (y0-y1)/float(x0-x1)
    else:
        m = 999999
    
    if m < 0:#transformation: reflect across x-axis
        y0,y1 = -y0,-y1
        z0,z1 = -z0,-z1
    
    if abs(m) > 1 :#transformation: reflect across y=x
        tmp0,tmp1 = x0,x1#swap((x0,x1),(y0,y1))
        x0,x1 = y0,y1
        y0,y1 = tmp0,tmp1
        z0,z1 = -z0,-z1
    
    A = 2 * (y1-y0)
    B = 2 * (x0-x1)
    C = 2 * (z1-z0)
    x,y,z = x0,y0,z0
    d = A + B/2
    e = A + C/2
    
    
    while x <= x1:
        if m > 1: #transformation: reflect back across y=x
            plot(screen, color, y, x, -z)
        elif 0 <= m <= 1: #transformation: none
            plot(screen, color, x, y, z)
        elif -1 <= m < 0: #transformation: reflect back across x-axis
            plot(screen, color, x, -y, -z)
        else: #transformation: reflect back across y=x, then back across x-axis
            plot(screen, color, y, -x, z)
        if d > 0:
            y+=1
            d+=B
        if e > 0:
            z+=1
            e+=B
        x+=1
        d+=A
        e+=C
