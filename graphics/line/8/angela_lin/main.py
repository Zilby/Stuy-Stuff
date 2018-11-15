from display import *
from draw import *
import random

screen = new_screen()
z = 0

for a in range(5):
    matrix = []
    color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    for i in range(50):
        add_edge(matrix, i*10, (100*a) + i*10, z, i*10, 100 + (a*100) + i*10, z)
        add_edge(matrix, i*10, i*10 + (100*a), z, i*10 + 100, i*10 + (100*a), z)
    draw_lines( matrix, screen, color )

for a in range(5):
    matrix = []
    color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    for i in range(50):
        add_edge(matrix, i*10 + (100*a), i*10, z, i*10 + (100*a), 100 + i*10, z)
        add_edge(matrix, i*10 + (100*a), i*10, z, i*10 + 100 + (100*a), i*10, z)
    draw_lines( matrix, screen, color )

for a in range(5):
    matrix = []
    color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    for i in range(50):
        add_edge(matrix, XRES-(i*10 + (100*a)), YRES-i*10, z, XRES-(i*10 + (100*a)), YRES-(100 + i*10), z)
        add_edge(matrix, XRES-(i*10 + (100*a)), YRES-i*10, z, XRES-(i*10 + 100 + (100*a)), YRES-i*10, z)
    draw_lines( matrix, screen, color )

for a in range(5):
    matrix = []
    color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
    for i in range(50):
        add_edge(matrix, XRES-i*10, YRES-((100*a) + i*10), z, XRES-i*10, YRES-(100 + (a*100) + i*10), z)
        add_edge(matrix, XRES-i*10, YRES-(i*10 + (100*a)), z, XRES-(i*10 + 100),YRES-( i*10 + (100*a)), z)
    draw_lines( matrix, screen, color )

draw_lines( matrix, screen, color )
display(screen)

############################################################

screen_two = new_screen()
matrix = []
color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
add_edge(matrix, 0, 0, z, 500, 0, z)
add_edge(matrix, 0, 0, z, 500, 0, z)
add_edge(matrix, 500, 0, z, 500, 500, z)
add_edge(matrix, 0, 500, z, 500, 500, z)
color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255)]
add_edge(matrix, 0, 0, z, 500, 500, z);
add_edge(matrix, 500, 0, z, 0, 500, z)

draw_lines(matrix, screen, color)
display(screen)
