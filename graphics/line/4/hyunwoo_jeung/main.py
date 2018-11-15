from display import *
from draw import *
import random
import math

screen = new_screen()
color = [ 100, 0, 100 ]
color2 = [0,255,0]
matrix = []
matrix2 = []


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]


add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
add_edge(matrix, XRES-1,YRES-1,0,0,0,0)

#random lines are green
random.seed(23)

for n in range(20):
    add_edge(matrix2, random.randint(0,XRES),random.randint(0,XRES),0,random.randint(0,XRES),random.randint(0,XRES),0)
draw_lines(matrix,screen,color)
draw_lines(matrix2,screen,color2)
display(screen)
