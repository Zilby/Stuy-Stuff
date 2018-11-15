from display import *
from matrix import *
from draw import *



def parse_file( fname, points, transform ):
    screen = new_screen()
    color = [255, 255, 255]
    f = open(fname) 
    commands = [c.strip('\n') for c in f.readlines()]
    for i in range(len(commands)):
        c = commands[i]
        if c in ('l','s','t','x','y','z','c','b','h','d','m','p'):

            args = commands[i+1].split()
            for i in range(len(args)):
                if '.' in args[i]:
                    args[i] = float(args[i])
                else:
                    args[i] = int(args[i])

            if c == 'l':
                add_edge(points,*args)
                
            elif c == 'c':
                print 'adding circle'
                add_circle(points, args[0], args[1], 0, args[2], .01)
            
            elif c == 'b':
                args.append(.01)
                args.append('bezier')
                add_curve(points, *args)

            elif c == 'h':
                args.append(.01)
                args.append('hermite')
                add_curve(points, *args)

            elif c == 'm':
                add_sphere(points, *args)

            elif c == 'd':
                add_torus(points, *args)

            elif c == 'p':
                add_prism(points, *args)

            else:
                if c == 's':
                    m = make_scale(*args)
                elif c == 't':
                    m = make_translate(*args)
                elif c == 'x':
                    m = make_rotX(*args)
                elif c == 'y':
                    m = make_rotY(*args)
                elif c == 'z':
                    m = make_rotZ(*args)
                    
                transform = matrix_mult(m,transform)
                
        elif c == 'g':  
            fname = commands[i+1]
            draw_lines(points, screen, color)
            save_extension(screen, fname)

        elif c == 'i':
            transform = ident(transform)

        elif c == 'a':
            points = matrix_mult(transform, points)
            
        elif c == 'v':
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)

        elif c == 'w':
            points = []

points = []
transform = new_matrix()

parse_file('script_c', points, transform)

