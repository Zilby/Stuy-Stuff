from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    data = open(fname, 'r')
    data = data.read()
    data = data.splitlines()
    screen = new_screen()
    color = [0, 0, 255]
    for x in data:
        if (data[x] == 'l'):
            p = data[i+1].split()
            add_edge(points, float(p[0]), float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[5]))
	elif (data[x] == 'i'):
            transform = ident()
        elif (data[x] == 's'):
            p = data[x+1].split()
            transform = matrix_mult(make_scale(float(p[0]), float(p[1]), float(p2[0])), transform)
        elif (data[x] == 't'):
            p = data[x+1].split()
            transform = matrix_mult(make_translate(float(p[0]), float(p[1]), float(p[2])), transform)
        elif (data[x] == 'x'):
            transform = matrix_mult(make_rotX(float(data[x+1])), transform)
        elif (data[x] == 'y'):
            transform = matrix_mult(make_rotY(float(data[x+1])), transform)
        elif (data[x] == 'z'):
            transform = matrix_mult(make_rotZ(float(data[x+1])), transform)
        elif (data[x] == 'a'):
            points = matrix_mult(transform, points)
        elif (data[x] == 'v'):
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)
        elif (data[x] == 'g'):
            draw_lines(points, screen, color)
            display(screen)
        else:


points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
