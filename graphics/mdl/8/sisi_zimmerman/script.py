import mdl
from display import *
from matrix import *
from draw import *
import math
import copy

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
        if command[0] == "push":
            stack.append(copy.deepcopy(stack[-1]))
            #stack.append(stack[-1])
        elif command[0] == "pop":
            stack.pop()

        elif command[0] == "move":
            m = make_translate(command[1],command[2],command[3])
            matrix_mult(stack[-1],m)
            stack[-1] = m

        elif command[0] == "rotate":
            d = command[2] * (math.pi /180)
            if command[1] == "x":
                m = make_rotX(d)
            if command[1] == "y":
                m = make_rotY(d)
            if command[1] == "z":
                m = make_rotZ(d)
        
            matrix_mult(stack[-1],m)
            stack[-1] = m
                
        elif command[0] == "scale":
            m = make_scale(command[1],command[2],command[3])
            matrix_mult(stack[-1],m)
            stack[-1] = m

        elif command[0] == "box":
            temp = []
            add_box( temp, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1],temp)
            draw_polygons(temp, screen, color)

        elif command[0] == "sphere":
            temp = []
            add_sphere( temp, command[1], command[2], command[3], command[4], 5)
            matrix_mult(stack[-1],temp)
            draw_polygons(temp, screen, color)

        elif command[0] == "torus":
            temp = []
            add_torus( temp, command[1], command[2], command[3], command[4], command[5], 5)
            matrix_mult(stack[-1],temp)
            draw_polygons(temp, screen, color)

        elif command[0] == "line":
            temp = []
            add_edge( temp, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1],temp)
            draw_lines(temp, screen, color)

        elif command[0] == "save":
            save_extension(screen, command[1])

        elif command[0] == "display":
            display(screen)

        elif command[0][0] == "#":
            pass
            

run("robot.mdl")
