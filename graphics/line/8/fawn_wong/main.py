from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 100, 0 ]
matrix = []
y = 10

for x in range(y):
	x = x + 1
	add_edge(matrix, 0, 0, 0, int(XRES * x / y), YRES , 0)
for x in range(y):
	x = x + 1
	add_edge(matrix, 0, 0, 0, XRES, int(YRES * x / y), 0)

draw_lines( matrix, screen, color )

color = [ 0, 100, 255 ]
matrix = []

for x in range(y):
	x = x + 1
	add_edge(matrix, XRES, YRES, 0, int(XRES * x / y), 0 , 0)
for x in range(y):
	x = x + 1
	add_edge(matrix, XRES, YRES, 0, 0, int(XRES * x / y), 0)

draw_lines( matrix, screen, color )

display(screen)
