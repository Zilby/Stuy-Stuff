from display import *
from matrix import *
from gmath import calculate_dot
from math import cos, sin, pi
from random import randint
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
from lighting import *
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master

def draw_polygons( points, screen, color ):
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return

    p = 0
    while p < len(points) - 2:
        if calculate_dot(points, p) >= 0:
<<<<<<< HEAD
            draw_line(screen, points[p][0], points[p][1], points[p][2], points[p+1][0], points[p+1][1], points[p+1][2], color)
            draw_line(screen, points[p+1][0], points[p+1][1], points[p+1][2], points[p+2][0], points[p+2][1], points[p+2][2], color)
            draw_line(screen, points[p+2][0], points[p+2][1], points[p+2][2], points[p][0], points[p][1], points[p][2], color)
=======
<<<<<<< HEAD
            draw_line(screen, points[p][0], points[p][1], points[p][2], points[p+1][0], points[p+1][1], points[p+1][2], color)
            draw_line(screen, points[p+1][0], points[p+1][1], points[p+1][2], points[p+2][0], points[p+2][1], points[p+2][2], color)
            draw_line(screen, points[p+2][0], points[p+2][1], points[p+2][2], points[p][0], points[p][1], points[p][2], color)
=======
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
            fill_polygon(screen, points[p], points[p+1], points[p+2], color)
        p+= 3

def fill_polygon(screen, p0, p1, p2, color):
<<<<<<< HEAD
    fill = [randint(0,255),randint(0,255),randint(0,255)]
=======
<<<<<<< HEAD
    fill = [randint(0,255),randint(0,255),randint(0,255)]
=======
    fill = get_illumination(p0, p1, p2)
    draw_line(screen, p0[0], p0[1], p0[2], p1[0], p1[1], p1[2], fill)
    draw_line(screen, p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], fill)
    draw_line(screen, p2[0], p2[1], p2[2], p0[0], p0[1], p0[2], fill)
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    points = [p0,p1,p2]
    points.sort(key=lambda x: x[1])
    bottom = points[0]
    middle = points[1]
    top = points[2]
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/master
    d1 = middle[1] - bottom[1] + 1
    d2 = top[1] - middle[1]
    for y in range(int(d1)):
        xcor1 = (bottom[0]*(d1-y) + middle[0]*y)/d1
        xcor2 = (bottom[0]*(d1+d2-y) + top[0]*y)/(d1+d2)
        zcor1 = (bottom[2]*(d1-y) + middle[2]*y)/d1
        zcor2 = (bottom[2]*(d1+d2-y) + top[2]*y)/(d1+d2)
        ycor = y + bottom[1]
        draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)
    for y in range(int(d2)):
        xcor1 = (middle[0]*(d2-y) + top[0]*y)/d2
        xcor2 = (bottom[0]*(d2-y) + top[0]*(d1+y))/(d1+d2)
        zcor1 = (middle[2]*(d2-y) + top[2]*y)/d2
        zcor2 = (bottom[2]*(d2-y) + top[2]*(d1+y))/(d1+d2)
        ycor = y + middle[1]
        draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)    
<<<<<<< HEAD
=======
=======
    d1 = middle[1] - bottom[1]
    d2 = top[1] - middle[1]

    if d1 != 0:
        for y in range(int(d1+1)):
            xcor1 = (bottom[0]*(d1-y) + middle[0]*y)/d1
            xcor2 = (bottom[0]*(d1+d2-y) + top[0]*y)/(d1+d2)
            zcor1 = (bottom[2]*(d1-y) + middle[2]*y)/d1
            zcor2 = (bottom[2]*(d1+d2-y) + top[2]*y)/(d1+d2)
            ycor = y + bottom[1]
            draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)
            
    if d2 != 0:
        for y in range(int(d2+1)):
            xcor1 = (middle[0]*(d2-y) + top[0]*y)/d2
            xcor2 = (bottom[0]*(d2-y) + top[0]*(d1+y))/(d1+d2)
            zcor1 = (middle[2]*(d2-y) + top[2]*y)/d2
            zcor2 = (bottom[2]*(d2-y) + top[2]*(d1+y))/(d1+d2)
            ycor = y + middle[1]
            draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)    


