from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script.c",'w')
for i in range (50):
    f.write(str(i *20) + " 350 " + str(i*31) + " 250 " + str(i *20) + " 150 " + str(i*31) + " 400")

f.write("v\n")
f.write("g\n")
f.write("face.png\n")
f.write("q\n")

#octant I
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

display(screen)
