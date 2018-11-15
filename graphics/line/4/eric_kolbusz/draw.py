from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of points
def draw_lines( matrix, screen, color ):
    i = 0
    while i<len(matrix)-1:
        draw_line(screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color)
        i += 2
        

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if x0 > x1: #left to right
        #x
        temp = x1
        x1 = x0
        x0 = temp
        #y
        temp = y1
        y1 = y0
        y0 = temp
    if x0 == x1: #i aint about that limit life
        if y0 > y1:
            yi = y1
            yf = y0
        else:
            yi = y0
            yf = y1
        for ycor in range(yi,yf+1):
            plot(screen, color, x0, ycor)
    else:
        dx = x1-x0
        dy = y1-y0
        a = 2*dy
        b = -2*dx
        m = float(dy)/float(dx) #this int division debug only took about 5 minutes surprisingly
        if (m>=0) and (m<=1): #I, V
            d = a + b/2
            while (x0 <= x1):
                plot(screen, color, x0, y0)
                if d > 0:
                    y0 += 1
                    d += b
                x0 += 1
                d += a
        elif m>1: #II, VI
            d = a/2 + b
            while (y0 <= y1):
                plot(screen, color, x0, y0)
                if d < 0:
                    x0 += 1
                    d += a
                y0 += 1
                d += b
        elif m<-1: #III, VII
            d = a + b/2
            while (y0 >= y1):
                plot(screen, color, x0, y0)
                if d > 0:
                    x0 += 1
                    d += a
                y0 -= 1
                d -= b
        else: #IV, VIII
            d = a + b/2
            while (x0 <= x1):
                plot(screen, color, x0, y0)
                if d < 0:
                    y0 -= 1
                    d -= b
                x0 += 1
                d += a
            
        
        
    
