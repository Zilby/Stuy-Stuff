from display import *
from draw import *

screen = new_screen()

color = [ 52, 152, 219 ]
matrix = []

for x in range(14):
    add_edge(matrix, 0, 0, 0, int((XRES-1)*(14-x)/15), int((YRES-1)*(x+1)/15), 0)
for x in range(14):
    add_edge(matrix, 0, 0, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(14-x)/15), 0)
add_edge(matrix, 0, 0, 0, (XRES-1)/2, (YRES-1)/2, 0)

draw_lines( matrix, screen, color )


color = [ 241, 196, 15 ]
matrix = []

for x in range(14):
    add_edge(matrix, XRES-1, YRES-1, 0, int((XRES-1)*(14-x)/15), int((YRES-1)*(x+1)/15), 0)
for x in range(14):
    add_edge(matrix, XRES-1, YRES-1, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(14-x)/15), 0)
add_edge(matrix, XRES-1, YRES-1, 0, (XRES-1)/2, (YRES-1)/2, 0)

draw_lines( matrix, screen, color )

color = [ 46, 204, 113 ]
matrix = []

for x in range(14):
    add_edge(matrix, XRES-1, 0, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(x+1)/15), 0)
for x in range(14):
    add_edge(matrix, XRES-1, 0, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(x+1)/15), 0)
add_edge(matrix, XRES-1, 0, 0, (XRES-1)/2, (YRES-1)/2, 0)

draw_lines( matrix, screen, color )


color = [ 155, 89, 182 ]
matrix = []

for x in range(14):
    add_edge(matrix, 0, YRES-1, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(x+1)/15), 0)
for x in range(14):
    add_edge(matrix, 0, YRES-1, 0, int((XRES-1)*(x+1)/15), int((YRES-1)*(x+1)/15), 0)
add_edge(matrix, 0, YRES-1, 0, (XRES-1)/2, (YRES-1)/2, 0)

draw_lines( matrix, screen, color )


color = [ 236, 240, 241 ]
matrix = []

add_edge(matrix, 0, 0, 0, 0, YRES-1, 0)
add_edge(matrix, 0, 0, 0, XRES-1, 0, 0)
add_edge(matrix, XRES-1, YRES-1, 0, 0, YRES-1, 0)
add_edge(matrix, XRES-1, YRES-1, 0, XRES-1, 0, 0)

draw_lines( matrix, screen, color )

display(screen)
