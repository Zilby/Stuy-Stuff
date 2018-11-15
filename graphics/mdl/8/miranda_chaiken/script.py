import mdl
import copy, math
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [0, 0, 255]
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
        cmd = command[0]
        print command
        if cmd == "push":
            new =copy.deepcopy(stack[len(stack)-1])
            #new[0][1]=44
            #print new
            #print stack[len(stack)-1]
            stack.append(new)
        elif cmd == "pop":
            stack.pop(-1)
        elif cmd in ["sphere","box","torus"]:
            if cmd == "sphere":
                add_sphere(points,command[1],command[2],command[3],command[4],5)
            elif cmd == "box":
                add_box(points, command[1],command[2],command[3],command[4], command[5],command[6])
            elif cmd == "line":
                add_edge(points, command[1],command[2],command[3],command[4], command[5],command[6])
            elif cmd == "torus":
                add_torus(points, command[1],command[2],command[3],command[4], command[5],5)
            matrix_mult(stack[-1],points)
            draw_polygons( points, screen, color )
            points=[];
        elif cmd == "line":
            add_edge(points, command[1],command[2],command[3],command[4], command[5],command[6])
            draw_lines( points, screen, color )
            points=[];
        elif cmd in ["move","scale","rotate"]:
            if cmd == "move":
                t= make_translate(command[1],command[2],command[3])
            elif cmd == "scale":
                t = make_scale(command[1],command[2],command[3])
            elif cmd == "rotate":
                rad = command[2] * ( math.pi / 180.0 )
                print rad
                print command[1]
                if command[1] == "x":
                    t= make_rotX(rad)
                elif command[1] == "y":
                    t = make_rotY(rad)
                elif command[1] == "z":
                    t = make_rotZ(rad)
            matrix_mult(stack[-1],t)
            stack[-1]=t
            print stack[-1]

        elif cmd == "display":
            display( screen )
        elif cmd == "save":
            save_extension( screen, command[1] )
        

# elif command[

#run("test.mdl")
