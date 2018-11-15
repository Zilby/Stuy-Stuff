import mdl, copy
from display import *
from matrix import *
from draw import *
from math import pi

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Can't Parse"
        return

    stack = [ tmp ]
    screen = new_screen()

    for command in commands:
        
        print command
        print stack
        cmd = command[0]
        args = command[1:]
        
        if cmd == "push":
            stack.append(copy.deepcopy(stack[-1]))
        elif cmd == "pop":
            stack.pop()
        elif cmd == "move":
            t = make_translate( args[0], args[1], args[2] )
            matrix_mult( stack[-1], t )
            stack[-1] = t
        elif cmd == "rotate":
            angle = args[1] * pi / 180.0
            if args[0] == 'x':
                r = make_rotX( angle )
            elif args[0] == 'y':
                r = make_rotY( angle )
            elif args[0] == 'z':
                r = make_rotZ( angle )
            matrix_mult( stack[-1], r )
            stack[-1] = r
        elif cmd == "scale":
            s = make_scale( args[0], args[1], args[2] )
            matrix_mult( stack[-1], s )
            stack[-1] = s
        elif cmd == "box":
            temp = []
            add_box( temp, args[0], args[1], args[2], args[3], args[4], args[5] )
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, color)
        elif cmd == "sphere":
            temp = []
            add_sphere( temp, args[0], args[1], args[2], args[3], 5 )
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, color)
        elif cmd == "torus":
            temp = []
            add_torus( temp, args[0], args[1], args[2], args[3], args[4], 5 )
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, color)
        elif cmd == "line":
            temp = []
            add_edge( temp, args[0], args[1], args[2], args[3], args[4], args[5] )
            matrix_mult( stack[-1], temp )
            draw_lines( temp, screen, color)
        elif cmd == "save":
            save_extension( screen, args[0] )
        elif cmd == "display":
            display( screen )
            pass

