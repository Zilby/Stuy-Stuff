from display import *
from matrix import *
import math
'''
box, sphere, torus with lines now end with are add_<poly name> ( ... )
box, sphere, torus with triangles  are the add_<poly name>

The Drawing:

    Create new functions to add a polygon to a matrix, and go through the matrix 3 points at a time to draw triangles.
        In c, these functions can be found in draw.c
        In python, they can be found in draw.py
        Modify add box, add sphere and add torus to add triangles instead of points.
    Make sure the parser calls the draw_polygons functions when needed instead of draw_lines

'''
#poly- poly is the point matrix for polygons-> sets of three points


def add_box(poly,x,y,z,l,h,d):
    print l, h, d, x, y, z
    #front face
    add_tri(poly, x,y,z, x,y-h,z,   x+l,y-h,z);
    add_tri(poly, x,y,z, x+l,y-h,z, x+l,y,z);
    #back face
    add_tri(poly, x,y,z-d, x,y-h,z-d,   x+l,y-h,z-d);
    add_tri(poly, x,y,z-d, x+l,y-h,z-d, x+l,y,z-d);
    #add_tri(poly, x,y,z-d, x+l,y-h,z-d, x,y-h,z-d);
    #top face
    add_tri(poly, x,y,z, x+l,y,z-d, x,y,z-d);
    add_tri(poly, x,y,z, x+l,y,z-d, x+l,y,z);
    #bottom face
    add_tri(poly, x,y-h,z, x+l,y-h,z-d, x,y-h,z-d);
    add_tri(poly, x,y-h,z, x+l,y-h,z-d, x+l,y-h,z);
    #left face
    add_tri(poly, x,y,z,   x,y,z-d, x,y-h,z);
    add_tri(poly, x,y-h,z, x,y,z-d, x,y-h,z-d);
    #right face
    add_tri(poly, x+l,y,z,   x+l,y,z-d,   x+l,y-h,z);
    add_tri(poly, x+l,y-h,z, x+l,y,z-d, x+l,y-h,z-d);
    


def add_tri(poly, x,y,z,x1,y1,z1,x2,y2,z2):
    add_point(poly, x,y,z)
    add_point(poly, x1,y1,z1)
    add_point(poly, x2,y2,z2)

def add_triPoint(poly, p1, p2, p3):
    try:
        add_tri(poly, p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], p3[0], p3[1], p3[2])
    except:
        pass

def add_sphere(poly,cx,cy,r,step):
    print "not implemented yet - add_sphere"
    c = 0
    cz = 0
    points = []
    n = int(1/step)
    while c < 1 + step: 
        t = 0
        while t < 1 + step :
            theta = t*2.0*math.pi
            p = c*1.0*math.pi
            x = r*math.cos(theta) + cx
            y = r*math.cos(p)*math.sin(theta) + cy
            z = r*math.sin(theta)*math.sin(p) + cz
            points.append([x,y,z])
            t += step
        c += step
    i = 0
    while i < len(points):
        try:
            q = points[i+n+1]
            if (i%2==0):
                add_triPoint(poly,points[i], points[i+n], points[i+n+1])
            else:
                add_triPoint(poly,points[i], points[i+n+1], points[i+1])
        except:
            pass
        i += 1

def add_torus(poly,cx,cy,r,r2,step):
    print "Taurusify"
    t = 0
    c = 0
    cz = 0
    points=[]
    n = int(1/step)
    while c < 1 + step: #circle rotation  # 0 -> a little over 1
        p = c*2.0*math.pi
        t = 0 #need to reset t
        while t < 1 + step :  # 0 -> a little over 1
            theta = t*2.0*math.pi
            x = math.cos(p)*(r*math.cos(theta) + r2) + cx
            y = r*math.sin(theta) + cy
            z = -1*math.sin(p)*(r*math.cos(theta)+r2) + cz
            points.append([x,y,z])
            t += step
        c += step
    i = 0    
    while i < len(points):
        try:
            print points[i], points[i+n], points[i+n+1]
            if (i%2==0):
                add_triPoint(poly,points[i], points[i+n], points[i+n+1])
            else:
                add_triPoint(poly,points[i], points[i+n+1], points[i+1])
        except:
            pass
        i += 1
    

