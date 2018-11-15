from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    c = 0
    a = len(matrix)/2
    for i in range(a):
        p1 = matrix[c]
        p2 = matrix[c+1]
        c += 2
        draw_line(screen, p1[0], p1[1], p2[0], p2[1], color)


#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    P1 = [x0, y0, z0, 1]
    P2 = [x1, y1, z1, 1]
    matrix.append(P1)
    matrix.append(P2)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    p = [x, y, z, 1]
    matrix/append(p)

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if(x1 == x0):
        if(y0 > y1):
            y = y0
            yf = y1
        else:
            y = y1
            yf = y0
        while( y != yf ):
            plot(screen,color,x0,y)
            y-=1;
        return
    if (x1>= x0):
        Xa = x0
        Xb = x1
        Ya = y0
        Yb = y1
    else:
        Xa = x1
        Xb = x0
        Ya = y1
        Yb = y0
    a = 2*(Yb-Ya)
    b = -2*(Xb-Xa)
    if ((Xb-Xa) == 0):
        m = 1
    else:
        m = float(Yb - Ya)/float(Xb - Xa)
        if (Yb >= Ya): #increasing
            if m <=1: #1st (5th)
                d = a + b/2
                while (Xa <= Xb):
                    plot(screen,color,Xa,Ya)
                    if d > 0:
                        Ya += 1
                        d += b
                    Xa += 1
                    d += a
            else: #2nd (6th)
                d = a/2 + b
                while (Ya <= Yb):
                    plot(screen,color,Xa,Ya)
                    if d < 0:
                        Xa += 1
                        d += a
                    Ya += 1
                    d += b
        else: #decreasing
            if m >= -1: #3rd (7th)
                d = a - b/2
                while (Xa <= Xb):
                    plot(screen,color,Xa,Ya)
                    if d < 0:
                        Ya -= 1
                        d -= b
                    Xa += 1
                    d += a
            else: #4th (8th)
                d = a/2 - b
                while (Ya >= Yb):
                    plot(screen,color,Xa,Ya)
                    if d > 0:
                        Xa += 1
                        d += a
                    Ya -= 1
                    d -= b
