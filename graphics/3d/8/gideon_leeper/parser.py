from display import *
from matrix import *
from draw import *
import math

def parse_file( fname, points, transform ):
	f = open(fname, 'r')
	screen = new_screen()
	while 1:
		l = f.readline()
		if len(l) == 0:
			break
		if l[0] in 'lchbpmdstxyz':
			s = map(float, f.readline().split(' '))
		if l[0] == 'l':
			add_edge(points, *s)
		elif l[0] == 'c':
			add_circle(points, *s)
		elif l[0] == 'h':
			add_hermite(points, *s)
		elif l[0] == 'b':
			add_bezier(points, *s)
		elif l[0] == 'p':
			add_prism(points, *s)
		elif l[0] == 'm':
			add_sphere(points, *s)
		elif l[0] == 'd':
			add_torus(points, *s)
		elif l[0] == 'i':
			transform = ident(transform)
		elif l[0] == 's':
			transform = matrix_mult(make_scale(*s), transform)
		elif l[0] == 't':
			transform = matrix_mult(make_translate(*s), transform)
		elif l[0] == 'x' or l[0] == 'y' or l[0] == 'z':
			func = [make_rotX, make_rotY, make_rotZ][ord(l[0])-ord('x')]
			transform = matrix_mult(func(s[0]*math.pi / 180.0), transform)
		elif l[0] == 'a':
			points = matrix_mult(points, transpose(transform))
		elif l[0] == 'w':
			points = []
		elif l[0] == 'v':
			draw_lines(points, screen, [255, 255, 255])
			display(screen)
		elif l[0] == 'g':
			s = f.readline().strip()
			draw_lines(points, screen, [255, 255, 255])
			save_extension(screen, s)
			clear_screen(screen)

points = []
transform = new_matrix()

parse_file( 'script', points, transform )