def add_box0(points, x,y,z,l,h,d):
    print x,y,z,l,h,d
    add_edge(points,x,y,z,x,y,z)
    add_edge(points,x,y-h,z,x,y-h,z)
    add_edge(points,x+l,y,z,x+l,y,z)
    add_edge(points,x+l,y-h,z,x+l,y-h,z)
    add_edge(points,x,y,z-d,x,y,z-d)
    add_edge(points,x,y-h,z-d,x,y-h,z-d)
    add_edge(points,x+l,y,z-d,x+l,y,z-d)
    add_edge(points,x+l,y-h,z-d,x+l,y-h,z-d)

def add_sphere0(points,cx,cy,r,step):
    print "I want my sphere with points"
    t = 0
    c = 0
    cz = 0
    while c < 1 + step: 
        t = 0
        while t < 1 + step :
            theta = t*2.0*math.pi
            p = c*1.0*math.pi
            x = r*math.cos(theta) + cx
            y = r*math.cos(p)*math.sin(theta) + cy
            z = r*math.sin(theta)*math.sin(p) + cz
            add_edge(points,x,y,z,x,y,z);
            t += step
        c += step

def add_torus0(points,cx,cy,r,r2,step):
    t = 0
    c = 0
    cz = 0
    while c < 1 + step: #circle rotation  # 0 -> a little over 1
        p = c*2.0*math.pi
        t = 0 #need to reset t
        while t < 1 + step :  # 0 -> a little over 1
            theta = t*2.0*math.pi
           
            x = math.cos(p)*(r*math.cos(theta) + r2) + cx
            y = r*math.sin(theta) + cy
            z = -1*math.sin(p)*(r*math.cos(theta)+r2) + cz
            add_edge(points,x,y,z,x,y,z);
            t += step
        c += step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    xm = generate_curve_coefs(x0,x1,x2,x3,curve_type)
    ym = generate_curve_coefs(y0,y1,y2,y3,curve_type)
    t = 0
    while (t <= 1.0+step):
        x = xm[0][0]*(t*t*t) + xm[0][1]*(t*t) + xm[0][2]*t + xm[0][3]
        y = ym[0][0]*(t*t*t) + ym[0][1]*(t*t) + ym[0][2]*t + ym[0][3]
        add_edge(points,x0,y0,0,x,y,0)
        x0 = x
        y0 = y
        t += step
        
def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    ang = t*2.0*math.pi
    x = cx
    y = cy
    z = cz
    x0 = r*math.cos(ang) + cx;
    y0 = r*math.sin(ang) + cy;
    while t <= step+1 : #1.05 or something <-step
        ang = t*2.0*math.pi
        x = r*math.cos(ang) + cx;
        y = r*math.sin(ang) + cy;
        add_edge(points,x0,y0,cz,x,y,cz);
        x0 = x;
        y0 = y;
        t += step   
   
def draw_lines( matrix, screen, color ):
    if len( matrix ) == 0:
        print "No line-drawing here"
        return
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def vectorify (p1, p2, p3): #p1,p2,p3 arrays of point coords
    A= [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    B= [p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]]
    return [A, B]

def mult_vect(v1, v2): #v1 and v2 arrays representing vectors of 3 
    N = []
    N.append(v1[1]*v2[2]-v1[2]*v2[1])
    N.append(v1[2]*v2[0]-v1[0]*v2[2])
    N.append(v1[0]*v2[1]-v1[1]*v2[0])
    return N

def dot_product(N,V):
    dot = 0
    i = 0
    while i < 3:
        dot += N[i]*V[i]
        i+=1
    return dot

def draw_triangles(poly, screen, color):
    # go through the polygon matrix and draw lines of each fo the three points
    if len ( poly ) < 3 and len( poly ) > 0: #if poly is 0, it skip the loop...
        print "You need at least 3 points to draw a triangle"
        '''
        Calculate surface normal N.
         Find the cross product of two vertices with a common endpoint and are
        pointed in opposite directions. Keep in mind that the order of
        multiplication has to be counter-clockwise
        '''
    V= [0,0,-1] # view vector
    t = 0
    while t < len ( poly ) - 1:
        AB = vectorify(poly[t], poly[t+1], poly[t+2])
        N = mult_vect(AB[0], AB[1])
        print N
        print V
        dot = dot_product(N,V)
        print dot
        if dot >= 0:
            draw_line(screen, poly[t][0], poly[t][1], poly[t+1][0], poly[t+1][1], color)
            draw_line(screen, poly[t+1][0], poly[t+1][1], poly[t+2][0], poly[t+2][1], color)
            draw_line(screen, poly[t+2][0], poly[t+2][1], poly[t][0], poly[t][1], color)
        t+=3
    
    
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

