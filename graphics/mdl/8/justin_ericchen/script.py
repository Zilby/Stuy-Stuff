import mdl
import copy
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
        points = []
        cmd = command[0]
        arg = command[1:]
        if cmd == "push":
            stack.append(copy.deepcopy(stack[-1]))
        elif cmd == "pop":
            stack.pop()
        elif cmd in ["move", "rotate", "scale"]:
            if cmd == "move":
                matrix = make_translate(arg[0], arg[1], arg[2])
            elif cmd == "rotate":
                matrix = make_rot(arg[0], arg[1]*(math.pi/180))
            else:
                matrix = make_scale(arg[0], arg[1], arg[2])
            matrix_mult(stack[-1], matrix)
            stack[-1] = matrix
        elif cmd in ["box", "sphere", "torus"]:
            if cmd == "box":
                add_box(points, arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
            elif cmd == "sphere":
                add_sphere(points, arg[0], arg[1], arg[2], arg[3], 5)
            else:
                add_torus(points, arg[0], arg[1], arg[2], arg[3], arg[4], 5)
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif cmd == "save":
            save_extension(screen, arg[0])
        elif cmd == "display":
            display(screen)
