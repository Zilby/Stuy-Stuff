from display import *
from matrix import *
from gmath import *
from math import cos, sin, pi
import random
import numpy
MAX_STEPS = 300

colors = [ [255,0,0],[0,255,0],[0,0,255],[100,0,150],[100,100,100],[120,100,50],[200,50,50]]

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )

def get_cross_prod(a, b):
    v = []
    v.append(a[1]*b[2] - a[2]*b[1])
    v.append(a[2]*b[0] - a[0]*b[2])
    v.append(a[0]*b[1] - a[1]*b[0])
    return v

def get_cosine( p1, p2, p3 ):
    n = get_normal(p1,p2,p3)
    v = [0, 0, -1]
    return n[0]*v[0] + n[1]*v[1] + n[2]*v[2]

def get_normal(points,i):
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]
    
    bx = points[ i ][0] - points[ i + 2 ][0]
    by = points[ i ][1] - points[ i + 2 ][1]
    bz = points[ i ][2] - points[ i + 2 ][2]
    
    return calculate_normal( ax, ay, az, bx, by, bz )

def get_dot(v1,v2):
    #print v1
    dot = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
    mag = ( (v1[0] * v1[0]) +
                 (v1[1] * v1[1]) +
                 (v1[2] * v1[2]) ) ** 0.5
    mag*=( (v2[0] * v2[0]) +
                            (v2[1] * v2[1]) +
                             (v2[2] * v2[2]) ) ** 0.5
    return dot/mag



def lightDiff(Ip,Kd,points,p,light_pos):
    #dot = get_dot(get_normal(points[p][0],points[p][1],points[p][2],points[p+1][0],points[p],points[p+2]),light_pos)
    print dot
    print Ip
    print Kd
    return Ip*Kd*get_dot(get_normal(points[p],points[p+1],points[p+2]),light_pos)

def lightSpec(Ip,Kd,points,p,light_pos):
    dot = calculate_dot_light(points,p,light_pos)
    print dot
    n = get_normal(points,p)
    print n
    scalar_mult([n], 2*dot)
    y = [n[0]-light_pos[0],n[1]-light_pos[1],n[2]-light_pos[2]]
    return Ip*Kd*get_dot(y,[250,250,-10])**4

def draw_polygons( points, screen, color,zbuff, Ka, Kd, Ks, Ia, lights):

    print "DRAW POLYGONS"
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return
    
    p = 0
    while p < len( points ) - 2:
       
        if calculate_dot( points, p ) >= 0:
            IambR = Ia[0]*Ka[0]
            IambG = Ia[1]*Ka[1]
            IambB = Ia[2]*Ka[2]
            '''
            IdifR = lightDiff(Ip[0],Kd[0],points,p,light_pos)
            IdifG = lightDiff(Ip[1],Kd[1],points,p,light_pos)
            IdifB = lightDiff(Ip[2],Kd[2],points,p,light_pos)
            '''
            IspecR = 0
            IspecG = 0
            IspecB = 0
            #print light
            light_pos = lights[0][1]
            Ip = lights[0][0]
            IdifR = calculate_dot_light(points,p,light_pos)*Ip[0]*Kd[0]
            IdifG = calculate_dot_light(points,p,light_pos)*Ip[1]*Kd[1]
            IdifB = calculate_dot_light(points,p,light_pos)*Ip[2]*Kd[2]
            
            IspecR = lightSpec(Ip[0],Kd[0],points,p,light_pos)
            IspecG = lightSpec(Ip[1],Kd[1],points,p,light_pos)
            IspecB = lightSpec(Ip[2],Kd[2],points,p,light_pos)
          
            # print IspecG
            It=(int(IambR+IdifR+IspecR),int(IambG+IdifG+IspecG),int(IambB+IdifB+IspecB))
           
            print "IT:"+str(It)
            #It = (255,255,255)
            draw_line( screen, points[p][0], points[p][1],
                      points[p+1][0], points[p+1][1], It )
            draw_line( screen, points[p+1][0], points[p+1][1],
                    points[p+2][0], points[p+2][1], It )
            draw_line( screen, points[p+2][0], points[p+2][1],
                    points[p][0], points[p][1], It )
            scanline_convert(points[p][0],points[p][1],points[p+1][0],points[p+1][1],points[p+2][0],points[p+2][1],screen,It)
        p+= 3


def scanline_convert( x1,y1,x2,y2,x3,y3,screen,color):
    s= sorted([(y1,x1),(y2,x2),(y3,x3)])

    ty=round(s[2][0])
    tx=round(s[2][1])
    
    by=round(s[0][0])
    bx=round(s[0][1])
    
    my=round(s[1][0])
    mx=round(s[1][1])
    
    
    xa=bx
    y=by
    xb=bx

    passedM = False
    while y<ty:
        #print "POINTS: "+str(xa)+" "+str(y)+" "+str(xb)+" "+str(y)
        
        d0 = ((tx - bx))/(ty-by)
        if not passedM and y >= my:
            passedM = True
            xb=mx
            y=my
        #print "passed M"
        if passedM:
            if my-.5<=ty<=my+.5:
                d1=0
            else:
                d1= ((tx - mx)*1.0)/(ty-my)
            
        else:
            if by-.5<=my<=by+.5:
                d1 =0
            else:
                d1 = ((mx - bx)*1.0)/(my-by)
        
        xa+=d0
        xb+=d1
        y+=1
        draw_line(screen,int(xa),int(y),int(xb),int(y),color)




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


def draw_line( screen, x0, y0, z0,x1, y1, color ):
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
        while y < y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        #print "X "+str(x)
        #print "X1 "+str(x1)
        '''
        if x1 > XRES:
            x1 = XRES
            print "TOO BIG"
        elif x < 0:
            x = 0
            print "TOO SMALL"
    '''
        while x < x1 :
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x < x1:
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
        while y < y1:
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
        while x < x1:
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
        while y < y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

