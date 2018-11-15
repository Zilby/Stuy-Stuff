from display import *
from matrix import *
from draw import *
commands_a = ["l", "s", "t", "x", "y", "z", "g"]
commands_b = ['a', 'v', 'i']
screen = new_screen()
GREEN = [ 0, 255, 0 ]
RED = [ 255, 0, 0 ]
BLUE = [ 0, 0, 255 ]
def parse_file( fname, points, transform ):
	f = open('script_c', 'r')
	cmd = f.readline().rstrip()
	while (cmd):
		if cmd in commands_a:
			args = f.readline().rstrip()
			try:
				args = map(float, args.rsplit(" "))
			except ValueError:
				fname = args
                        m = ident(new_matrix())
                        if cmd == "g":
				draw_lines(points, screen, BLUE)
				save_ppm(screen, fname)
				save_extension(screen, fname)
			elif cmd == "l":
				add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
			elif cmd == "s":
				m = make_scale(args[0], args[1], args[2])
			elif cmd == "t":
				m = make_translate(args[0], args[1], args[2])
			elif cmd == "x":
				m = make_rotX(args[0])
			elif cmd == "y":
				m = make_rotY(args[0])
			elif cmd == "z":
				m = make_rotZ(args[0])
                        transform = matrix_mult(transform, m)
                                
		elif cmd in commands_b:
			if cmd == "i":
				transform = ident(transform)
			elif cmd == "a":
				points = matrix_mult(transform, points)
			elif cmd == "v":
				screen = new_screen()
				draw_lines(points, screen, BLUE)
				display(screen)
		cmd = f.readline().rstrip()		

points = []
transform = new_matrix()


