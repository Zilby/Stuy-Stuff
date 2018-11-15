from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )


#draw_lines( matrix, screen, color )

#display(screen)

print matrix
print len(matrix)
L = ident(new_matrix())
print scalar_mult(matrix, 5)
print matrix_mult(matrix, L)
