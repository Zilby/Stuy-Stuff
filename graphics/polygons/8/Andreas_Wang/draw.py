from display import *
from matrix import *
from math import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for x in range(len(matrix))[::2]:
        draw_line(screen, matrix[x][0], matrix[x][1], matrix[x + 1][0], matrix[x + 1][1], color)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])


def mult(m1, m2, final):
    ret = new_matrix(len(m1), len(m2[0]))
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            for h in range(len(m2)):
                ret[x][y] = ret[x][y] * 1.0
                ret[x][y] = float(ret[x][y]) +  float(m1[x][h] * m2[h][y])
                #print ret[x][y] 
            if final:
                ret[x][y] = int(ret[x][y])
    #print ret
    return ret

def make_circle(matrix, cx, cy, r):
    x0 = cx + r
    y0 = cy
    z = 0
    for i in range(100):
        t = (i +1) / 100.0
        x = r * cos(2*pi*t) + cx
        y = r * sin(2*pi*t) + cy
        add_edge(matrix, x0, y0, z, x, y, z)
        x0 = x
        y0 = y

def make_spline(edge_matrix, splinetype, points):
    t = new_matrix(4,4)
    if splinetype == "hermite":
        t[0][0] = 2
        t[1][0] = -3
        t[2][0] = 0
        t[3][0] = 1
        t[0][1] = -2
        t[1][1] = 3
        t[2][1] = 0
        t[3][1] = 0        
        t[0][2] = 1
        t[1][2] = -2
        t[2][2] = 1
        t[3][2] = 0
        t[0][3] = 1
        t[1][3] = -1
        t[2][3] = 0
        t[3][3] = 0
    elif splinetype == "bezier":
        t[0][0] = -1
        t[1][0] = 3
        t[2][0] = -3
        t[3][0] = 1
        t[0][1] = 3
        t[1][1] = -6
        t[2][1] = 3
        t[3][1] = 0        
        t[0][2] = -3
        t[1][2] = 3
        t[2][2] = 0
        t[3][2] = 0
        t[0][3] = 1
        t[1][3] = 0
        t[2][3] = 0
        t[3][3] = 0
    px = new_matrix(4,1)
    py = new_matrix(4,1)
    for i in range(4):
        px[i][0] = points[i * 2]
        py[i][0] = points[i * 2 + 1]
    if splinetype == "hermite":
        px[1][0], px[2][0] = px[2][0], px[1][0]
        py[1][0], py[2][0] = py[2][0], py[1][0]
    paramx = mult(t, px, False)
    paramy = mult(t, py, False)
    x0 = px[0][0]
    y0=  py[0][0]
    z = 0
    for i in range(100):
        t = (i +1) / 100.0
        x = paramx[0][0] * pow(t,3) + paramx[1][0] * pow(t,2) + paramx[2][0] * t + paramx[3][0]
        y = paramy[0][0] * pow(t,3) + paramy[1][0] * pow(t,2) + paramy[2][0] * t + paramy[3][0]
        add_edge(edge_matrix, x0, y0, z, x, y, z)
        x0 = x
        y0 = y

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if (x0 > x1):
        draw_line(screen, x1, y1, x0, y0, color)
    else: 
        if (x0 == x1):
            if y0 > y1:
                y0,y1= y1,y0
            for i in range(y0, y1 + 1):
                plot(screen, color, x0, i)
        else:
            A = 2 * (y1 - y0)
            B = -2 * (x1 - x0)
            m = -1.0 * A / B
            x = x0
            y = y0
                
#Octant I

            if ( m <= 1 and m >= 0):
                #print "Octant 1"
                #print x
                #print y
                d = A +  B/2
                while(x <= x1):
                    plot(screen, color, x,y)
                    if d > 0: 
                        y = y + 1
                        d  +=  B
                    x = x + 1
                    d = d + A

#Octant II
            elif ( m >= 1 ):
                d = A/2 + B
                while (y <= y1):
                    plot(screen, color, x, y)
                    if d < 0:
                        x += 1
                        d += A
                    y += 1
                    d += B
#Octant VII
            elif ( m <= -1 ):
                d = A/2 - B
                while (y >= y1):
                    plot(screen, color, x, y)
                    if d > 0:
                        x += 1
                        d += A
                    y -= 1
                    d -= B
#Octant VIII
            elif ( m > -1 and m < 0 ):
                d = A - B/2
                while (x <= x1): 
                    plot(screen, color, x, y)
                    if d < 0:
                        y -= 1
                        d -= B
                    x += 1
                    d += A
        
    




            

