import mdl
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

        if command[0] = "push":
            stack.append(stack[len(stack) - 1])
        elif command[0] = "pop":
            stack = stack[:len(stack) - 1]
        elif command[0] = "move":
            x = command[1]
            y = command[2]
            z = command[3]

            move = make_translate(x,y,z)

            stack[len(stack) - 1] = matrix_mult(move, stack[len(stack) - 1])

        elif command[0] = "rotate":
            theta = command[2]

            if command[1] = "x":
                rot = make_rotX(theta)
            elif command[1] = "y":
                rot = make_rotY(theta)
            elif command[1] = "z":
                rot = make_rotZ(theta)

            stack[len(stack) - 1] = matrix_mult(rot, stack[len(stack) - 1])

        elif command[0] = "scale":
            x = command[1]
            y = command[2]
            z = command[3]

            scale = make_scale(x,y,z)

            stack[len(stack) - 1] = matrix_mult(scale, stack[len(stack) - 1])

        elif command[0] = "box":
            
