from display import *
from draw import *
import random
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

for i in range(10):
    x = random.randrange(XRES)
    y = random.randrange(YRES)
    add_edge(matrix, x, y , 0, XRES - x, YRES - y, 0)
    
#octant I
#add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
#add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

display(screen)
