from display import *
from matrix import *
from gmath import calculate_dot, calculate_normal, magnitude
from math import cos, sin, pi
import random

MAX_STEPS = 100

zbuffer = []

shared_vertices = {}

for y in xrange(601):
    zbuffer.append([])
    for x in xrange(601):
        zbuffer[y].append(-2147483647)
        
def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )
def bound(x):
    if x <= 255 and x >= 0:
        return x
    else:
        if x > 255:
            return 255
        else:
            return 0
def scanline_convert( v0, v1, v2, screen ):
    BMT = sorted( [ ( v0[0], v0[1], v0[2] ),
                    ( v1[0], v1[1], v1[2] ),
                    ( v2[0], v2[1], v2[2] )
                ], key = lambda x: x[1] )
    B = BMT[0][:]
    M = BMT[1][:]
    T = BMT[2][:]
    randomred = random.randint(0,255)
    randomgreen = random.randint(0,255)
    randomblue = random.randint(0,255)


    d_zero = ((T[0] - B[0])/(T[1] - B[1]))
    d_oneb = ((M[0] - B[0])/(M[1] - B[1]))
    d_onet = ((T[0] - M[0])/(T[1] - M[1]))

    d_zero_z = ((T[2] - B[2])/(T[1] - B[1]))
    d_oneb_z = ((M[2] - B[2])/(M[1] - B[1]))
    d_onet_z = ((T[2] - M[2])/(T[1] - M[1]))
    
    
    for dy in xrange(int(round(M[1] - B[1] + 1))):
        draw_line( screen, B[0] + d_zero * dy, B[1] + dy, B[0] + d_oneb * dy, B[1] + dy, [randomred, randomgreen, randomblue], B[2] + d_zero_z * dy, B[2] + d_oneb_z * dy )
    for dy in xrange(int(round(T[1] - M[1] + 1))):
        draw_line( screen, T[0] - d_zero * dy, T[1] - dy, T[0] - d_onet * dy, T[1] - dy, [randomred, randomgreen, randomblue], T[2] - d_zero_z * dy, T[2] - d_onet_z * dy )



def light(N, Ia, Ka, Ip, Kd, Ks, L, V):
    ambient = [Ia[0] * Ka[0], Ia[1] * Ka[1], Ia[2] * Ka[2]]


    #surface_point = [ sum(x)/3.0 for x in zip(B,M,T) ]
    if len(N) == 1:
        N = [N[0],N[0],N[0]]

    mag_light = magnitude(L)
    mag_normal = magnitude(N)
    normal_vector = [ x/(mag_normal * mag_light) for x in N ]
    diffuse_vectors = (L[0]*normal_vector[0] + L[1]*normal_vector[1] + L[2]*normal_vector[2])
    diffuse_constants = [Ip[0] * Kd[0], Ip[1] * Kd[1], Ip[2] * Kd[2]]
    diffuse = [ bound(diffuse_vectors * x) for x in diffuse_constants]


    # specular_vectors = [ 2 * diffuse_vectors * x for x in N ]
    # specular_vectors = [ specular_vectors[0] - L[0], specular_vectors[1] - L[1], specular_vectors[2] - L[2] ]
    # mag_specular = magnitude(specular_vectors)
    # mag_view = magnitude(V)
    # specular_vectors = [ x/(mag_specular * mag_view) for x in specular_vectors ]
    # specular_vectors = specular_vectors[0]*V[0] + specular_vectors[1]*V[1] + specular_vectors[2]*V[2]
    # specular_vectors = specular_vectors * specular_vectors * specular_vectors * specular_vectors
    # specular_constants = [Ip[0] * Ks[0], Ip[1] * Ks[1], Ip[2] * Ks[2]]
    # specular = [ specular_vectors * x for x in specular_constants ]
    
    return [ bound(int(sum(x))) for x in zip(ambient, diffuse) ]

    #return [ bound(int(sum(x))) for x in zip(ambient, diffuse, specular) ]

def normalize_vertex( v ):
    n = [ calculate_normal(
        x[1][0] - x[0][0],
        x[1][1] - x[0][1],
        x[1][2] - x[0][2],
        x[0][0] - x[2][0],
        x[0][1] - x[2][1],
        x[0][2] - x[2][2]
    ) for x in shared_vertices[tuple(v)]]
    #N = []
    #for n_vector in n:
    #    N.append(map( lambda x: x/magnitude(n_vector), n_vector))

    N = [0,0,0]
    for x in n:
        N[0] += x[0]
        N[1] += x[1]
        N[2] += x[2]
    return [ x/len(n) for x in N ]

#    return map(lambda x : sum(x[0])/len(shared_vertices[tuple(v)]), zip(n))

        

