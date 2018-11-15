from display import *
from draw import *
import random

screen = new_screen()

color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255),]
for a in range(10):
    matrix = []
    for x in range(50):
        add_edge(matrix, x*a*10, 0, 0, XRES, x*a*10, 0)
        draw_lines( matrix, screen, color )

color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255),]
for a in range(10):
    matrix = []
    for x in range(50):
        add_edge(matrix, 0, x*a*10, 0, x*a*10, YRES, 0)
        draw_lines( matrix, screen, color )

color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255),]
for a in range(10):
    matrix = []
    for x in range(50):
        add_edge(matrix, XRES, 0, 0, XRES-x*a*10, x*a*10, 0)
        draw_lines( matrix, screen, color )

color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255),]
for a in range(10):
    matrix = []
    for x in range(50):
        add_edge(matrix, x*a*10, YRES, 0, XRES, YRES-x*a*10, 0)
        draw_lines( matrix, screen, color )

display(screen)


