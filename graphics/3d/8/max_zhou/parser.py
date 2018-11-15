import writer
from matrix import *
from param import *
from line import *

def parse( fname, oname, xres, yres):
    global pt_matrix
    global master
    global identity
    print pt_matrix
    f = open( fname )
    commands = f.readlines()
    f.close()
    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()

        if cmd in 'lstxyzcbh':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                add_edge( pt_matrix, args[0], args[1], args[3], args[4], z1=args[2],z2=args[5] )

            elif cmd == 'c':
                add_circle(args[0], args[1], args[2], pt_matrix )

            elif cmd == 'b':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'BEZIER' )

            elif cmd == 'h':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'HERMITE' )

            elif cmd == 's':
                s = scale( args[0], args[1], args[2] )
                m_mult(master, s )

            elif cmd == 't':
                t = translate( args[0], args[1], args[2] )
                m_mult(master, t)

            else:
                angle = args[0]
                if cmd == 'x':
                    r = rot_x( angle )
                elif cmd == 'y':
                    r = rot_y( angle )
                elif cmd == 'z':
                    r = rot_z( angle )
                m_mult(master, r )

        elif cmd == 'i':
            master = identity

        elif cmd == 'a':
            #m_mult( transform, points )
            pt_matrix = apply_transformations()

        elif cmd in 'vg':
            print 'When finished, files are automatically saved to the desired directory in command-line args.  Sorry, no viewing.'
            return pt_matrix
        else:
            print 'Invalid command: ' + cmd
        c+= 1


