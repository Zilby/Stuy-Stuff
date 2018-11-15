from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

def randcolor():
    return [random.randrange(255),random.randrange(255),random.randrange(255)]

#octant I
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

#display(screen)
m1 = [[1,4],[2,5],[3,6]]
'''
1 2 3 
4 5 6 
'''
m2 = [[7,9,11],[8,10,12]]
'''
7 8 
9 10 
11 12 
'''


'''
you should get
58 634
139 154
'''
matrix_mult(m1,m2)
