from display import *
from draw import *
import math
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

'''
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
'''
x = 0
while(x < XRES):
    #y = int(math.sqrt(random.randint(0,math.pow(YRES,2))))
    y = int(math.pow(x,2))
    y = int(math.sin(0.05*x)*YRES/2)+YRES/2
    y1 = int(math.sin(0.05*(x+1))*YRES/2)+YRES/2
    add_edge(matrix, x, y, 0, x+1, y1,0)
    x += 1 

draw_lines( matrix, screen, color )

matrix=[]
x=0
color = [255, 0, 0]
while(x < XRES):
    #y = int(math.sqrt(random.randint(0,math.pow(YRES,2))))
    y = int(math.pow(x,2))
    y = int(-1*math.sin(0.05*x)*YRES/2)+YRES/2
    y1 = int(-1*math.sin(0.05*(x+1))*YRES/2)+YRES/2
    add_edge(matrix, x, y, 0, x+1, y1,0)
    x += 1 

draw_lines( matrix, screen, color )

matrix=[]
x = 0
while(x < XRES):
    #y = int(math.sqrt(random.randint(0,math.pow(YRES,2))))
    y = int(math.pow(x,2))
    y = int(math.cos(0.05*x)*YRES/2)+YRES/2
    y1 = int(math.cos(0.05*(x+1))*YRES/2)+YRES/2
    add_edge(matrix, x, y, 0, x+1, y1,0)
    x += 1 

matrix=[]
x=0
color = [0, 0, 255]
while(x < XRES):
    #y = int(math.sqrt(random.randint(0,math.pow(YRES,2))))
    y = int(math.pow(x,2))
    y = int(-1*math.cos(0.05*x)*YRES/2)+YRES/2
    y1 = int(-1*math.cos(0.05*(x+1))*YRES/2)+YRES/2
    add_edge(matrix, x, y, 0, x+1, y1,0)
    x += 1 



draw_lines( matrix, screen, color )


display(screen)
