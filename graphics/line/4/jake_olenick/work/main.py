from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

##octant I

theta = 0.0
phi = 0.0

while (theta < math.pi/2):
    R = int((theta/(math.pi/2)) * 255.0)
    clr = [R,0,0]
    draw_line(screen,0,0,int(XRES*math.cos(theta)),int(YRES*math.sin(theta)),clr)
    theta += math.pi/300

while (phi < math.pi/2):
    B = int((phi/ (math.pi/2)) * 255.0)
    clr = [ 0,0,B ]
    draw_line(screen,0,499,int(500*math.cos(phi)),int(500 - 500*math.sin(phi)),clr)
    phi += math.pi/300


add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

display(screen)
