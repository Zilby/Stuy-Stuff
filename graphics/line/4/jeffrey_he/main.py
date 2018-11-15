from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
'''add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
'''
'''add_edge(matrix, 100,100,0,200,80,0)
add_edge(matrix, 200, 200, 0, 100, 300, 0)
add_edge(matrix, 150,150, 0, 200, 50, 0)
add_edge(matrix, 300,300,0, 400, 250,0)'''
'''
add_edge(matrix, 0 , YRES/2, 0 , XRES-1, YRES/2,0)
add_edge(matrix, XRES/2 , 0 ,0 , XRES/2, YRES-1,0) '''

dy = 15
dx = 16
xold = 250
yold = 250

xx = xold + dx
yy = yold + dy


while(xx>0 and xx < XRES and yy > 0 and yy < YRES):
    add_edge(matrix, xold, yold, 0, xx, yy, 0)
    xold = xx
    yold = yy
    xx += dx
    yy += dy
    dy -= 1
    dx -= 3
draw_lines( matrix, screen, color )


save_ppm(screen, "pic.ppm")
