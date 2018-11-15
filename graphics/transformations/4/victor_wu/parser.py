from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    f = open(fname, 'r')
    do = f.read()
    command = do.split('\n')
    screen = new_screen()
    for i in range(len(command)):
        if command[i] == 'l':
            coord = command[i+1].split(' ')
            if len(coord) != 6:
                print "Incorrect parameters"
            else:
                for i in range(len(coord)):
                    coord[i] = int(coord[i])
                add_edge(points, coord[0], coord[1], coord[2], coord[3], coord[4], coord[5])
            i = i + 1
        elif command[i] == 'i':
            transform = ident(transform)
        elif command[i] == 's':
            scale = command[i+1].split(' ')
            if len(scale) != 3:
                print "Incorrect parameters"
            else:
                for i in range(len(scale)):
                    scale[i] = float(scale[i])
                transform = matrix_mult(transform, make_scale(scale[0], scale[1], scale[2]))
            i = i + 1
        elif command[i] == 't':
            trans = command[i+1].split(' ')
            if len(trans) != 3:
                print "Incorrect parameters"
            else:
                for i in range(len(trans)):
                    trans[i] = int(trans[i])
                transform = matrix_mult(transform, make_translate(trasn[0], trans[1], trans[2]))
            i = i + 1
        elif command[i] == 'x':
            theta = command[i+1].split(' ')
            if len(theta) != 1:
                print "Incorrect parameters"
            else:
                theta = int(theta)
                transform = matrix_mult(transform, make_rotX(theta))
            i = i+1
        elif command[i] == 'y':
            theta = command[i+1].split(' ')
            if len(theta) != 1:
                print "Incorrect parameters"
            else:
                theta = int(theta)
                transform = matrix_mult(transform, make_rotY(theta))
            i = i + 1
        elif command[i] == 'z':
            theta = command[i+1].split(' ')
            if len(theta) != 1:
                print "Incorrect parameters"
            else:
                theta = int(theta)
                transform = matrix_mult(transform, make_rotZ(theta))
            i = i + 1
        elif command[i] == 'a':
            points = matrix_mult(transform, points)
        elif command[i] == 'v':
            clear_screen(screen)
            draw_lines(points, screen, [255, 255, 255])
            display(screen)
        elif command[i] == 'g':
            name = command[i+1].split(' ')
            clear_screen(screen)
            draw_lines(points, screen, [255, 255, 255])
            display(screen)
            save_ppm(screen, name)
            i = i + 1
                    

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
