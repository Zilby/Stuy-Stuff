import mdl
from display import *
from matrix import *
from draw import *
import copy, math
def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    points = []

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()


    # print "----------------------------------------"
    # for symbol in symbols:
    #     print symbol
    # print "----------------------------------------"
    # for command in commands:
    #     print command
    # print "----------------------------------------"

    for command in commands:
        print command
        if command[0] == "push":
            m = copy.deepcopy(stack[-1])
            stack.append(m)

        elif command[0] == "pop":
            stack.pop()

        elif command[0] == "move":
            m = make_translate(command[1],command[2],command[3])
            matrix_mult(stack[-1],m)
            stack[-1] = m

        elif command[0] == "rotate":
            m = []
            angle = command[2] * (math.pi/180)
            if command[1] == "y":
                m = make_rotY(angle)
            elif command[1] == "x":
                m = make_rotX(angle)
            elif command[1] == "z":
                m = make_rotZ(angle)

            matrix_mult(stack[-1],m)
            stack[-1] = m

        elif command[0] == "scale":
            m = make_scale(command[1],command[2],command[3])
            matrix_mult( stack[-1], m )
            stack[-1] = m

        elif command[0] == "box":
            m = []
            add_box( m, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1],m)
            draw_polygons( m, screen, color )


        elif command[0] == "sphere":
            m = []
            add_sphere( m, command[1], command[2], command[3], command[4], 5 )
            matrix_mult(stack[-1],m)
            draw_polygons( m, screen, color )


        elif command[0] == "torus":
            m = []
            add_torus( m, command[1], command[2], command[3], command[4], command[5], 5 )
            matrix_mult(stack[-1],m)
            draw_polygons( m, screen, color )


        elif command[0] == "line":
            m = []
            add_edge( m, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1],m)
            draw_lines( m, screen, color)
            
        elif command[0] == "display":
            display(screen)
        elif command[0] == 'save':
            save_extension( screen, command[1] )
        for x in stack:
            print x

if __name__ == "__main__":
    run("stuff.mdl")


   
   
