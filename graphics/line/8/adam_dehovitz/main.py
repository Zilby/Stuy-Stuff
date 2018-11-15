from display import *
from draw import *

screen = new_screen()
color = [ 255, 0, 0 ]
matrix = []



increment = 5
constant = increment * -1
while ("PIGS" != "FLY"):
    constant = constant + increment
    add_point( matrix, 0 + constant, 0 + constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, XRES- constant, 0+ constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, XRES- constant, YRES- constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, 0+ constant, YRES- constant)
    if (constant>=XRES/2):
        break
    

draw_lines( matrix, screen, color )

color = [ 0, 255, 0 ]
matrix = []



increment = 5
constant = 5
while ("PIGS" != "FLY"):
    constant = constant + increment
    add_point( matrix, 0 + constant, 0 + constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, XRES- constant, 0+ constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, XRES- constant, YRES- constant)
    if (constant>=XRES/2):
        break
    constant = constant + increment
    add_point( matrix, 0+ constant, YRES- constant)
    if (constant>=XRES/2):
        break
    

draw_lines( matrix, screen, color )



matrix = []
color = [0, 0, 255]
add_edge(matrix, 0, 0, 0, XRES, YRES, 0)
draw_lines( matrix, screen, color )
matrix = []
add_edge(matrix, 0, YRES, 0, XRES, 0, 0)
draw_lines( matrix, screen, color )

display(screen)
