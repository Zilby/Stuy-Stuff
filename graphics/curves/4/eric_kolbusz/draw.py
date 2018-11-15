from display import *
from matrix import *

def draw_lines( matrix, screen, color ):
    i = 0
    while i<len(matrix)-1:
        draw_line(screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color)
        i += 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])

def draw_line( screen, x0, y0, x1, y1, color ):
    x0 = int(round(x0))
    x1 = int(round(x1))
    y0 = int(round(y0))
    y1 = int(round(y1))
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
            
def add_circle(points, cx, cy, cz, r, step):
    cy = YRES - cy
    t = step
    x0 = cx+r
    y0 = cy
    for i in range(int(1.0/step)):
        x = r*math.cos(2*math.pi*t) + cx
        y = r*math.sin(2*math.pi*t) + cy
        add_edge(points, x0, y0, cz, x, y, cz)
        x0 = x
        y0 = y
        t += step

def add_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    y0 = YRES - y0
    y1 = YRES - y1
    y2 = YRES - y2
    y3 = YRES - y3
    t = step
    co = generate_curve_coefs([x0,y0], [x1,y1], [x2,y2], [x3,y3], curve_type)
    for i in range(int(1.0/step)):
        x = co[0][0][0]*t*t*t + co[0][0][1]*t*t + co[0][0][2]*t + co[0][0][3]
        y = co[1][0][0]*t*t*t + co[1][0][1]*t*t + co[1][0][2]*t + co[1][0][3]
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step
        
        
        
        
        
        
    
