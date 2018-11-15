from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    i=0
    while i< len(matrix) -1:
        point1=matrix[i]
        point2=matrix[i+1]
        draw_line(screen,point1[0],point1[1],0,point2[0],point2[1],0,color)
        i+=2

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0,z0, x1, y1,z1, color ):
    if (x0 > x1):
        tmpx =x1
        x1=x0
        x0 =tmpx
        tmpy=y1
        y1=y0
        y0=tmpy
        print "swapped"
    B= -2*(x1 - x0)
    A= 2*(y1 -y0)
    x=x0
    y= y0
    if B!=0:
        m = - A/B
    else:
        m=100* A
        print " M" +str(m)
    print m
    if 0<= m <1:
        print 1
        d = A + B/2
        while x <= x1:
            #print str(x)+ "," +str(y) +"/n"
            plot(screen,color,x,y)
            if d > 0:
                y+=1
                d+=B
            x+=1
            d+=A
    elif m >=1:
        print 2
        d = A/2 + B
        while y <= y1:
            #print str(x)+ "," +str(y) +"/n"
            plot(screen,color,x,y)
            if d < 0:
                x+=1
                d+=A
            y+=1
            d+=B
        
    elif -1<= m:
        print 3
        d = A - (B/2)
        #print x
        #print x1
        while x <= x1:
            #print str(x)+ "," +str(y)
            plot(screen,color,x,y)
            if d < 0:
                y-=1
                d-=B
            x+=1
            d += A
    else:
        print 4
        d = A/2 + B
        while y >= y1:
            #print str(x)+ "," +str(y)
            plot(screen,color,x,y)
            if d > 0:
                x+=1
                d+=A
            y-=1
            d-=B