def flat_shading ( v0, v1, v2, screen, Ia, Ka, Ip, Kd, Ks, L, V ):
    BMT = sorted( [ ( v0[0], v0[1], v0[2] ),
                    ( v1[0], v1[1], v1[2] ),
                    ( v2[0], v2[1], v2[2] )
                ], key = lambda x: x[1] )
    B = BMT[0][:]
    M = BMT[1][:]
    T = BMT[2][:]
    
    normal_vector = calculate_normal(
        v1[0] - v0[0],
        v1[1] - v0[1],
        v1[2] - v0[2],
        v0[0] - v2[0],
        v0[1] - v2[1],
        v0[2] - v2[2]
    )
    lighting = light(normal_vector, Ia, Ka, Ip, Kd, Ks, L, V )

    d_zero = ((T[0] - B[0])/(T[1] - B[1]))
    d_oneb = ((M[0] - B[0])/(M[1] - B[1]))
    d_onet = ((T[0] - M[0])/(T[1] - M[1]))

    d_zero_z = ((T[2] - B[2])/(T[1] - B[1]))
    d_oneb_z = ((M[2] - B[2])/(M[1] - B[1]))
    d_onet_z = ((T[2] - M[2])/(T[1] - M[1]))
    
    
    for dy in xrange(int(round(M[1] - B[1] + 1))):
        draw_line( screen, B[0] + d_zero * dy, B[1] + dy, B[0] + d_oneb * dy, B[1] + dy, lighting, B[2] + d_zero_z * dy, B[2] + d_oneb_z * dy )
    for dy in xrange(int(round(T[1] - M[1] + 1))):
        draw_line( screen, T[0] - d_zero * dy, T[1] - dy, T[0] - d_onet * dy, T[1] - dy, lighting, T[2] - d_zero_z * dy, T[2] - d_onet_z * dy )
    
def goroud_shading( points, v0, v1, v2, screen, Ia, Ka, Ip, Kd, Ks, L, V ):
    global shared_vertices

    if shared_vertices == {}:
        for x in xrange( 0, len( points ) - 2, 3 ):
            if tuple(points[x]) not in shared_vertices.keys():
                shared_vertices[tuple(points[x])] = [[points[x],points[x+1],points[x+2]]]
            else:
                shared_vertices[tuple(points[x])].append([points[x],points[x+1],points[x+2]])
            if tuple(points[x+1]) not in shared_vertices.keys():
                shared_vertices[tuple(points[x+1])] = [[points[x],points[x+1],points[x+2]]]
            else:
                shared_vertices[tuple(points[x+1])].append([points[x],points[x+1],points[x+2]])
            if tuple(points[x+2]) not in shared_vertices.keys():
                shared_vertices[tuple(points[x+2])] = [[points[x],points[x+1],points[x+2]]]
            else:
                shared_vertices[tuple(points[x+2])].append([points[x],points[x+1],points[x+2]])
            
    
    
    BMT = sorted( [ ( v0[0], v0[1], v0[2], v0[3] ),
                    ( v1[0], v1[1], v1[2], v1[3] ),
                    ( v2[0], v2[1], v2[2], v2[3] )
                ], key = lambda x: x[1] )
    B = BMT[0][:]
    M = BMT[1][:]
    T = BMT[2][:]
   
    normal_B = normalize_vertex(B)
    normal_M = normalize_vertex(M)
    normal_T = normalize_vertex(T)
    
    light_B = light(normal_B ,Ia, Ka, Ip, Kd, Ks, L, V)
    light_M = light(normal_M ,Ia, Ka, Ip, Kd, Ks, L, V)
    light_T = light(normal_T, Ia, Ka, Ip, Kd, Ks, L, V)
    
    d_light_BT = [ (light_T[0] - light_B[0]) / (T[1] - B[1]),
                   (light_T[1] - light_B[1]) / (T[1] - B[1]),
                   (light_T[2] - light_B[2]) / (T[1] - B[1]) ]
    d_light_BM = [ (light_M[0] - light_B[0]) / (M[1] - B[1]),
                   (light_M[1] - light_B[1]) / (M[1] - B[1]),
                   (light_M[2] - light_B[2]) / (M[1] - B[1]) ]
    d_light_MT = [ (light_T[0] - light_M[0]) / (T[1] - M[1]),
                   (light_T[1] - light_M[1]) / (T[1] - M[1]),
                   (light_T[2] - light_M[2]) / (T[1] - M[1]) ]
    
    

    d_zero = ((T[0] - B[0])/(T[1] - B[1]))
    d_oneb = ((M[0] - B[0])/(M[1] - B[1]))
    d_onet = ((T[0] - M[0])/(T[1] - M[1]))

    d_zero_z = ((T[2] - B[2])/(T[1] - B[1]))
    d_oneb_z = ((M[2] - B[2])/(M[1] - B[1]))
    d_onet_z = ((T[2] - M[2])/(T[1] - M[1]))
    
    lighting = light_B[:]
    for dy in xrange(int(round(M[1] - B[1] + 1))):
        draw_line( screen, B[0] + d_zero * dy, B[1] + dy, B[0] + d_oneb * dy, B[1] + dy, [bound(int(x)) for x in lighting], B[2] + d_zero_z * dy, B[2] + d_oneb_z * dy )
        #lighting = [ lighting[0] + d_light_BT[0],
        #             lighting[1] + d_light_BT[1],
        #             lighting[2] + d_light_BT[2] ]
        lighting = [ lighting[0] + d_light_BM[0],
                     lighting[1] + d_light_BM[1],
                     lighting[2] + d_light_BM[2] ]
                     
    lighting = light_T[:]       
    for dy in xrange(int(round(T[1] - M[1] + 1))):
        draw_line( screen, T[0] - d_zero * dy, T[1] - dy, T[0] - d_onet * dy, T[1] - dy, [bound(int(x)) for x in lighting], T[2] - d_zero_z * dy, T[2] - d_onet_z * dy )
        #lighting = [ lighting[0] + d_light_BT[0],
        #             lighting[1] + d_light_BT[1],
        #             lighting[2] + d_light_BT[2] ]
        lighting = [ lighting[0] - d_light_MT[0],
                     lighting[1] - d_light_MT[1],
                     lighting[2] - d_light_MT[2] ]

