from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


#octant I
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

#m3 = make_translate(50,-50,0)
#m3 = make_rotZ( 40)
m3 = make_scale(1,2,1)
matrix = matrix_mult(m3,matrix)

draw_lines( matrix, screen, color )



display(screen)

m1 = []

m1.append([1 , 2, 3 , 4 , 5])
m1.append([4 , 5, 6 , 4 , 3])
m1.append([7 , 8, 9 , 5, 2])

print_matrix(m1)

m2 = []
m2.append([2 ,3, 4])
m2.append([1 ,3, 5])
m2.append([2 ,6, 4])
m2.append([1 ,3, 4])

print_matrix(m2)

print_matrix(matrix_mult(m1,m2))
#print_matrix(m2)

