from display import *
from draw import *

screen = new_screen()
red = [255,0,0]
orange = [255,127,0]
yellow = [255,255,0]
green = [0,255,0]
cyan = [0,255,255]
blue = [0,0,255]
purple = [127,0,255]
magenta = [255,0,127]
color = [255,255,255]
matrix = new_matrix(0,4)


add_edge(matrix, XRES/2 + 64, YRES/2 + 224, 0, XRES/2 + 224, YRES/2 + 64, 0)
add_edge(matrix, XRES/2 + 224, YRES/2 + 64, 0, XRES/2 + 224, YRES/2 - 64, 0)
add_edge(matrix, XRES/2 + 224, YRES/2 - 64, 0, XRES/2 + 64, YRES/2 - 224, 0)
add_edge(matrix, XRES/2 + 64, YRES/2 - 224, 0, XRES/2 - 64, YRES/2 - 224, 0)
add_edge(matrix, XRES/2 - 64, YRES/2 - 224, 0, XRES/2 - 224, YRES/2 - 64, 0)
add_edge(matrix, XRES/2 - 224, YRES/2 - 64, 0, XRES/2 - 224, YRES/2 + 64, 0)
add_edge(matrix, XRES/2 - 224, YRES/2 + 64, 0, XRES/2 - 64, YRES/2 + 224, 0)
add_edge(matrix, XRES/2 - 64, YRES/2 + 224, 0, XRES/2 + 64, YRES/2 + 224, 0)

add_edge(matrix, XRES/2 + 224, YRES/2 + 64, 0, XRES/2 + 196, YRES/2 - 56, 0)
add_edge(matrix, XRES/2 + 196, YRES/2 - 56, 0, XRES/2 + 48, YRES/2 - 168, 0)
add_edge(matrix, XRES/2 + 48, YRES/2 - 168, 0, XRES/2 - 40, YRES/2 - 140, 0)
add_edge(matrix, XRES/2 - 40, YRES/2 - 140, 0, XRES/2 - 112, YRES/2 - 32, 0)
add_edge(matrix, XRES/2 - 112, YRES/2 - 32, 0, XRES/2 - 84, YRES/2 + 24, 0)
add_edge(matrix, XRES/2 - 84, YRES/2 + 24, 0, XRES/2 - 16, YRES/2 + 56, 0)
add_edge(matrix, XRES/2 - 16, YRES/2 + 56, 0, XRES/2 + 8, YRES/2 + 28, 0)
add_edge(matrix, XRES/2 + 8, YRES/2 + 28, 0, XRES/2 + 7, YRES/2 + 2, 0)
print_matrix(matrix)
draw_lines( matrix, screen, color )

#all octants:
draw_line(screen, XRES/2 + 2, YRES/2 + 7, XRES/2 + 64, YRES/2 + 224, red)
draw_line(screen, XRES/2 + 7, YRES/2 + 2, XRES/2 + 224, YRES/2 + 64, orange)
draw_line(screen, XRES/2 + 7, YRES/2 - 2, XRES/2 + 224, YRES/2 - 64, yellow)
draw_line(screen, XRES/2 + 2, YRES/2 - 7, XRES/2 + 64, YRES/2 - 224, green)
draw_line(screen, XRES/2 - 2, YRES/2 - 7, XRES/2 - 64, YRES/2 - 224, cyan)
draw_line(screen, XRES/2 - 7, YRES/2 - 2, XRES/2 - 224, YRES/2 - 64, blue)
draw_line(screen, XRES/2 - 7, YRES/2 + 2, XRES/2 - 224, YRES/2 + 64, purple)
draw_line(screen, XRES/2 - 2, YRES/2 + 7, XRES/2 - 64, YRES/2 + 224, magenta)
draw_line(screen, XRES/2, 0, XRES/2, YRES-1, color)
draw_line(screen, 0, YRES/2, XRES-1, YRES/2, color)


display(screen)
