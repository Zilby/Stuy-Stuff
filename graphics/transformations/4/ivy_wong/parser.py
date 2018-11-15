from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    f = open(fname, 'r')
    screen = new_screen()
    cmd = f.readline().strip("\n")
    while cmd != '':
        print "Edge: "
        print_matrix(points)
        print "Transform: "
        print_matrix(transform)
        if cmd == 'l':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            add_edge(points,args[0],args[1],args[2],args[3],args[4],args[5])
        elif cmd == 'i':
            transform = ident(points)
        elif cmd == 's':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            tmp = make_scale(args[0],args[1],args[2])
            transform = matrix_mult(transform, tmp) 
        elif cmd == 't':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            tmp = make_translate(args[0],args[1],args[2])
            transform = matrix_mult(transform, tmp)
        elif cmd == 'x':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            tmp = make_rotX(args[0])
            transform = matrix_mult(transform, tmp)
        elif cmd == 'y':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            tmp = make_rotY(args[0])
            transform = matrix_mult(transform, tmp)  
        elif cmd == 'z':
            args = f.readline().strip('\n').split(" ")
            for i, num in enumerate(args):
                args[i] = float(num)
            tmp = make_rotZ(args[0])
            transform = matrix_mult(transform, tmp)
        elif cmd == 'a':
            print "APPLYING CHANGES..." 
            print_matrix(points)
            print_matrix(transform)
            points = matrix_mult(points,transform)
            print_matrix(points)
            transform = ident(transform)
            print len(points)
        elif cmd == 'v':
            clear_screen(screen)
            color = [0, 255, 0]
            draw_lines(points, screen, color)
            display(screen)
        elif cmd == 'g':
            clear_screen(screen)
            color = [0, 255, 0]
            draw_lines(points, screen, color)
            img = f.readline().split()[0]
            save_ppm(screen,img)
        print cmd
        cmd = f.readline().strip('\n')

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
