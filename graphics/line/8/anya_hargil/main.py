
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

for i in range(500):
    add_edge(matrix, i, i%23, 0, i+75, i, 0)

draw_lines( matrix, screen, color )
matrix =[]

for i in range(100):
    add_edge(matrix, 0, 500, 0, i*25, 0, 0)

color = [255, 89, 140]
draw_lines( matrix, screen, color )
matrix =[]

for i in range(100):
    add_edge(matrix, 0, 0, 0, 500, i*30, 0)

color = [63, 72, 196]
draw_lines( matrix, screen, color )


display(screen)
