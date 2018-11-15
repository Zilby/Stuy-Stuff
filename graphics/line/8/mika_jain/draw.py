from display import *
from matrix import *
import math
import itertools

def add_edge( matrix, l0, l1, color):
	matrix.append([color]+l0+[1])
	matrix.append([color]+l1+[1])

def add_point( matrix, l, color):
	matrix.append([color]+l+[1]) #TREATS STAND-ALONE POINT AS LINE WITH NO LENGTH, USEFUL FOR TRANSFORMATIONS
	matrix.append([color]+l+[1])

def plot( matrix, screen ): #WHERE HYPERDIMENSIONAL TRANFORMATIONS OCCUR
	i = 0
	while i < len(matrix):
		if matrix[i] == matrix[i+1]:
			point = matrix[i][1:-1]
			plot_point(screen, matrix[i][0], point[0], point[1])
		else:
			point0 = matrix[i][1:-1]
			point1 = matrix[i+1][1:-1]
			plot_line( screen, matrix[i][0], point0[0], point0[1], point1[0], point1[1] )
		i += 2

def plot_point( screen, color, x, y ):
    x = int(len(screen[0])/2 + x + 0.5)
    y = int(len(screen)/2 - y + 0.5)
    if ( x >= 0 and x < len(screen[0]) and y >= 0 and y < len(screen)):
        screen[y][x] = color[:]

def plot_line( screen, color, x0, y0, x1, y1):
    if y1-y0 > x1-x0 >= 0:
        octant = 2
        x0,y0=y0,x0
        x1,y1=y1,x1
    elif y1-y0 > abs(x1-x0) and x1-x0 < 0:
        octant = 3
        x0,y0=y0,-x0
        x1,y1=y1,-x1
    elif abs(x1-x0) >= y1-y0 > 0 and x1-x0 < 0:
        octant = 4
        x0,y0=-x0,y0
        x1,y1=-x1,y1
    elif abs(x1-x0) > abs(y1-y0) and x1-x0 < 0 and y1-y0 <= 0:
        octant = 5
        x0,y0=-x0,-y0
        x1,y1=-x1,-y1
    elif abs(y1-y0) >= abs(x1-x0) and x1-x0 < 0 and y1-y0 < 0:
        octant = 6
        x0,y0=-y0,-x0
        x1,y1=-y1,-x1
    elif abs(y1-y0) > abs(x1-x0) and x1-x0 >= 0 and y1-y0 < 0:
        octant = 7
        x0,y0=-y0,x0
        x1,y1=-y1,x1
    elif abs(x1-x0) >= abs(y1-y0) and x1-x0 > 0 and y1-y0 < 0:
        octant = 8
        x0,y0=x0,-y0
        x1,y1=x1,-y1
    else:
        octant = 1
        x = x0
        y = y0
    x = x0
    y = y0
    a = 2*(y1-y0)     
    b = 2*(x0-x1)       
    d = a + 0.5*b       
    while x <= x1:
        if octant == 2:
            plot_point( screen, color, y, x )
        elif octant == 3:
            plot_point( screen, color, -y, x )
        elif octant == 4:
            plot_point( screen, color, -x, y )
        elif octant == 5:
            plot_point( screen, color, -x, -y )
        elif octant == 6:
            plot_point( screen, color, -y, -x )
        elif octant == 7:
            plot_point( screen, color, y, -x )
        elif octant == 8:
            plot_point( screen, color, x, -y )
        else:
            plot_point( screen, color, x, y )
        if d>0:
            y+=1
            d+=b
        x+=1
        d+=a
