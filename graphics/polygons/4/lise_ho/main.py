from display import *
from draw import *
from parser import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

def randcolor():
    return [random.randrange(255),random.randrange(255),random.randrange(255)]

color=randcolor()
#octant I
'''
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

display(screen)
'''
parse_file( 'script_c', points, poly, transform )
