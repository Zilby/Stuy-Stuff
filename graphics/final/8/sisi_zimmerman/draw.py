from display import *
from matrix import *
from gmath import calculate_dot
from math import cos, sin, pi
import random

MAX_STEPS = 100

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )
    
def draw_polygons( points, screen, color , zbuff):

    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len( points ) - 2:

        if calculate_dot( points, p ) >= 0:
            #draw_line( screen, points[p][0], points[p][1], points[p][2],
            #           points[p+1][0], points[p+1][1], points[p+1][2], color )
            #draw_line( screen, points[p+1][0], points[p+1][1], points[p+1][1],
            #           points[p+2][0], points[p+2][1], points[p+2][2], color )
            #draw_line( screen, points[p+2][0], points[p+2][1], points[p+2][2],
            #           points[p][0], points[p][1], points[p][2], color )

            V = [0, 0, -1]
            L = [1, 1, 1]
            Ia = 250
            Ip = 250

            #color = flat_shading(points[p], points[p+1], points[p+2], L, Ia, Ip, V)

            #for i in color:
            #    i += lighting

            color = [int(256*random.random()),int(256*random.random()),int(256*random.random())]
            scanline_convert(points[p], points[p+1], points[p+2], screen, color,zbuff)
        p+= 3


def flat_shading(p1, p2, p3, light_vector, Ia, Ip , view_vector):
    Ka = .4
    Kp = .4
    Kd = .4


    norm = calculate_normal( p1,p2,p3 )

    I_diffuse = Ka * Ia

    I_point = Kp*Ip*calculate_dot(norm,light_vector)

    I_specular = Ks*Ip*calculate_dot( x, view_vector)

    pass


def scanline_convert(p1, p2, p3, screen, color, zbuff):
   
    points = sorted( [(p1[1],p1[0],p1[2]), ( p2[1],p2[0],p2[2]), (p3[1],p3[0],p3[2])] )  
    
    tx=round(points[2][1])
    ty=round(points[2][0])
    tz=round(points[2][2])

    mx=round(points[1][1])
    my=round(points[1][0])
    mz=round(points[1][2])

    bx=round(points[0][1])
    by=round(points[0][0])
    bz=round(points[0][2])
    
    #start vals
    y_val = by
    x_start = bx
    x_fin = bx
    z_start = bz
    z_fin = bz

    #setting amount to add by
    if (ty == by):
        X_t_b = 0
        Z_t_b = 0
    else:
        X_t_b = ((tx - bx))/(ty-by)
        Z_t_b = ((tz - bz)/(ty-by))
    
    if (ty == my):
        X_t_m = 0
        Z_t_m = 0
    else:
        X_t_m = float(tx - mx)/(ty-my)
        Z_t_m = float(mz - bz)/(ty-my)
    if (my == by):
        X_m_b = 0
        Z_m_b = 0
    else:
        X_m_b = float(mx - bx)/(my-by)
        Z_m_b = float(mz - bz)/(my-by)
        
    #looping through vals
    while (y_val < ty):        
        
        if y_val == my:
            x_fin = mx
            z_fin = mz

        if y_val >= my:
            delta_x = X_t_m 
            delta_z = Z_t_m
        else:
            delta_x = X_m_b
            delta_z = Z_m_b
        
        x_start += X_t_b
        x_fin += delta_x
        z_start += Z_t_b
        z_fin += delta_z
        y_val += 1
        draw_line(screen,int(x_start),int(y_val),int(z_start),
                  int(x_fin),int(y_val),int(z_fin), color, zbuff)
        

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


def draw_line( screen, x0, y0, z0, x1, y1, z1, color ,zbuff):
    dx = x1 - x0
    dy = y1 - y0
    dz = z1 - z0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        dz = 0 - dz
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
        
    delta_z_x = 0
    delta_z_y = 0
    if dx != 0:
        delta_z_x = dz/dx
    if dy != 0:
        delta_z_y = dz/dy

    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y , z0, zbuff)
            y = y + 1
            z0 += delta_z_y
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0, z0, zbuff)
            x = x + 1
            z0 += delta_z_x
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y,z0)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            z0 += delta_z_x
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y,z0, zbuff)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            z0 += delta_z_y
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y,z0, zbuff)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            z0 += delta_z_x
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y, z0, zbuff)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            z0 += delta_z_y
            d = d + dx

