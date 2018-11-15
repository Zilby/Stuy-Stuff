from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

def add_teststar():
    add_edge(matrix, 200, 200, 0, 200, 300, 0 )
    add_edge(matrix, 200, 200, 0, 250, 300, 0 )
    add_edge(matrix, 200, 200, 0, 300, 300, 0 )
    add_edge(matrix, 200, 200, 0, 300, 250, 0 )
    add_edge(matrix, 200, 200, 0, 300, 200, 0 )
    add_edge(matrix, 200, 200, 0, 300, 150, 0 )
    add_edge(matrix, 200, 200, 0, 300, 100, 0 )
    add_edge(matrix, 200, 200, 0, 250, 100, 0 )
    add_edge(matrix, 200, 200, 0, 200, 100, 0 )
    add_edge(matrix, 200, 200, 0, 150, 100, 0 )
    add_edge(matrix, 200, 200, 0, 100, 100, 0 )
    add_edge(matrix, 200, 200, 0, 100, 150, 0 )
    add_edge(matrix, 200, 200, 0, 100, 200, 0 )
    add_edge(matrix, 200, 200, 0, 100, 250, 0 )
    add_edge(matrix, 200, 200, 0, 100, 300, 0 )
    add_edge(matrix, 200, 200, 0, 150, 300, 0 )

def dist(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2) + ((y1-y2)**2))

def add_testellipse():
    f1x = 170
    f1y = 150
    f2x = 330
    f2y = 350

    edge = []
    d = 400
    #i_cant_do_math.jpg
    #brute_force.png
    for y in range(100):
        y = y*5
        for x in range(500):
            f1d = dist(x,y,f1x,f1y)
            f2d = dist(x,y,f2x,f2y)
            curd = f1d + f2d
            if abs(curd-d)<1:
                add_edge(matrix, f1x,f1y,0, x,y,0)
                add_edge(matrix, f2x,f2y,0, x,y,0)
                break
        for x in range(500):
            x = 500-x
            f1d = dist(x,y,f1x,f1y)
            f2d = dist(x,y,f2x,f2y)
            curd = f1d + f2d
            if abs(curd-d)<1:
                add_edge(matrix, f1x,f1y,0, x,y,0)
                add_edge(matrix, f2x,f2y,0, x,y,0)
                break
            

#add_teststar();
add_testellipse();

draw_lines( matrix, screen, color )
print_matrix(matrix)

display(screen)
