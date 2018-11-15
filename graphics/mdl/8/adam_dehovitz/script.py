import mdl
from display import *
from matrix import *
from draw import *
import copy, math

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 0, 255]
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
        if command[0] == "push":
            stack.append(copy.deepcopy(stack[-1]))
        elif command[0] == "pop":
            stack.pop()
        elif command[0] in ["sphere","box","torus"]:
            if command[0] == "sphere":
                add_sphere(matrix,command[1],command[2],command[3],command[4],5)
            elif command[0] == "box":
                add_box(matrix, command[1],command[2],command[3],command[4], command[5],command[6])
            elif command[0] == "line":
                add_edge(matrix, command[1],command[2],command[3],command[4], command[5],command[6])
            elif command[0] == "torus":
                add_torus(matrix, command[1],command[2],command[3],command[4], command[5],5)
            matrix_mult(stack[-1],matrix)
            draw_polygons( matrix, screen, color )
            matrix=[];
        elif command[0] == "line":
            add_edge(matrix, command[1],command[2],command[3],command[4], command[5],command[6])
            draw_lines( matrix, screen, color )
            matrix=[];
        elif command[0] in ["move","scale","rotate"]:
            if command[0] == "move":
                t= make_translate(command[1],command[2],command[3])
            elif command[0] == "scale":
                t = make_scale(command[1],command[2],command[3])
            elif command[0] == "rotate":
                r = command[2] * ( math.pi / 180.0 )
                if command[1] == "x":
                    t= make_rotX(r)
                elif command[1] == "y":
                    t = make_rotY(r)
                elif command[1] == "z":
                    t = make_rotZ(r)
            matrix_mult(stack[-1],t)
            stack[-1]=t
        elif command[0] == "display":
            display( screen )
        elif command[0] == "save":
            save_extension( screen, command[1] )
        
       
run("robot.mdl")
