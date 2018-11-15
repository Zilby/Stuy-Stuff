import copy
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
    shapes = []
        
    for command in commands:
        if command[0] == "push":
            stack.append(copy.deepcopy(stack[-1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "move":
            t = make_translate(command[1], command[2], command[3])
            matrix_mult(stack[-1], t)
            stack[-1] = t
        elif command[0] == "scale":
            s = make_scale(command[1], command[2], command[3])
            matrix_mult(stack[-1], s)
            stack[-1] = s
        elif command[0] == "rotate":
            if command[1] == "x":
                r = make_rotX(math.radians(command[2]))
                matrix_mult(stack[-1], r)
                stack[-1] = r
            elif command[1] == "y":
                r = make_rotY(math.radians(command[2]))
                matrix_mult(stack[-1], r)
                stack[-1] = r
            elif command[1] == "z":
                r = make_rotZ(math.radians(command[2]))
                matrix_mult(stack[-1], r)
                stack[-1] = r
        elif command[0] == "sphere":
            add_sphere(shapes, command[1], command[2], command[3], command[4], 5)
            matrix_mult(stack[-1], shapes)
            draw_polygons(shapes, screen, color)
        elif command[0] == "torus":
            add_torus(shapes, command[1], command[2], command[3], command[4], command[5],  5)
            matrix_mult(stack[-1], shapes)
            draw_polygons(shapes, screen, color)
        elif command[0] == "box":
            add_box(shapes, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], shapes)
            draw_polygons(shapes, screen, color)
        elif command[0] == "line":
            add_edge(shapes, command[1], command[2], command[3], command[4], command[5], command[6])
            draw_lines(shapes, screen, color)
        elif command[0] == "save":
            save_extension(screen, command[1])
        elif command[0] == "display":
            display(screen)
        
run("robot.mdl")
