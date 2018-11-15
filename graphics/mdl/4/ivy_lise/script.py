import mdl
from display import *
from matrix import *
from draw import *
STEP_SIZE = 5

def run(filename):
    color = [255, 55, 255]
    tmp = new_matrix()
    ident( tmp )
    poly = [] #polygon matrix
    
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p  #symbols is something....
    else:
        print "Parsing failed."
        return
    stack = [ tmp ] #LIFO
    screen = new_screen()
    for command in commands:
        print command
   
        cmd = command[0]
        if cmd == "display":
            display(screen)

        elif cmd == "save":
            try:
                save_extension( screen, command[1] )
            except:
                print "no picture name given - defaulting to image.png as name"
                save_extension(screen, "image.png")
        elif cmd == "line":
            pass
        
        elif cmd == "push":
            m = [row[:] for row in stack[-1]]
            stack.append(m)

        elif cmd == "pop":
            stack.pop() #removes the last element of stack (last in)
        
        elif cmd == "move":
            m = make_translate(command[1],command[2],command[3])
            matrix_mult(stack[-1],m)
            stack[-1] = m
        
        elif cmd == "rotate":
            angle = command[2] * ( math.pi / 180.0 )
            if command[1] == "x":
                m = make_rotX(angle)
            elif command[1] == "y":
                m = make_rotY(angle)
            else:
                m = make_rotZ(angle)
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
            add_sphere(poly, command[1], command[2],command[3], command[4], STEP_SIZE)
            matrix_mult(stack[-1],poly)
            draw_polygons(poly, screen, color)
            poly=[]
        
        elif cmd == "torus":
            add_torus(poly, command[1], command[2],command[3], command[4], command[5], STEP_SIZE)
            matrix_mult(stack[-1],poly)
            draw_polygons(poly, screen, color)
            poly=[]
        
        elif cmd == "clear":
            poly = []
            ident(tmp)

        elif cmd == "quit":
            return


