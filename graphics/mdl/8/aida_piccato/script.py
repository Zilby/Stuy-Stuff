import mdl, copy
from display import *
from matrix import *
from draw import *

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
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
    for command in commands:
        print command
        matrix = []
        cmd = command[0]
        args = command[1:]
        if cmd == "push":
            stack.append(copy.deepcopy(stack[-1]))
        elif cmd == "pop":
            stack.pop()
        elif cmd == "move":
            t = make_translate(args[0], args[1], args[2])
            matrix_mult(stack[-1], t)
            stack[-1] = t
        elif cmd == "rotate":
            angle = args[1] * ( math.pi / 180)
            if args[0] == 'x':
                r = make_rotX( angle )
            elif args[0] == 'y':
                r = make_rotY( angle )
            elif args[0] == 'z':
                r = make_rotZ( angle )
            matrix_mult(stack[-1],r)
            stack[-1] = r
        elif cmd == "scale":
            s = make_scale( args[0], args[1], args[2] )
            matrix_mult(stack[-1],s)
            stack[-1] = s
            
        elif cmd == "box":
            add_box(matrix, args[0], args[1], args[2], args[3], args[4], args[5])
            matrix = matrix_mult(stack[-1],matrix)
            draw_polygons(matrix, screen, color)
        
        elif cmd == "sphere":
            add_sphere(matrix, args[0], args[1], args[2], args[3], 5)
            matrix_mult(stack[-1],matrix)
            draw_polygons(matrix, screen, color)
        
        elif cmd == "torus":
            add_torus(matrix, args[0], args[1], args[2], args[3], args[4], 5)
            matrix_mult(stack[-1],matrix)
            draw_polygons(matrix, screen, color)
        
        
        elif cmd == "line":
            add_edge(matrix, args[0], args[1], args[2], args[3], args[4], args[5])
            draw_lines(matrix, screen, color)
            
        elif cmd == "display":
            display(screen)
        elif cmd == "save":
            save_extension(screen, args[0])
        elif cmd == "#":
            pass
run("munchkins.mdl")