def draw_polygons( points, screen, color ):
    global shared_vertices
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len( points ) - 2:

        if calculate_dot( points, p ) >= 0:
            #flat_shading(points[p], points[p+1], points[p+2], screen, [90,90,90], [.64, .16, .16], [200,200,200], [.85,.21,.21], [.9,.9,.9], [400,100,-200], [0,0,-1])
        
            goroud_shading(points, points[p], points[p+1], points[p+2], screen, [90,90,90], [.64, .16, .16], [200,200,200], [.85,.21,.21], [.9,.9,.9], [400,100,-200], [0,0,-1])
        
            #scanline_convert( points[p], points[p+1], points[p+2], screen )
            # draw_line( screen, points[p][0], points[p][1],
            #          points[p+1][0], points[p+1][1], color, points[p][2] - 1, points[p+1][2] - 1 )
            # draw_line( screen, points[p+1][0], points[p+1][1],
            #          points[p+2][0], points[p+2][1], color, points[p+1][2] - 1, points[p+2][2] - 1 )
            # draw_line( screen, points[p+2][0], points[p+2][1],
            #          points[p][0], points[p][1], color, points[p+2][2] - 1, points[p][2] - 1 )
        p+= 3
    shared_vertices = {}
    


    
    



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


def draw_line( screen, x0, y0, x1, y1, color, z0 = 0, z1 = 0 ):
    global zbuffer
    dx = x1 - x0
    dy = y1 - y0

    z = z0
    dz_dy = 0
    dz_dx = 0
    if dy != 0:
        dz_dy = (z1 - z0) / dy
    if dx != 0:
        dz_dx = (z1 - z0) / dx

    
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
            if int(y) < 600 and int(x0) < 600 and zbuffer[int(y)][int(x0)] <= -z:
                plot(screen, color,  x0, y)
                # zbuffer[int(y)][int(x0)], -z
                zbuffer[int(y)][int(x0)] = -z
            y = y + 1
            z = z + dz_dy
    elif dy == 0:
        x = x0
        while x <= x1:
            if int(y0) < 600 and int(x) < 600 and zbuffer[int(y0)][int(x)] <= -z:
                plot(screen, color, x, y0)
                # zbuffer[int(y0)][int(x)], -z
                zbuffer[int(y0)][int(x)] = -z
            x = x + 1
            z = z + dz_dx
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            if int(y) < 600 and int(x) < 600 and zbuffer[int(y)][int(x)] <= -z:
                plot(screen, color, x, y)
                # zbuffer[int(y)][int(x)], -z
                zbuffer[int(y)][int(x)] = -z
            if d > 0:
                y = y - 1
                d = d - dx
                z = z - dz_dy
            x = x + 1
            d = d - dy
            z = z + dz_dx
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            if int(y) < 600 and int(x) < 600 and zbuffer[int(y)][int(x)] <= -z:
                plot(screen, color, x, y)
                # zbuffer[int(y)][int(x)], -z
                zbuffer[int(y)][int(x)] = -z
            if d > 0:
                x = x - 1
                d = d - dy
                z = z - dz_dx
            y = y + 1
            d = d - dx
            z = z + dz_dy
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            if int(y) < 600 and int(x) < 600 and zbuffer[int(y)][int(x)] <= -z:
                plot(screen, color, x, y)
                # zbuffer[int(y)][int(x)], -z
                zbuffer[int(y)][int(x)] = -z
            if d > 0:
                y = y + 1
                d = d - dx
                z = z + dz_dy
            x = x + 1
            d = d + dy
            z = z + dz_dx
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            if int(y) < 600 and int(x) < 600 and zbuffer[int(y)][int(x)] <= -z:
                plot(screen, color, x, y)
                # zbuffer[int(y)][int(x)], -z
                zbuffer[int(y)][int(x)] = -z
            if d > 0:
                x = x + 1
                d = d - dy
                z = z + dz_dx
            y = y + 1
            d = d + dx
            z = z + dz_dy
