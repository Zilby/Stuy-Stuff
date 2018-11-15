from display import *
from draw import *

screen = new_screen()

'''
color = [ 0, 255, 0 ]
matrix = []
#eyes
add_edge(matrix, 100, 50, 0, 150, 50, 0)
add_edge(matrix, 150, 50, 0, 150, 100, 0)
add_edge(matrix, 150, 100, 0, 100, 100, 0)
add_edge(matrix, 100, 100, 0, 100, 50, 0)
add_edge(matrix, 170, 50, 0, 220, 50, 0)
add_edge(matrix, 220, 50, 0, 220, 100, 0)
add_edge(matrix, 220, 100, 0, 170, 100, 0)
add_edge(matrix, 170, 100, 0, 170, 50, 0)
#pupils
add_edge(matrix, 115, 75, 0, 125, 85, 0)
add_edge(matrix, 125, 85, 0, 135, 75, 0)
add_edge(matrix, 135, 75, 0, 125, 65, 0)
add_edge(matrix, 125, 65, 0, 115, 75, 0)
add_edge(matrix, 185, 75, 0, 195, 85, 0)
add_edge(matrix, 195, 85, 0, 205, 75, 0)
add_edge(matrix, 205, 75, 0, 195, 65, 0)
add_edge(matrix, 195, 65, 0, 185, 75, 0)
#mouth
add_edge(matrix, 100, 150, 0, 125, 130, 0)
add_edge(matrix, 125, 130, 0, 160, 145, 0)
add_edge(matrix, 160, 145, 0, 195, 130, 0)
add_edge(matrix, 195, 130, 0, 220, 150, 0)

draw_lines( matrix, screen, color )

'''

color1 = [ 0, 255, 0 ]
matrix1 = []
color2 = [ 0, 0, 255 ]
matrix2 = []
color3 = [ 255, 0, 0 ]
matrix3 = []
color4 = [ 255, 255, 0 ]
matrix4 = []

for x in range(0,YRES,30):
    add_edge( matrix1, 0, x, 0, XRES, YRES, 0 )
    add_edge( matrix2, XRES, x, 0, 0, YRES, 0 )
    add_edge( matrix3, 0, x, 0, XRES, 0, 0 )
    add_edge( matrix4, XRES, x, 0, 0, 0, 0 )


draw_lines(matrix1, screen, color1)
draw_lines(matrix2, screen, color2)
draw_lines(matrix3, screen, color3)
draw_lines(matrix4, screen, color4)


display(screen)

save_ppm(screen, "image.ppm")
