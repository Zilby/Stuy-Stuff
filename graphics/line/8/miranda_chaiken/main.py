from display import *
from draw import *

screen = new_screen()
green = [ 0, 255, 0 ]
blue = [ 0, 0, 255 ]
matrix = []

i=50

while i < YRES:
    add_edge(matrix, XRES-1, 0, 0, 50+(i/4), YRES - i, 0 )
    add_edge(matrix, XRES-1, 0, 0, i, YRES - 50-(i/4), 0 )
    add_edge(matrix, XRES-1, YRES - 1, 0, 50+i/4, i, 0 )
    add_edge(matrix, XRES-1, YRES - 1, 0, i, 50+i/4, 0 )
    add_edge(matrix, 0, 0, 0, XRES - 50- (i/4), YRES - i, 0 )
    add_edge(matrix, 0, 0, 0, XRES - i, YRES - 50- (i/4), 0 )
    add_edge(matrix, 0, YRES - 1, 0, XRES - 50- (i/4), i, 0 )
    add_edge(matrix, 0, YRES - 1, 0, XRES - i, 50+(i/4), 0  )
    draw_lines(matrix,screen,[( (i)/2 ) %255,0,i/2 %255])
    matrix=[]
    i+=8
i=0
while i < 200:
    add_edge(matrix, XRES/2, YRES/2, 0, 10+(i/4), YRES - i, 0 )
    add_edge(matrix, XRES/2, YRES/2, 0, i, YRES - 10-(i/4), 0 )
    add_edge(matrix, XRES/2, YRES/2, 0, 10+i/4, i, 0 )
    add_edge(matrix, XRES/2, YRES/2, 0, i, 10+i/4, 0 )
    add_edge(matrix, XRES/2, YRES/2, 0, XRES - 10- (i/4), YRES - i, 0 )
    add_edge(matrix, XRES/2, YRES/2, 0, XRES - i, YRES - 10- (i/4), 0 )
    add_edge(matrix, XRES/2,  YRES/2, 0, XRES - 10- (i/4), i, 0 )
    add_edge(matrix, XRES/2,YRES/2, 0, XRES - i, 10+(i/4), 0  )
    draw_lines(matrix,screen,blue)
    matrix=[]
    i+=5

print_matrix(matrix)


save_ppm(screen,"image.ppm")
display(screen)
