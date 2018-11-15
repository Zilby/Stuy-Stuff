from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    screen = new_screen()
    color = [255, 255, 0]

    f = open(fname, 'r')
    fs = []
    for line in f.readlines():
        fs.append(line[:-1])

    i = 0
    while i < len(fs):
        if (fs[i] == "l"):
            ps = fs[i+1].split(" ")
            add_edge(points, float(ps[0]), float(ps[1]), float(ps[2]), float(ps[3]), float(ps[4]),float(ps[5]))
        elif (fs[i] == "i"):
            transform = ident()
        elif (fs[i] == "s"):
            ps = fs[i+1].split()
            transform = matrix_mult(make_scale(float(ps[0]), float(ps[1]), float(ps[2])), transform)
        elif (fs[i] == "t"):
            ps = fs[i+1].split()
            transform = matrix_mult(make_translate(float(ps[0]), float(ps[1]), float(ps[2])), transform)
        elif (fs[i] == "x"):
            transform = matrix_mult(make_rotX(float(fs[i+1])), transform)
        elif (fs[i] == "y"):
            transform = matrix_mult(make_rotY(float(fs[i+1])), transform)
        elif (fs[i] == "z"):
            transform = matrix_mult(make_rotZ(float(fs[i+1])), transform)
        elif (fs[i] == "a"):
            points = matrix_mult(transform, points)
        elif (fs[i] == "v"):
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)
        elif (fs[i] == "g"):
            print str(i) + fs[i]
            draw_lines(points, screen, color)
            display(screen)
        i=i+1

points = []
transform = new_matrix()
#parse_file( 'script_c', points, transform )
parse_file( 'script2', points, transform )
