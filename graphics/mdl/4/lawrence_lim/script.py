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
    tmp = ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()

    for command in commands:
        if command[0] == "push":
            copy = matrix_copy(stack[-1])
            stack.append(copy)

        elif command[0] == "pop":
            stack.pop()

        elif command[0] == "move":
            dx,dy,dz = command[1],command[2],command[3]
            if command[4]:
                pass
            tmat = make_translate(dx,dy,dz)
            stack[-1] = matrix_mult(stack[-1],tmat)
            
        elif command[0] == "rotate":
            rmat = new_matrix(4,4)
            deg = command[2]
            if command[3]:
                pass
            if command[1] == "x":
                rmat = make_rotX(deg)
            elif command[1] == "y":
                rmat = make_rotY(deg)
            elif command[1] == "z":
                rmat = make_rotZ(deg)
            else:
                print "invalid rotation axis"
            stack[-1] = matrix_mult(stack[-1],rmat)


        elif command[0] == "scale":
            sx,sy,sz = command[1],command[2],command[3]
            if command[4]:
                pass
            smat = make_scale(sx,sy,sz)
            stack[-1] = matrix_mult(stack[-1],smat)
        
        elif command[0] == "box":
            polymat = []
            add_prism(polymat,
                      command[1],command[2],command[3],
                      command[4],command[5],command[6])
            #if command[7]:
            #    pass
            polymat = matrix_mult(stack[-1], polymat)
            draw_polygons(polymat, screen, color)

        elif command[0] == "sphere":
            polymat = []
            add_sphere(polymat,
                       command[1],command[2],command[3],
                       command[4],12)
            #if command[5]:
            #    pass
            polymat = matrix_mult(stack[-1], polymat)
            draw_polygons(polymat, screen, color)

        elif command[0] == "torus":
            polymat = []
            add_torus(polymat,
                      command[1],command[2],command[3],
                      command[4],command[5],12)
            #if command[6]:
            #    pass
            polymat = matrix_mult(stack[-1], polymat)
            draw_polygons(polymat, screen, color)

        elif command[0] == "line":
            linemat = []
            #if command[whatever]:
            #    pass
            add_edge(linemat,
                     command[1],command[2],command[3],
                     command[4],command[5],command[6])
            linemat = matrix_mult(stack[-1], linemat)
            draw_lines(linemat)
            

        elif command[0] == "save":
            save_ppm(screen, command[1])

        elif command[0] == "display":
            display(screen)

        else:
            print "unknown command somehow?"
