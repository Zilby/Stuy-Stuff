from display import *
from matrix import *

#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines(matrix, screen, color):
    x = 0
    for i in range(len(matrix)/2):
        p = matrix[x]
        p2 = matrix[x+1]
        x += 2
        draw_line(screen, p[0], p[1], p2[0], p2[1], color) 
    
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])
    
#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line(screen, x0, y0, x1, y1, color):
    if(x0>x1):
        draw_line(screen, x1, y1, x0, y0, color)
    else:
        x = x0
        y = y0
        a = 2*(y1-y0)
        b = (-2)*(x1-x0)
        if(float(x1-x0)==0):
            if(y0>y1):
                y0, y1 = y1, y0
            while(y0<=y1):
                plot(screen,color,x,y0)
                y0+=1
        else:
            m=float(y1-y0)/float(x1-x0)
            #1,5
            if(m>=0 and m<1):
                d = a+b/2
                while(x<=x1):
                    plot(screen,color,x,y)
                    if(d>0):
                        y+=1
                        d+=b
                    x+=1
                    d+=a
            #2,6
            elif(m>=1):
                d = a/2+b
                while(y<=y1):
                    plot(screen,color,x,y)
                    if(d<0):
                        x+=1
                        d+=a
                    y+=1
                    d+=b
            #3,7
            elif(m<=-1):
                d = a/2-b
                while(y>=y1):
                    plot(screen,color,x,y)
                    if(d>0):
                        x+=1
                        d+=a
                    y-=1
                    d-=b
            #4,8
            elif (0>m and m>=-1):
                d = a-b/2
                while(x<=x1):
                    plot(screen,color,x,y)
                    if (d<0):
                        y-=1
                        d-=b
                    x+=1
                    d+=a
