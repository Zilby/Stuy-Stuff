from display import *
from draw import *

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = []

#left eye
add_edge(matrix, 100, 50, 0, 50, 150, 0 )
add_edge(matrix, 100, 50, 0, 150, 150, 0 )
add_edge(matrix, 50, 150, 0, 150, 150, 0 )

#right eye
add_edge(matrix, XRES - 100, 50, 0, XRES - 50, 150, 0 )
add_edge(matrix, XRES - 100, 50, 0, XRES - 150, 150, 0 )
add_edge(matrix, XRES -50, 150, 0, XRES - 150, 150, 0 )
draw_lines( matrix, screen, color )



matrix = []
color = [ 0, 255, 0 ]
#nose
add_edge(matrix, 250, 200, 0, 300, 300, 0 )
add_edge(matrix, 250, 300, 0, 300, 300, 0 )
draw_lines( matrix, screen, color )


matrix = []
color = [ 255, 0, 0 ]

#mouth
add_edge(matrix, XRES - 50, YRES - 100, 0, 250, YRES - 90, 0 )
add_edge(matrix, 250, YRES - 90, 0, 50, YRES - 100, 0 )

add_edge(matrix, XRES - 50, YRES - 50, 0, 250, YRES - 40, 0 )
add_edge(matrix, 250, YRES - 40, 0, 50, YRES - 50, 0 )

add_edge(matrix, XRES - 50, YRES - 100, 0, XRES - 50, YRES - 50, 0 )
add_edge(matrix, 50, YRES - 100, 0, 50, YRES - 50, 0 )


draw_lines( matrix, screen, color )

#Horizontal
#add_edge(matrix, 0, 50, 0, XRES - 1, 50, 0 )
#1st
#add_edge(matrix, 0, YRES - 1, 0, XRES - 1, YRES - 10, 0 )
#2nd
#add_edge(matrix, 0, YRES - 1, 0, XRES - 100, 0 , 0 )
#3rd
#add_edge(matrix, 0, 0, 0, XRES, 100, 0 )
#4th
#add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
#add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
#Vertical
#add_edge(matrix, 50, 0, 0, 50, YRES - 1, 0 )



display(screen)
