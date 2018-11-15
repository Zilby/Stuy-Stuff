from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_points( matrix, screen, color ):
    for x in matrix:
        screen[x[0]][x[1]] = color

def draw_lines( matrix, screen, color ):
    i = 0
    while i < len(matrix):
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i+1][0],matrix[i+1][1],color);
        i += 2

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    matrix.append([x0,y0,z0,1])
    matrix.append([x1,y1,z1,1])
    return matrix
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([x,y,z,1])
    return matrix

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color
def draw_line( screen, x0, y0, x1, y1, color ):
    if x1 - x0 < 0:
        placeholder = x1
        x1 = x0
        x0 = placeholder
        placeholder = y1
        y1 = y0
        y0 = placeholder

    A = -2*(y1 - y0)
    B = -2*(x1-x0)
    d = .5 * A + B
    if x0 != x1 and (1.0*((YRES-y1)-(YRES-y0)))/(1.0*x1-x0) <= 1 and (1.0*((YRES-y1)-(YRES-y0)))/(1.0*x1-x0) >= 0:
        while (x0 <= x1):
            screen[x0][y0] = color
            if (d > 0):
                y0 -= 1
                d += B
            x0 += 1
            d += A
    elif  (x1 == x0 and y1 < y0) or (x1 != x0 and (1.0*((YRES-y1)-(YRES-y0)))/(1.0*x1-x0) > 1):
        while (y0 >= y1):
            screen[x0][y0] = color
            if (d < 0):
                x0 += 1
                d += A
            y0 -= 1
            d += B
    elif x1 != x0 and (1.0*((YRES-y1)-(YRES-y0)))/(1.0*x1-x0) <= 0 and (1.0*((YRES-y1)-(YRES-y0)))/(1.0*x1-x0) >= -1:
        d = A - .5 * B;
        while (x0 <= x1):
            screen[x0][y0] = color
            if (d < 0):
                y0 += 1
                d -= B
            x0 += 1
            d += A
    else:
        d = A - .5 * B;
        while (y0 <= y1):
            screen[x0][y0] = color
            if (d > 0):
                x0 += 1
                d += A
            y0 += 1
            d -= B
    return screen

if __name__ == "__main__":
    m = []
    screen = new_screen();
    #add_point(m,12,11)
    #add_point(m,0,90)
    #add_edge(m,100,200,0,300,450,0)
    
    draw_line(screen,0,400,250,300,[255,0,0])
    draw_line(screen,250,200,0,300,[255,0,0])
    draw_line(screen,0,150,450,325,[255,0,0])
    draw_line(screen,0,0,100,400,[255,0,0])
    add_edge(m,0,400,0,250,300,0)
    add_edge(m,0,300,0,250,200,0)
    add_edge(m,0,150,0,450,325,0)
    draw_line(screen,100,400,200,100,[255,0,0])
    draw_points(m,screen,[0,255,0])
    display(screen)
