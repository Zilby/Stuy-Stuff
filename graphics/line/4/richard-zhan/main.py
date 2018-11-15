from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
# add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
# add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

# add_edge(matrix,0,400,0,250,300,0)
# add_edge(matrix,0,300,0,250,200,0)
# add_edge(matrix,0,150,0,450,325,0)

add_edge(matrix,0,250,0,250,0,0)
add_edge(matrix,250,0,0,499,250,0)
add_edge(matrix,499,250,0,250,499,0)
add_edge(matrix,250,499,0,0,250,0)
draw_lines( matrix, screen, color )
matrix=[]
add_edge(matrix,125,125,0,375,125,0)
add_edge(matrix,375,125,0,375,375,0)
add_edge(matrix,375,375,0,125,375,0)
add_edge(matrix,125,375,0,125,125,0)
# add_edge(matrix,0,250,0,250,0,0)
color = [255,0,0]
draw_lines(matrix,screen,color)

display(screen)
