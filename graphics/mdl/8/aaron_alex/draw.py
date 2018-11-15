from display import *
from matrix import *
import math      

def add_box(points, x, y, z, w, h, d):
    add_polygon(points, x, y, z, x+w, y, z, x+w, y+h, z)
    add_polygon(points, x, y, z, x+w, y+h, z, x, y+h, z)
    add_polygon(points, x+w, y+h, z+d, x+w, y, z+d, x, y, z+d)
    add_polygon(points, x, y+h, z+d, x+w, y+h, z+d, x, y, z+d)
    add_polygon(points, x, y, z, x+w, y, z+d, x+w, y, z)
    add_polygon(points, x, y, z, x, y, z+d, x+w, y, z+d)
    add_polygon(points, x+w, y+h, z, x+w, y+h, z+d, x, y+h, z)
    add_polygon(points, x+w, y+h, z+d, x, y+h, z+d, x, y+h, z)
    add_polygon(points, x, y, z, x, y+h, z+d, x, y, z+d)
    add_polygon(points, x, y, z, x, y+h, z, x, y+h, z+d)
    add_polygon(points, x+w, y, z+d, x+w, y+h, z+d, x+w, y, z)
    add_polygon(points, x+w, y+h, z+d, x+w, y+h, z, x+w, y, z)
    
def add_sphere(points, x, y, z, r, steps=15):
    spts = []
    theta = 0
    while theta <= 2*math.pi:
        phi = 0
        spts.append([])
        while phi <= math.pi:
            xcor = r*math.sin(phi)*math.cos(theta) + x
            ycor = r*math.cos(phi) + y
            zcor = r*math.sin(phi)*math.sin(theta) + z
            add_polygon(points,xcor,ycor,zcor,xcor,ycor,zcor,xcor,ycor,zcor)
            spts[len(spts)-1].append([xcor,ycor,zcor])
            phi += math.pi / steps
        theta += math.pi / steps
    fill_faces(points,spts,False,True)


def add_torus(points, x, y, z, r1, r2, steps=15):
    spts = []
    theta = 0
    while theta < 2*math.pi: 
        spts.append([])
        phi = 0
        while phi < 2*math.pi:
            xcor = math.cos(theta)*(r2*math.cos(phi) + r1) + x
            ycor = r2*math.sin(phi) + y
            zcor = -1*math.sin(theta)*(r2*math.cos(phi) + r1) + z 
            spts[len(spts)-1].append([xcor,ycor,zcor])
            phi += math.pi / steps
        theta += math.pi / steps
    fill_faces(points,spts,True,True)
    

def fill_faces(points, spts, wrapX, wrapY):
    xRange = len(spts) - 1
    yRange = len(spts[0]) - 1
    for x in range(xRange):
        for y in range(yRange):
            add_polygon(points, spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[x][y+1][0], spts[x][y+1][1], spts[x][y+1][2], 
                        spts[x+1][y+1][0], spts[x+1][y+1][1], spts[x+1][y+1][2])
            add_polygon(points, spts[x+1][y][0], spts[x+1][y][1], spts[x+1][y][2], 
                        spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[x+1][y+1][0], spts[x+1][y+1][1], spts[x+1][y+1][2])
    if wrapX:
        y = len(spts[0]) - 1
        for x in range(xRange):
            add_polygon(points, spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[x][0][0], spts[x][0][1], spts[x][0][2], 
                        spts[x+1][0][0], spts[x+1][0][1], spts[x+1][0][2])
            add_polygon(points, spts[x+1][y][0], spts[x+1][y][1], spts[x+1][y][2], 
                        spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[x+1][0][0], spts[x+1][0][1], spts[x+1][0][2])
    if wrapY:
        x = len(spts) - 1
        for y in range(yRange):
            add_polygon(points, spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[x][y+1][0], spts[x][y+1][1], spts[x][y+1][2], 
                        spts[0][y+1][0], spts[0][y+1][1], spts[0][y+1][2])
            add_polygon(points, spts[0][y][0], spts[0][y][1], spts[0][y][2], 
                        spts[x][y][0], spts[x][y][1], spts[x][y][2], 
                        spts[0][y+1][0], spts[0][y+1][1], spts[0][y+1][2])

def add_circle( points, cx, cy, cz, r, step ):
    t = 0
    theta = 0
    while t < 1.0000001:
        add_point(points, cx + r*math.cos(theta), cy + r*math.sin(theta), cz)
        t += step
        theta = t*2*math.pi
        add_point(points, cx + r*math.cos(theta), cy + r*math.sin(theta), cz)   

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    if curve_type == "bezier":
        xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
        ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]
        
    elif curve_type == "hermite":
        xcoefs = generate_curve_coefs(x0, x2, x1-x0, x3-x2, curve_type)[0]
        ycoefs = generate_curve_coefs(y0, y2, y1-y0, y3-y2, curve_type)[0]
        
    else:
        print "invalid curve type"

    x, y, t = x0, y0, 0
    while t < 1.0000001:            
            t += step
            add_point(points, x, y, 0)
            x = t*t*t*xcoefs[0] + t*t*xcoefs[1] + t*xcoefs[2] + xcoefs[3]
            y = t*t*t*ycoefs[0] + t*t*ycoefs[1] + t*ycoefs[2] + ycoefs[3]
            add_point(points, x, y, 0)    
        
def draw_polygons( points, screen, color ):
    if len( points ) < 3:
        print "Need at least 3 points to draw a polygon"   
    
    else:
        p = 0
        while p < len(points) - 1:
            if facing_view(points[p:p+4]):
                draw_line( screen, points[p][0], points[p][1],
                           points[p+1][0], points[p+1][1], color )
                draw_line( screen, points[p+1][0], points[p+1][1],
                           points[p+2][0], points[p+2][1], color )
                draw_line( screen, points[p+2][0], points[p+2][1],
                           points[p][0], points[p][1], color )
            p+= 3

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(points, x0, y0, z0)
    add_point(points, x1, y1, z1)
    add_point(points, x2, y2, z2)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def draw_line( screen, x0, y0, x1, y1, color ):
    if x0 > x1 or (x0 == x1 and y0 > y1): #swap((x1,y1),(x0,y0))
        xtmp,ytmp = x0,y0
        x0,y0 = x1,y1
        x1,y1 = xtmp,ytmp

    if x0 != x1:
        m = (y0-y1)/float(x0-x1)
    else:
        m = 9999

    if m < 0:#transformation: reflect across x-axis
        y0,y1 = -y0,-y1

    if abs(m) > 1 :#transformation: reflect across y=x
        tmp0,tmp1 = x0,x1#swap((x0,x1),(y0,y1))
        x0,x1 = y0,y1
        y0,y1 = tmp0,tmp1

    A = 2 * (y1-y0)
    B = 2 * (x0-x1)
    x,y = x0,y0
    d = A + B/2

    while x <= x1: 
        if m > 1:#transformation: reflect back across y=x
            plot(screen, color, y, x)
        elif 0 <= m <= 1:#transformation: none
            plot(screen, color, x, y)
        elif -1 <= m < 0:#transformation: reflect back across x-axis
            plot(screen, color, x, -y)
        else:#transformation: reflect back across y=x, then back across x-axis
            plot(screen, color, y, -x)
        if d > 0:
            y+=1
            d+=B
        x+=1
        d+=A
