from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

#add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
#add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
#add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

vertices = [ (150,50) , (350, 50) , (150, 450), (350, 450), (25, 250), (475, 250)]

for i in range(6):
    for j in range(i+1, 6):
        add_edge(matrix, vertices[i][0], vertices[i][1], 0, 
                 vertices[j][0], vertices[j][1], 0)



draw_lines( matrix, screen, color )

display(screen)
