from display import *
from draw import *

screen = new_screen()
GREEN = [ 0, 255, 0 ]
RED = [ 255, 0, 255 ]
BLUE = [ 0, 0, 255]
matrix = new_matrix()
# add_point(matrix, 250, 250)
# add_point(matrix, 500, 200)
#add_edge(matrix, 2, 4, 0, 3, 4, 0 )
#print_matrix(matrix)

#octant I
## X-AXIS
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
# add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
print_matrix(matrix)
draw_lines( matrix, screen, GREEN )
draw_line2(screen, 0, 0, XRES - 1, YRES - 75, GREEN)

display(screen)
