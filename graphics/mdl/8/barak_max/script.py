import mdl
import math
import copy
from display import *
from matrix import *
from draw import *

STEP = 3

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    points = []
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
        
        if command[0] == 'push':
            stack.append(copy.deepcopy(stack[len(stack)-1]))

        elif command[0] == 'pop':
            stack.pop()

        elif command[0] in ['move', 'rotate', 'scale']:

            if command[0] == 'move':
                t = make_translate(command[1],command[2],command[3])

            elif command[0] == 'rotate':
                theta = command[2] * math.pi / 180.0
                if command[1] == 'x':
                    t = make_rotX(theta)
                elif command[1] == 'y':
                    t = make_rotY(theta)
                elif command[1] == 'z':
                    t = make_rotZ(theta)

            elif command[0] == 'scale':
                t = make_scale(command[1],command[2],command[3])

            matrix_mult(stack[-1],t)
            stack[-1] = t

        elif command[0] in ['sphere', 'box', 'torus']:

            if command[0] == 'sphere':
                add_sphere(points,command[1],command[2],command[3],command[4],STEP)

            elif command[0] == 'box':
                add_box(points,command[1],command[2],command[3],command[4],command[5],command[6])

            elif command[0] == 'torus':
                add_torus(points,command[1],command[2],command[3],command[4],command[5],STEP)

            matrix_mult(stack[-1],points)
            draw_polygons(points,screen,color)
            points=[]

        elif command[0] == 'line':
            add_edge(points,command[1],command[2],command[3],command[4],command[5],command[6])
            draw_lines(points,screen,color)
            points=[]

        elif command[0] == 'save':
            save_extension(screen, command[1])

        elif command[0] == 'display':
            display(screen)
