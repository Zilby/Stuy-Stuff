import mdl
from display import *
from matrix import *
from draw import *

step = 2

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    points = []
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

#############################

    poly = []
    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        #print command
        cmd = command[0]


        if cmd == "display":
            display(screen)

        elif cmd == "push":
            m = [row[:] for row in stack[-1]]
            stack.append(m)

        elif cmd == "pop":
            stack.pop() 
        
        elif cmd == "move":
            m = make_translate(command[1], command[2], command[3])
            matrix_mult (stack[-1],m)
            stack [-1] = m
        
        elif cmd == "rotate":
            theta = command[2] * ( math.pi / 180.0 )
            if command [1] == "x":
                m = make_rotX (theta)
            elif command [1] == "y":
                m = make_rotY (theta)
            else:
                m = make_rotZ (theta)

            matrix_mult(stack[-1], m)
            stack[-1] = m
            
        elif cmd == "scale":
            m = make_scale(command[1], command[2], command[3])
            matrix_mult(stack[-1], m)
            stack[-1] = m 
        
        elif cmd == "box":
            add_box(poly, command[1], command[2],command[3], command[4], command[5], command[6])
            matrix_mult(stack[-1],poly)
            draw_polygons(poly, screen, color)
            poly=[]
        
        elif cmd == "sphere":
            add_sphere(poly, command[1], command[2],command[3], command[4], step)
            #add_sphere(poly, command[1], command[2],command[3], command[4], command[5])
            matrix_mult(stack[-1],poly)
            draw_polygons(poly, screen, color)
            poly=[]
        
        elif cmd == "torus":
            add_torus(poly, command[1], command[2],command[3], command[4], command[5], step)
            #add_torus(poly, command[1], command[2],command[3], command[4], command[5], command[6])

            matrix_mult(stack[-1],poly)
            draw_polygons(poly, screen, color)
            poly=[]
        
        elif cmd == "line":
            add_edge( points, command[1], command[2], command[3], command[4], command[5], command[6] )
            draw_lines( points, screen, color )
            points = [] 

        elif cmd == "save":
            try:
                save_extension( screen, command[1] )
            except:#no name
                save_extension(screen, "image.png")

        elif cmd == "clear":
            poly = []
            ident(tmp)

        elif cmd == "quit":
            return
