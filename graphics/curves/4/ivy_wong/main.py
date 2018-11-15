from display import *
from draw import *
from random import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
'''add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
'''
#draw_lines( matrix, screen, color )

#display(screen)

f = open("script_r",'w')
for r in range(0,500,2):
    if randint(0,2) < 1:
        f.write("h\n%d %d %d %d %d %d %d %d\n"%(r, 0, randint(0,500), randint(0,250), 0, r, randint(250,500), randint(0,500)))
    else:
        f.write("h\n%d %d %d %d %d %d %d %d\n"%(r, XRES, randint(0,250), randint(0,250), YRES, r, randint(0,500), randint(0,500)))
        
f.write("v\ng\ntest.png")
