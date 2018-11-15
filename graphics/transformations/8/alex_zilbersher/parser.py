from display import *
from matrix import *
from draw import *

def parse_file(fname, points, transform):
    data = open(fname,'r').read().splitlines()
    screen = new_screen()
    color = [0, 255,0]
    i=0;
    while (i < len(data)):
        if (data[i] == 'l'):
            p = data[i+1].split()
            add_edge(points, float(p[0]), float(p[1]), float(p[2]), float(p[3]), float(p[4]), float(p[5]))
	elif (data[i] == 'i'):
            transform = ident()
        elif (data[i] == 's'):
            p = data[i+1].split()
            transform = matrix_mult(make_scale(float(p[0]), float(p[1]), float(p[2])), transform)
        elif (data[i] == 't'):
            p = data[i+1].split()
            transform = matrix_mult(make_translate(float(p[0]), float(p[1]), float(p[2])), transform)
        elif (data[i] == 'x'):
            transform = matrix_mult(make_rotX(float(data[i+1])), transform)
        elif (data[i] == 'y'):
            transform = matrix_mult(make_rotY(float(data[i+1])), transform)
        elif (data[i] == 'z'):
            transform = matrix_mult(make_rotZ(float(data[i+1])), transform)
        elif (data[i] == 'a'):
            points = matrix_mult(transform, points)
        elif (data[i] == 'v'):
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)
        elif (data[i] == 'g'):
            draw_lines(points, screen, color)
            display(screen)
        i+=1
points = []
transform = new_matrix()
parse_file('script_c', points, transform )
