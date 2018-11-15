from display import *
from matrix import *
from math import *

def add_polygon(points, x0, y0, z0, x1, y1, z1, x2, y2, z2):
	add_point(points, x0, y0, z0)
	add_point(points, x1, y1, z1)
	add_point(points, x2, y2, z2)

def draw_polygons(points, screen, color):
	for i in range(0, len(points)-1, 3):
		#perspective
		#x0 = 250 + ((points[i][0]-250) * 750)/points[i][2]
		#y0 = 250 + ((points[i][1]-250) * 750)/points[i][2]
		#x1 = 250 + ((points[i+1][0]-250) * 750)/points[i+1][2]
		#y1 = 250 + ((points[i+1][1]-250) * 750)/points[i+1][2]
		#x2 = 250 + ((points[i+2][0]-250) * 750)/points[i+2][2]
		#y2 = 250 + ((points[i+2][1]-250) * 750)/points[i+2][2]
		#draw_line(screen, x0, y0, x1, y1, color)
		#draw_line(screen, x1, y1, x2, y2, color)
		#draw_line(screen, x2, y2, x0, y0, color)
		#no perspective
		draw_line(screen, points[i][0], points[i][1], points[i+1][0], points[i+1][1], color)
		draw_line(screen, points[i+1][0], points[i+1][1], points[i+2][0], points[i+2][1], color)
		draw_line(screen, points[i+2][0], points[i+2][1], points[i][0], points[i][1], color)

def add_curve(points, start, stop, res, v):
	def compose(f, t):
		return [x(t) for x in f]
	x0, y0, z0, = compose(v, start)
	for i in range(res):
		x1, y1, z1, = compose(v, start + float(((stop - start)*(i+1)))/res)
		add_edge(points, x0, y0, z0, x1, y1, z1)
		x0, y0, z0 = x1, y1, z1

def add_circle(points, cx, cy, cz, r):
	def x(t):
		return cx + r*cos(t)
	def y(t):
		return cy + r*sin(t)
	def z(t):
		return cz
	add_curve(points, 0, 2*pi, 100, [x, y, z])

def add_hermite(points, x0, y0, x1, y1, x2, y2, x3, y3):
	a3, a2, a1, a0 = 2*x0 + x1 - 2*x2 + x3, -3*x0 - 2*x1 + 3*x2 - x3, x1, x0
	b3, b2, b1, b0 = 2*y0 + y1 - 2*y2 + y3, -3*y0 - 2*y1 + 3*y2 - y3, y1, y0
	def x(t):
		return a0 + t*(a1 + t*(a2 + t*a3))
	def y(t):
		return b0 + t*(b1 + t*(b2 + t*b3))
	def z(t):
		return 750
	add_curve(points, 0, 1, 100, [x, y, z])

def add_bezier(points, x0, y0, x1, y1, x2, y2, x3, y3):
	a3, a2, a1, a0 = -x0 + 3*x1 - 3*x2 + x3, 3*x0 - 6*x1 + 3*x2, -3*x0 + 3*x1, x0
	b3, b2, b1, b0 = -y0 + 3*y1 - 3*y2 + y3, 3*y0 - 6*y1 + 3*y2, -3*y0 + 3*y1, y0
	def x(t):
		return a0 + t*(a1 + t*(a2 + t*a3))
	def y(t):
		return b0 + t*(b1 + t*(b2 + t*b3))
	def z(t):
		return 750
	add_curve(points, 0, 1, 100, [x, y, z])

