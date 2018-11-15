from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
#add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
#add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

#These are the line tests that I used:
#add_edge(matrix, 0, 0, 0, 100, 80, 0)
#add_edge(matrix, 200, 100, 0, 0, 0, 0)
#add_edge(matrix, 0, 0, 0, 80, 100, 0)
#dd_edge(matrix, 100, 200, 0, 0, 0, 0)
#add_edge(matrix, 100, 50, 0, 200, 0, 0)
#add_edge(matrix, 200, 0, 0, 100, 80, 0)
#add_edge(matrix, 100, 200, 0, 200, 0, 0)
#add_edge(matrix, 200, 0, 0, 100, 150, 0)
#add_edge(matrix, 100, 100, 0, 200, 100, 0)
#add_edge(matrix, 100, 100, 0, 100, 200, 0)
#add_edge(matrix, 100, 100, 0, 200, 200, 0)
#add_edge(matrix, 100, 200, 0, 200, 100, 0)

#This is my drawing:
#Eye 1:
add_edge(matrix, 100, 50, 0, 150, 70, 0)
add_edge(matrix, 150, 70, 0, 100, 90, 0)
add_edge(matrix, 100, 90, 0, 50, 70, 0)
add_edge(matrix, 50, 70, 0, 100, 50, 0)

#Eye 2
add_edge(matrix, 200, 50, 0, 250, 70, 0)
add_edge(matrix, 250, 70, 0, 200, 90, 0)
add_edge(matrix, 200, 90, 0, 150, 70, 0)
add_edge(matrix, 150, 70, 0, 200, 50, 0)

#Mouth
add_edge(matrix, 50, 120, 0, 250, 120, 0)
add_edge(matrix, 50, 120, 0, 100, 200, 0)
add_edge(matrix, 100, 200, 0, 200, 200, 0)
add_edge(matrix, 200, 200, 0, 250, 120, 0)

#print_matrix(matrix)

draw_lines( matrix, screen, color )

display(screen)

save_ppm(screen, "line.ppm")
