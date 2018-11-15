from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
    for x in range(len(matrix) - 1):
        if matrix[x][0] != None:
            draw_line(screen,matrix[x][0],matrix[x][1] ,matrix[x+1][0], matrix[x+1][1], color)

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])
'''
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    if len(matrix) == 0:
        matrick = new_matrix()

    for x in range(len(matrix)):
        if matrix.get(x).get(0) == None:
            matrix.get(x).append(x0)
            matrix.get(x).append(y0)
            matrix.get(x).append(z0)
            matrix.get(x).append(1)
            matrix.get(x+1).append(x1)
            matrix.get(x+1).append(y1)
            matrix.get(x+1).append(z1)
            matrix.get(x+1).append(1)
    for row in matrix:
        if row.get(0) == None:
            row.append(x0)
            row.append(y0)
            row.append(z0)
            row.append(1)
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
     for row in matrix:
        if row.get(0) == None:
            row.append(x)
            row.append(y)
            row.append(z)
            row.append(1)  '''
#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):

    #Swapping
    if (x0 > x1):
        tempx =x1
        x1=x0
        x0 =tempx
        tempy=y1
        y1=y0
        y0=tempy
        
    x = x0
    y = y0
    a = 2*(y1-y0)
    b = -2*(x1-x0)

    #Slope handling
    if b!=0:
        m = - a/b
    else:
        m= 1000000000

    if 0<=m<1:
        d = a + b/2 
        while x<=x1:
            #print ("X: " + str(x) + " Y: " + str(y))
            plot(screen, color, x,y)
            if d > 0: 
                y+=1 
                d+=b
            x+=1
            d+=a
        
    elif m >=1:
        d = a/2 + b
        while y <= y1:
            #print ("X: " + str(x) + " Y: " + str(y))"
            plot(screen,color,x,y)
            if d < 0:
                x+=1
                d+=a
            y+=1
            d+=b
        
    elif -1<= m:
        d = a - (b/2)
        while x <= x1:
            #print ("X: " + str(x) + " Y: " + str(y))
            plot(screen,color,x,y)
            if d < 0:
                y-=1
                d-=b
            x+=1
            d += a
    else:
        d = a/2 + b
        while y >= y1:
            #print ("X: " + str(x) + " Y: " + str(y))
            plot(screen,color,x,y)
            if d > 0:
                x+=1
                d+=a
            y-=1
            d-=b
    
