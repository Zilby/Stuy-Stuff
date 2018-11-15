from display import *
from draw import *

screen = new_screen()
bluegreen = [0, 199, 144]
crimson = [220, 20, 60]
purple = [160, 32, 240]
matrix = []
r = 7

for i in range (r) :
    add_edge(matrix, 0, 0, 0, int(XRES * i / r), YRES, 0)
    add_edge(matrix, 0, 0, 0, XRES, int(YRES * i / r), 0)
draw_lines(matrix, screen, purple)

r = 9
matrix = []
for i in range (r) :
    add_edge(matrix, 0, 0, 0, int(XRES * i / r), YRES, 0)
    add_edge(matrix, 0, 0, 0, XRES, int(YRES * i / r), 0)
draw_lines(matrix, screen, crimson)

r = 13
matrix = []
for i in range (r) :
    add_edge(matrix, 0, 0, 0, int(XRES * i/r), YRES, 0)
    add_edge(matrix, 0, 0, 0, XRES, int(YRES * i/r), 0)
draw_lines(matrix, screen, bluegreen)



display(screen)
