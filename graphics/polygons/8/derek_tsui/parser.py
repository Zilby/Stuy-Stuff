from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):

    f = open( fname )
    commands = f.readlines()
    f.close()

    screen = new_screen()
    color = [ 50, 150, 250 ]

    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()

        if cmd in 'lstxyzcbhpmd':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                print "l"
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )

            elif cmd == 'c':
                print "c"
                add_circle( points, args[0], args[1], 0, args[2], .01 )

            elif cmd == 'b':
                print "b"
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )

            elif cmd == 'h':
                print "h"
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )

            elif cmd == 's':
                print "s"
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, transform )

            elif cmd == 't':
                print "t"
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, transform )

            elif cmd == 'p':
                print "p"
                add_box(points, args[0], args[1], args[2], args[3], args[4], args[5])

            elif cmd == 'm':
                print "m"
                add_sphere(points, args[0], args[1], 0, args[2], 5)

            elif cmd == 'd':
                print "d"
                add_torus(points, args[0], args[1], 0, args[2], args[3], 5)

            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'x':
                    print "x"
                    r = make_rotX( angle )
                elif cmd == 'y':
                    print "y"
                    r = make_rotY( angle )
                elif cmd == 'z':
                    print "z"
                    r = make_rotZ( angle )
                matrix_mult( r, transform )

        elif cmd == 'i':
            print "i"
            ident( transform )

        elif cmd == 'a':
            print "a"
            matrix_mult( transform, points )

        elif cmd in 'vg':
            print "vg"
            screen = new_screen()
            draw_polygons( points, screen, color )

            if cmd == 'v':
                print "v"
                display( screen )

            elif cmd == 'g':
                print "g"
                c+= 1
                save_extension( screen, commands[c].strip() )

        elif cmd == 'w':
            print "w"
            points = []

        else:
            print 'Invalid command: ' + cmd
        c+= 1


points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
