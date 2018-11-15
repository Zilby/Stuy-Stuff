from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

'''
#(0,0) to (499,425) - OCTANT ONE/FIVE
add_edge(matrix, 0, 0, 0, XRES - 1, YRES - 75, 0 )

#(0,0) to (425,499) - OCTANT TWO/SIX
add_edge(matrix, 0, 0, 0, XRES - 75, YRES - 1, 0 )

#(0, 499) to (499, 75) - OCTANT FOUR/EIGHT
add_edge(matrix, 0, YRES - 1, 0, XRES - 1, 75, 0 )


#(0, 499) to (425, 0) - OCTANT THREE/SEVEN
add_edge(matrix, 0, YRES - 1, 0, XRES - 75, 0, 0 )
'''

points = [(250, 500),
          (375, 467),
          (467, 375),
          (500, 250),
          (467, 125),
          (375,34),
          (250, 0),
          (125, 34),
          (34, 125),
          (0, 250),
          (34, 375),
          (125, 467)]

for i in range(len(points)-1):
    x = i + 1
    while (x < len (points)):
        add_edge (matrix, points[i][0], points[i][1], 0, points[x][0], points[x][1],0)
        x+=1
    #add_edge (matrix, points[i][0], points[i][1], 0, points[i+1][0], points [i+1][1], 0)

draw_lines( matrix, screen, color )


display(screen)

