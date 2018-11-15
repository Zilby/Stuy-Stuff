from display import *
from matrix import *


#Go through matrix 2 entries at a time and call
#draw_line on each pair of ponts
def draw_lines( matrix, screen, color ):
	for point in range(0, len(matrix[0]) - 3):
		draw_line2( screen, matrix[0][point], matrix[1][point], matrix[0][point+1], matrix[1][point+1], color )

#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
	# for x in range(x0, x1 + 1):
	# 	for y in range(y0, y1 + 1):
	# 		add_point( matrix, x, y, 0)
	add_point( matrix, x0, y0, z0 )
	add_point( matrix, x1, y1, z1 )
	add_point( matrix, 0, 0, 0 )

#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
	point = [x, y, z, 1]
	for i in range(0,4):
		matrix[i].append(point[i])

#Plot all the pixels needed to draw line (x0, y0) - (x1, y1)
#to screen with color


def draw_line1( screen, x0, y0, x1, y1, color ):
	A = 2 * (y1 - y0)
	B = -2 * ( x1 - x0 )
	d = A + B/2
	x = x0
	y = y0
	while (x < x1):
		plot(screen, color, x, y)
		if (d > 0):
			y += 1
			d += B
		x += 1
		d+= A

def draw_line2( screen, x0, y0, x1, y1, color ):
	A = 2 * (y1 - y0)
	B = -2 * ( x1 - x0 )
	d = A/2 + B
	x = x0
	y = y0
	while (y < y1):
		plot(screen, color, x, y)
		if (d < 0):
			x += 1
			d += A
		y += 1
		d += B

## Does not work yet; have to draw quadrants
# def draw_line3( screen, x0, y0, x1, y1, color ):
# 	A = 2 * (y1 - y0)
# 	B = -2 * ( x1 - x0 )
# 	d = A - B/2
# 	x = x0
# 	y = y0
# 	while (x < x1):
# 	plot(screen, color, x, y)
# 	if (d > 0):
# 		y -= 1
# 		d += A
# 	x += 1
# 	d += B 