def draw_planet_polygons( points, screen, ar1, ag1, ab1, dr1, dg1, db1, sr1, sg1, sb1, ar2, ag2, ab2, dr2, dg2, db2, sr2, sg2, sb2, steps=15):
    if len(points) < 3:
        print 'Need at least 3 points to draw a polygon!'
        return
    ar, ag, ab, dr, dg, db, sr, sg, sb = ar1, ag1, ab1, dr1, dg1, db1, sr1, sg1, sb1
    p = 0
    while p < len(points) - 2:
        xcor = 50*p/(steps*steps*3)
        ycor = 50*((p*3)%(steps*18))/(steps*9)
        def ran(x, y, r):
            return (xcor-x)**2 + (ycor-y)**2 + xcor%19 - ycor%11 + ycor%5 - xcor%7 < r**2

        if (ran(40,40,25) or ran(58,48,15) or ran(50,62,8) or ran(50,17,4) or ran(65,60,11) or ran(75,66,5) or ran(19,32,4) or ran(59,80,3) or ran(10,12,3) or ran(13,15,3) or ran(160,60,21) or ran(142,63,17) or ran(162,35,19) or ran(145,20,6) or ran(135,17,4) or ran(123,50,4) or ran(182,35,3) or ran(127,15,2) or ran(110,30,5) or ran(100,28,3) or ran(102,40,2) or ran(105,50,3) or ran(108,62,2)) and not (ran(50,49,2) or ran(51,48,2) or ran(155,55,2) or ran(156,57,2) or ran(138,58,2) or ran(139,56,1)):
            ar, ag, ab, dr, dg, db, sr, sg, sb = ar2, ag2, ab2, dr2, dg2, db2, sr2, sg2, sb2
        else: 
            ar, ag, ab, dr, dg, db, sr, sg, sb = ar1, ag1, ab1, dr1, dg1, db1, sr1, sg1, sb1
        if calculate_dot(points, p) >= 0:
            fill_planet_polygon(screen, points[p], points[p+1], points[p+2], ar, ag, ab, dr, dg, db, sr, sg, sb)
        p+= 3

def fill_planet_polygon(screen, p0, p1, p2, ar, ag, ab, dr, dg, db, sr, sg, sb):
    AMBIENT_LIGHT[0], AMBIENT_LIGHT[1], AMBIENT_LIGHT[2] = ar, ag, ab
    DIFFUSE_LIGHT[0], DIFFUSE_LIGHT[1], DIFFUSE_LIGHT[2] = dr, dg, db
    SPECULAR_LIGHT[0], SPECULAR_LIGHT[1], SPECULAR_LIGHT[2] = sr, sg, sb
    fill = get_illumination(p0, p1, p2)
    draw_line(screen, p0[0], p0[1], p0[2], p1[0], p1[1], p1[2], fill)
    draw_line(screen, p1[0], p1[1], p1[2], p2[0], p2[1], p2[2], fill)
    draw_line(screen, p2[0], p2[1], p2[2], p0[0], p0[1], p0[2], fill)
    points = [p0,p1,p2]
    points.sort(key=lambda x: x[1])
    bottom = points[0]
    middle = points[1]
    top = points[2]
    d1 = middle[1] - bottom[1]
    d2 = top[1] - middle[1]

    if d1 != 0:
        for y in range(int(d1+1)):
            xcor1 = (bottom[0]*(d1-y) + middle[0]*y)/d1
            xcor2 = (bottom[0]*(d1+d2-y) + top[0]*y)/(d1+d2)
            zcor1 = (bottom[2]*(d1-y) + middle[2]*y)/d1
            zcor2 = (bottom[2]*(d1+d2-y) + top[2]*y)/(d1+d2)
            ycor = y + bottom[1]
            draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)
            
    if d2 != 0:
        for y in range(int(d2+1)):
            xcor1 = (middle[0]*(d2-y) + top[0]*y)/d2
            xcor2 = (bottom[0]*(d2-y) + top[0]*(d1+y))/(d1+d2)
            zcor1 = (middle[2]*(d2-y) + top[2]*y)/d2
            zcor2 = (bottom[2]*(d2-y) + top[2]*(d1+y))/(d1+d2)
            ycor = y + middle[1]
            draw_line(screen, xcor1, ycor, zcor1, xcor2, ycor, zcor2, fill)    
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
       
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
<<<<<<< HEAD
            add_polygon(points,xcor,ycor,zcor,xcor,ycor,zcor,xcor,ycor,zcor)
=======
<<<<<<< HEAD
            add_polygon(points,xcor,ycor,zcor,xcor,ycor,zcor,xcor,ycor,zcor)
=======
            #add_polygon(points,xcor,ycor,zcor,xcor,ycor,zcor,xcor,ycor,zcor)
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
            spts[len(spts)-1].append([xcor,ycor,zcor])
            phi += math.pi / steps
        theta += math.pi / steps
    fill_faces(points,spts,False,True)

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
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
<<<<<<< HEAD
    
=======
<<<<<<< HEAD
    
=======
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master

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

def add_circle(points, cx, cy, cz, r, step):
    t = 0
    theta = 0
    while t < 1.0000001:
        add_point(points, cx + r*math.cos(theta), cy + r*math.sin(theta), cz)
        t += step
        theta = t*2*math.pi
        add_point(points, cx + r*math.cos(theta), cy + r*math.sin(theta), cz)

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

def add_polygon( points, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point( points, x0, y0, z0 )
    add_point( points, x1, y1, z1 )
    add_point( points, x2, y2, z2 )

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def draw_line( screen, x0, y0, z0, x1, y1, z1, color ):
    if x0 > x1 or (x0 == x1 and y0 > y1): #swap((x1,y1,z1),(x0,y0,z0))
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
        if m > 1:#transformation: reflect back across y=x
            plot(screen, color, y, x, -z)
        elif 0 <= m <= 1:#transformation: none
            plot(screen, color, x, y, z)
        elif -1 <= m < 0:#transformation: reflect back across x-axis
            plot(screen, color, x, -y, -z)
        else:#transformation: reflect back across y=x, then back across x-axis
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
