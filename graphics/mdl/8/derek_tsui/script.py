import mdl
from display import *
from matrix import *
from draw import *
import copy

def run(filename):
    """
    This function runs an mdl script
    """
    color = [240, 240, 120]
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
        print stack

        if command[0] == 'push':
            m = copy.deepcopy(stack[-1])
            stack.append(m)
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'move':
            m = make_translate(command[1],command[2],command[3])
            matrix_mult(stack[-1], m)
            stack[-1] = m

        elif command[0] == 'rotate':
            a = command[2] * (math.pi / 180)
            if command[1] == "x":
                m = make_rotX(a)
            elif command[1] == "y":
                m = make_rotY(a)
            elif command[1] == "z":
                m = make_rotZ(a)
            matrix_mult(stack[-1],m)
            stack[-1] = m

        elif command[0] == 'scale':
            m = make_scale(command[1],command[2],command[3])
            matrix_mult(m, stack[-1])
            stack[-1] = m

        elif command[0] == 'box':
            m = []
            add_box(m, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], m)
            draw_polygons(m, screen, color)
        elif command[0] == 'sphere':
            m = []
            add_sphere(m, command[1], command[2], command[3], command[4], 5)
            matrix_mult(stack[-1], m)
            draw_polygons(m, screen, color)
        elif command[0] == 'torus':
            m = []
            add_torus(m, command[1], command[2], command[3], command[4], command[5], 5)
            matrix_mult(stack[-1], m)
            draw_polygons( m, screen, color)
        elif command[0] == 'line':
            m = []
            add_edge(m, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], m)
            draw_lines(m, screen, color)
        elif command[0] == 'save':
            save_extension( screen, command[1] )
        elif command[0] == 'display':
            display(screen)

        print ""
