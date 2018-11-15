from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

pts = [  [0, 100, 0, 1],
        [100, 100, 0, 1],
        [100, 0, 0, 1],
        [0, 0, 0, 1],
        [20, 0, 0, 1],
        [30, 0, 0, 1]]
trans = [  [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]
'''
#octant I
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )

draw_lines( matrix, screen, color )

display(screen)
'''
print "PTS:"
print_matrix(pts)
mt = make_scale(3, 3, 0)

print "TRANS:"
print_matrix(mt)
pts = matrix_mult(pts, mt)
print "PTS MODIFIED:"
print_matrix(pts)

print "TRANS:"
print_matrix(trans)
pts = matrix_mult(pts, trans) #matrix_multi doesn't modify m2
print "PTS MODIFIED:"
print_matrix(pts)


