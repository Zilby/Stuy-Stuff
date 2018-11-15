from display import *
from draw import *

screen = new_screen()
red = [ 255, 0, 0 ]
yellow = [ 250, 200, 50 ]
orange = [ 255, 100, 50 ]
green = [ 0, 255, 0 ]
blue = [ 0, 0, 255 ]

matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []

boo = 1
j = 0
while(j < YRES):
    i=0
    while(i < XRES):
        m = 0
        while( m <100 ):
            if(boo == 1):
                add_edge(matrix4, m+i, j, 0,  m+i, j+100, 0 )
                add_edge(matrix2, i, j+100, 0,  i+m, j, 0 )
            else:
                add_edge(matrix1, i, j+m, 0,  i+100, j+m, 0 )
                add_edge(matrix5, i, j+m, 0,  i+100, j, 0 )
            m += 10
        boo = -boo
        i += 100
    j += 100

draw_lines( matrix1, screen, red )
draw_lines( matrix2, screen, orange )
#draw_lines( matrix3, screen, green )
draw_lines( matrix4, screen, yellow )
draw_lines( matrix5, screen, blue )


display(screen)
