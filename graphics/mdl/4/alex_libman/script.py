import mdl
from display import *
from matrix import *
from draw import *
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
        operator = command[0]
        if operator == "push":
            stack.append(copy.deepcopy(stack[-1])) #deepcopy required to copy an independent matrix
        elif operator == "pop":
            stack.pop()
        elif operator == "move":
            M = make_translate(command[1], command[2], command[3])
            if command[4] != None:
                scalar_mult(M, command[4])
            matrix_mult(stack[-1], M)
            stack[-1] = M
        elif operator == "rotate":
            if command[1] == "x":
                M = make_rotX(command[2])
            elif command[1] == "y":
                M = make_rotY(command[2])
            elif command[1] == "z":
                M = make_rotZ(command[2])
            if command[3] != None:
                scalar_mult(M, command[3])
            matrix_mult(stack[-1], M)
            stack[-1] = M
        elif operator == "scale":
            M = make_scale(command[1], command[2], command[3])
            if command[4] != None:
                scalar_mult(M, command[4])
            matrix_mult(stack[-1], M)
            stack[-1] = M
        elif operator == "box":
            points = []
            add_prism(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif operator == "sphere":
            points = []
            add_sphere(points, command[1], command[2], command[3], command[4])
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif operator == "torus":
            points = []
            add_torus(points, command[1], command[2], command[3], command[4], command[5])
            matrix_mult(stack[-1], points)
            draw_polygons(points, screen, color)
        elif operator == "line":
            points = []
            add_edge(points, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1], points)
            draw_lines(points, screen, color)
        elif operator == "hermite":
            points = []
            add_curve(points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12], 0.03, "hermite")
            matrix_mult(stack[-1], points)
            draw_lines(points, screen, color)
        elif operator == "bezier":
            points = []
            add_curve(points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12], 0.03, "bezier")
            matrix_mult(stack[-1], points)
            draw_lines(points, screen, color)
        elif operator == "display":
            display(screen)
        elif operator == "save":
            save_ppm(screen, command[1])
