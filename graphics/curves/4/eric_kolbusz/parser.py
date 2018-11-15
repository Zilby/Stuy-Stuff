from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    screen = new_screen()
    color = [255,255,255]
    f = open(fname, 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        if line == 'a':
            points = matrix_mult(transform, points)
        elif line == 'i':
            ident(transform)
        elif line == 'v':
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)
        elif line in list('lstxyzcbhg'):
            args = lines[i+1].strip().split(' ')
            if line == 'l':
                try:
                    args = [int(a) for a in args]
                    add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
                except:
                    print "Invalid args for operation l, exiting"
                    exit(1)
            if line == 's':
                try:
                    args = [float(a) for a in args]
                    m = make_scale(args[0], args[1], args[2])
                except:
                    print "Invald args for operation s, exiting"
                    exit(1)
                transform = matrix_mult(m, transform)
            if line == 't':
                try:
                    args = [int(a) for a in args]
                    m = make_translate(args[0], args[1], args[2])
                except:
                    print "Invald args for operation t, exiting"
                    exit(1)   
                transform = matrix_mult(m, transform)
            if line == 'x':
                try:
                    args = [int(a) for a in args]
                    m = make_rotX(args[0])
                except:
                    print "Invald args for operation x, exiting"
                    exit(1)   
                transform = matrix_mult(m, transform)
            if line == 'y':
                try:
                    args = [int(a) for a in args]
                    m = make_rotY(args[0])
                except:
                    print "Invald args for operation y, exiting"
                    exit(1)   
                transform = matrix_mult(m, transform)
            if line == 'z':
                try:
                    args = [int(a) for a in args]
                    m = make_rotZ(args[0])
                except:
                    print "Invald args for operation z, exiting"
                    exit(1)   
                transform = matrix_mult(m, transform)
            if line == 'c':
                try:
                    args = [int(a) for a in args]
                    add_circle(points, args[0], args[1], 0, args[2], .001)
                except:
                    print "Invald args for operation c, exiting"
                    exit(1)
            if line in list('bh'):
                try:
                    args = [int(a) for a in args]
                    add_curve(points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .001, line)
                except:
                    print "Invald args for operation %s, exiting"%(line)
                    exit(1)
            if line == 'g':
                draw_lines(points, screen, color)
                #save_ppm(screen, args[0])
                save_extension(screen, args[0])
            
                 


points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )


