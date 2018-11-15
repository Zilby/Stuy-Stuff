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
    ident( tmp )
    polygons = []
    
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
    top = 0
    step = 5
    print filename

    print stack[top]
    for command in commands:
        print command

        cmd = command[0]
        if cmd == "push":
            tmp = [row[:] for row in stack[-1]]
            stack.append(tmp)
            top+=1
            
        elif cmd == "pop":
            stack.pop()
            top-=1
            
        elif cmd == "move":
            tmp = make_translate( command[1], command[2], command[3])
            #print tmp
            matrix_mult(stack[top], tmp)
            stack[top] = tmp
            
        elif cmd == "rotate":
            theta = command[2] * math.pi / 180
            if command[1] == "x":
                tmp = make_rotX( theta )
            elif command[1] == "y":
                tmp = make_rotY( theta )
            elif command [1] == "z":
                tmp = make_rotZ( theta )
            else:
                print "invalid/incomplete call to ROTATE"
            matrix_mult(stack[top], tmp)
            stack[top] = tmp
            
        elif cmd == "scale":
            tmp = make_scale( command[1], command[2], command[3])
            matrix_mult(stack[top], tmp)
            stack[top] = tmp
            
        elif cmd == "box":
            add_box(polygons, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult(stack[top], polygons)
            draw_polygons(polygons, screen, color)
            polygons = []
            stack[top] = tmp
            
        elif cmd == "sphere":
            add_sphere(polygons, command[1], command[2], command[3], command[4], step)
            matrix_mult(stack[top], polygons)
            draw_polygons(polygons, screen, color)
            polygons = []
            stack[top] = tmp
            
        elif cmd == "torus":
            add_torus(polygons, command[1], command[2], command[3], command[4], command[5], step)
            matrix_mult(stack[top], polygons)
            draw_polygons(polygons, screen, color)
            polygons=[]
            stack[top] = tmp
            
        elif cmd == "clear":
            poly = []
            ident(tmp)
            clear_screen(screen)
        elif cmd == "display":
            display(screen)
        elif cmd == "save":
            try:
                save_extension(screen, command[1])
            except:
                save_extention(screen, "img.png")
        else:
            print "did not recognize the command: "+cmd
            #print stack[top]
