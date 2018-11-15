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
        if c in ('l','s','t','x','y','z','c','b','h'):

            args = commands[i+1].split()
            for i in range(len(args)):
                if '.' in args[i]:
                    args[i] = float(args[i])
                else:
                    args[i] = int(args[i])

            if c[0] == 'l':
                add_edge(points,*args)
                
            elif c[0] == 'c':
                print 'adding circle'
                add_circle( points, args[0], args[1], 0, args[2], .01 )
            
            elif c[0] == 'b':
                args.append(.01)
                args.append('bezier')
                add_curve( points, *args)

            elif c[0] == 'h':
                args.append(.01)
                args.append('hermite')
                add_curve( points, *args)

            else:
                if c[0] == 's':
                    m = make_scale(*args)
                elif c[0] == 't':
                    m = make_translate(*args)
                elif c[0] == 'x':
                    m = make_rotX(*args)
                elif c[0] == 'y':
                    m = make_rotY(*args)
                elif c[0] == 'z':
                    m = make_rotZ(*args)
                
                transform = matrix_mult(m,transform)
                
        elif c[0] == 'g':  
            fname = commands[i+1]
            draw_lines(points, screen, color)
            save_extension(screen, fname)

        elif c[0] == 'i':
            transform = ident(transform)

        elif c[0] == 'a':
            points = matrix_mult(transform, points)
            
        elif c[0] == 'v':
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)


points = []
transform = new_matrix()

parse_file('script_c', points, transform)

