from display import *
from draw import *
import random

screen = new_screen()
color = [0,255,0]

matrix = []
for i in range(1, 40):
    add_edge(matrix, 0, YRES / 2, 0, XRES / 2, (YRES / 40) * i, 0)
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
draw_lines( matrix, screen, color)

matrix = []
for i in range(1, 40):
    add_edge(matrix, XRES, YRES / 2, 0, XRES / 2, (YRES / 40) * i, 0)
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
draw_lines( matrix, screen, color)

matrix = []
for i in range(1, 40):
    add_edge(matrix, XRES / 2, 0, 0, (XRES / 40) * i, YRES / 2, 0)
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
draw_lines( matrix, screen, color)

matrix = []
for i in range(1, 40):
    add_edge(matrix, XRES / 2, YRES, 0, (XRES / 40) * i, YRES / 2, 0)
color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
draw_lines( matrix, screen, color)



print_matrix(matrix)
display(screen)
