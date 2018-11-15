from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
#matrix = []


#octant I
#add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
#add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

space = 30
green = [0,255,0]
matrix1 = []
x0 = 0
y0 = 0
x1 = space
y1 = YRES
while y0 < YRES and x1 < XRES:
    add_edge(matrix1, x0, y0, 0, x1, y1, 0)
    y0 += space
    x1 += space

draw_lines( matrix1, screen, green )


matrix2 = []
x0 = XRES
y0 = YRES
x1 = XRES - space
y1 = 0
while y0 > 0 and x1 > 0:
    add_edge(matrix2, x0, y0, 0, x1, y1, 0)
    y0 -= space
    x1 -= space

draw_lines( matrix2, screen, green )

display(screen)
