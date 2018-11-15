from display import *
from matrix import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for i in range(len(matrix[0])/2):
        draw_line(screen, matrix[0][2*i],matrix[1][2*i],matrix[0][(2*i) + 1],matrix[1][(2*i) + 1], color)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0)
    add_point( matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    point = [x,y,z,1]
    for i in range (4):
        matrix[i].append(point[i])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
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
            screen[y][x] = color
        elif 0 <= m <= 1:#transformation: none
            screen[x][y] = color
        elif -1 <= m < 0:#transformation: reflect back across x-axis
            screen[x][-y] = color
        else:#transformation: reflect back across y=x, then back across x-axis
            screen[y][-x] = color
        if d > 0:
            y+=1
            d+=B
        x+=1
        d+=A

    

