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
		if l[0] == 'l':
			s = map(float, f.readline().split(' '))
			add_edge(points, s[0], s[1], s[2], s[3], s[4], s[5])
		elif l[0] == 'i':
			transform = ident(transform)
		elif l[0] == 's':
			s = map(float, f.readline().split(' '))
			transform = matrix_mult(make_scale(s[0], s[1], s[2]), transform)
		elif l[0] == 't':
			s = map(float, f.readline().split(' '))
			transform = matrix_mult(make_translate(s[0], s[1], s[2]), transform)
		elif l[0] == 'x' or l[0] == 'y' or l[0] == 'z':
			func = [make_rotX, make_rotY, make_rotZ][ord(l[0])-ord('x')]
			s = float(f.readline())
			transform = matrix_mult(func(s*math.pi / 180.0), transform)
		elif l[0] == 'a':
			points = matrix_mult(points, transpose(transform))
		elif l[0] == 'v':
		#	print points
			draw_lines(points, screen, [255, 255, 255])
			display(screen)
		elif l[0] == 'g':
			s = f.readline().strip()
			draw_lines(points, screen, [255, 255, 255])
			save_extension(screen, s)
			clear_screen(screen)

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
