from display import *
from matrix import *
from draw import *


screen = new_screen()
color = [ 0, 255, 0 ]


def parse_file( fname, points, transform ):
    f = open(fname, 'r')
    file = f.readlines()
    #print file
    f.close()

    i = 0
    while (i<len(file)):
        line = file[i].strip('\n')
        if line == 'g':
            draw_lines(points, screen, color)
            save_extension(screen, file[i+1].strip('\n'))
            i += 2
        elif line == 'a':
            matrix_mult(transform, points)
            i += 1
        elif line == 'v':
            draw_lines(points, screen, color)
            display(screen)
            i += 1
        elif line == 'l':
            pts = file[i+1].strip('\n').split(" ")
            add_edge(points,
                     float(pts[0]),
                     float(pts[1]),
                     float(pts[2]),
                     float(pts[3]),
                     float(pts[4]),
                     float(pts[5]))
            i += 2
        elif line == 's':
            ps = file[i+1].strip('\n').split(" ")
            s = make_scale(float(ps[0]), float(ps[1]), float(ps[2]))
            transform = matrix_mult(s, transform)
            i += 2
        elif line == 't':
            ps = file[i+1].strip('\n').split(" ")
            t = make_translation(float(ps[0]), float(ps[1]), float(ps[2]))
            transform = matrix_mult(t, transform)
            i+=2
        elif line == 'x':
            theta = file[i+1].strip('\n')
            x = make_rotX(theta)
            transform = matrix_mult (x, transform)
            i += 2
        elif line == 'y':
            theta = file[i+1].strip('\n')
            y = make_rotY(theta)
            transform = matrix_mult (y, transform)
            i += 2
        elif line == 'z':
            theta = file[i+1].strip('\n')
            z = make_rotZ(theta)
            transform = matrix_mult(z, transform)
            i += 2
        else:
            i += 1


points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