def add_prism(points, x, y, z, w, h, d):
	add_polygon(points, x, y, z, x+w, y, z, x, y+h, z)
	add_polygon(points, x, y, z, x, y+h, z, x, y, z+d)
	add_polygon(points, x, y, z, x, y, z+d, x+w, y, z)
	add_polygon(points, x+w, y, z, x+w, y+h, z, x, y+h, z)
	add_polygon(points, x, y+h, z, x, y+h, z+d, x, y, z+d)
	add_polygon(points, x, y, z+d, x+w, y, z+d, x+w, y, z)
	add_polygon(points, x+w, y+h, z, x, y+h, z, x, y+h, z+d)
	add_polygon(points, x, y+h, z+d, x, y, z+d, x+w, y, z+d)
	add_polygon(points, x+w, y, z+d, x+w, y, z, x+w, y+h, z)
	add_polygon(points, x+w, y+h, z, x+w, y+h, z+d, x, y+h, z+d)
	add_polygon(points, x, y+h, z+d, x+w, y+h, z+d, x+w, y, z+d)
	add_polygon(points, x+w, y, z+d, x+w, y+h, z+d, x+w, y+h, z)

def add_sphere(points, x, y, z, r):
	def f(i, j):
		return [x + r*cos(pi*i / res), 
			y + r*sin(pi*i / res)*cos(pi*j / res), 
			z + r*sin(pi*i / res)*sin(pi*j / res)]
	res = 20
	for i in range(res): 		#vert
		for j in range(2*res): 	#rot
			a = f(i, j)
			b = f((i+1)%(2*res), j)
			c = f((i+1)%(2*res), (j+1)%(2*res))
			d = f(i, (j+1)%(2*res))
			add_polygon(points, a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2])
			add_polygon(points, c[0], c[1], c[2], d[0], d[1], d[2], a[0], a[1], a[2])

def add_torus(points, x, y, z, r1, r2):
	res1 = 10
	res2 = 30
	def f(i, j):
		return [x + cos(2*pi*j / res2) * (r2 + r1*cos(2*pi*i / res1)), 
			y + r1*sin(2*pi*i / res1), 
			sin(2*pi*j / res2) * (r2 + r1*cos(2*pi*i / res1))]
	for i in range(res1):
		for j in range(res2):
			a = f(i, j)
			b = f((i+1)%res1, j)
			c = f((i+1)%res1, (j+1)%res2)
			d = f(i, (j+1)%res2)
			add_polygon(points, a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2])
			add_polygon(points, c[0], c[1], c[2], d[0], d[1], d[2], a[0], a[1], a[2])

def draw_lines(matrix, screen, color):	
	for i in range(0, len(matrix)-1, 2):
		#perspective
		#x0 = 250 + ((matrix[i][0]-250) * 750)/matrix[i][2]
		#y0 = 250 + ((matrix[i][1]-250) * 750)/matrix[i][2]
		#x1 = 250 + ((matrix[i+1][0]-250) * 750)/matrix[i+1][2]
		#y1 = 250 + ((matrix[i+1][1]-250) * 750)/matrix[i+1][2]
		#draw_line(screen, x0, y0, x1, y1)
		#no perspective
		draw_line(screen, matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], color)

def add_edge(matrix, x0, y0, z0, x1, y1, z1):
	add_point(matrix, x0, y0, z0)
	add_point(matrix, x1, y1, z1)

def add_point(matrix, x, y, z=0):
	matrix.append([x, y, z, 1])

def draw_line(screen, x0, y0, x1, y1, color):
	x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
	if x1 < x0:
		temp = x1
		x1 = x0
		x0 = temp
		temp = y1
		y1 = y0
		y0 = temp
	x, y = x0, y0
	A, B = 2*(y1 - y0), -2*(x1 - x0)
	if y1 >= y0:
		if y1 - y0 <= x1 - x0:
			d = A + B/2
			while x <= x1:
				plot(screen, color, x, y)
				if d > 0:
					y += 1
					d += B
				x += 1
				d += A
		else:
			d = A/2 + B
			while y <= y1:
				plot(screen, color, x, y)
				if d < 0:
					x += 1
					d += A
				y += 1
				d += B
	else:
		if y0 - y1 <= x1 - x0:
			d = A - B/2
			while x <= x1:
				plot(screen, color, x, y)
				if d < 0:
					y -= 1
					d -= B
				x += 1
				d += A
		else:
			d = A/2 - B
			while y >= y1:
				plot(screen, color, x, y)
				if d > 0:
					x += 1
					d += A
				y -= 1
				d -= B
