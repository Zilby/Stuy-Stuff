import mdl, copy
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
    #I made matrix_mult return m2, which is helpful 
    
    print" here "

    for command in commands:
    #Andreas is doing these 
        if command[0] == 'push':
            stack.append(copy.deepcopy(stack[-1]))
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'move':
            tmp = make_translate(command[1],command[2], command[3])
            stack[-1] = matrix_mult(stack[-1],tmp)
        elif command[0] == 'rotate':
            if command[1] == "x":
                stack[-1] = matrix_mult(stack[-1], make_rotX(command[2]))
            elif command[1] =="y":
                stack[-1] = matrix_mult(stack[-1], make_rotY(command[2]))
            elif command[1] =="z":
                stack[-1] = matrix_mult(stack[-1], make_rotZ(command[2]))
        elif command[0] == 'scale':
                stack[-1] = matrix_mult(stack[-1],make_scale(command[1],command[2], command[3]))
        elif command[0] == 'box':
                tmp =[]
                add_box(tmp, command[1], command[2], command[3], command[4],command[5], command[6])
                matrix_mult(stack[-1], tmp)
                draw_polygons(tmp, screen, color)
                
    
    #cooper you do these 
        elif command[0] == 'torus':
                tmp = []
                step = command[6]
                if not step:
                    step = 5
                add_torus(tmp, command[1],command[2], command[3], command[4],command[5], step)
                matrix_mult(stack[-1], tmp)
                draw_polygons(tmp, screen, color)
        elif command[0] == 'sphere':
                tmp = []
                step = command[5]
                if not step:
                    step = 5
                add_sphere(tmp, command[1],command[2], command[3], command[4], step )
                matrix_mult(stack[-1], tmp)
                draw_polygons(tmp, screen, color)
        elif command[0] == 'line':
                tmp = []
                add_edge( tmp, command[1], command[2], command[3], command[4], command[5], command[6])
                matrix_mult(stack[-1],temp)
                draw_lines(temp, screen, color)
        elif command[0] == 'save':
                fname = command[1]
                save_extension(screen, fname)
        elif command[0] == 'display':
                display(screen)
        print command

run("robot.mdl")
