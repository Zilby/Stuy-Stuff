from display import *
from draw import *

screen = new_screen()
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
matrix1 = []
matrix2 = []
matrix3 = []

#octant I
i = 0
while i < YRES / 2:
    s = 0.25 + 1.75 * (2. * i / YRES) ** 2
    a = int(round(i * s))
    b = int(round((YRES - i) * s))
    add_edge(matrix1, 0, 0, 0, a, b, 0)
    add_edge(matrix1, 0, 0, 0, b, a, 0)
    add_edge(matrix2, a, b, 0, b, a, 0)
    add_edge(matrix3, XRES - 1, 0, 0, b, a, 0)
    add_edge(matrix3, 0, YRES - 1, 0, a, b, 0)
    i += 20
    
draw_lines(matrix1, screen, green)
draw_lines(matrix2, screen, blue)
draw_lines(matrix3, screen, red)

display(screen)
