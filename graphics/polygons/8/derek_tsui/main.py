from display import *
from draw import *
import random

screen = new_screen()
color = [ 150, 200, 150 ]
matrix = []

f= open ("script_c",'w')
cx=250
cy=250
r=200

f.write("p\n400 250 0 20 20 20\n")
f.write("p\n300 300 10 30 30 30\n")
f.write("p\n250 600 10 40 40 40\n")
x0 = cx + r
y0 = cy
t = 0.01
while (t <= 1.01):
    theta = (2 * t * math.pi)
    x1 = cx + r * math.cos(theta)
    y1 = cy + r * math.sin(theta)
    f.write("m\n"+str(x0)+" "+str(y0)+" "+str(150*((-1*t*t)+(1.12*t)))+"\n")
    x0 = x1
    y0 = y1
    t += 0.10
f.write("i\n")
f.write("x\n50\n")
f.write("y\n20\n")
f.write("z\n20\n")
f.write("t\n55 200 0\n")
f.write("a\n")

f.write("p\n250 250 250 10 10 10\n")

f.write("d\n325 340 20 100\n")
f.write("d\n325 370 20 100\n")
f.write("d\n325 400 20 100\n")
f.write("i\n")
f.write("x\n10\n")
f.write("z\n10\n")
#f.write("y\n30\n")
f.write("t\n100 -200 0\n")
f.write("a\n")

f.write("v\ng\n3d.png\nq\n")
f.close

#octant I
# add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
# add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
# add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
#
# draw_lines( matrix, screen, color )
#
# display(screen)
