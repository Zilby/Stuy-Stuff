from display import *
from matrix import *


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

