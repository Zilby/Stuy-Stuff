from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script","w")
for x in xrange(25):
    f.write("b\n")
    f.write("0 250 " + str(random.randint(0,250)) + " " + str(random.randint(0,500)) + " " + str(random.randint(250,500)) + " " + str(random.randint(0,500))+ " 500 250"+ "\n")
    f.write("h\n")
    f.write("250 0 " + str(random.randint(0,500)) + " " + str(random.randint(0,250)) + " 250 500 " + str(random.randint(0,500)) + " " + str(random.randint(250,500))+ "\n")
f.write("c\n250 250 200\n")
f.write("v\ng\nimage.png")
f.close

# #octant I
# add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
# add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

# draw_lines( matrix, screen, color )

# display(screen)
