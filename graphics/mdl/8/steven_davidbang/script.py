import mdl, copy
from display import *
from matrix import *
from draw import *

#https://nibbler.stuy.edu/webgallery/html/stuygal-mdl.html

def run(filename):
    """
    This function runs an mdl script
    """
    color = [0, 120, 255]
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
    polygons = []
    points = []
    print commands
    
    for cmd in commands:
        #print (cmd[0])

        if cmd [0][0] == '#':
            pass
        
        elif cmd[0] == 'push':
            stack.append(copy.deepcopy(stack[-1]))
            
        elif cmd [0] == 'pop':
            stack.pop()
            
        elif cmd [0] == 'move':
            t = make_translate( cmd[1], cmd[2], cmd[3] )
            matrix_mult( stack[-1], t )
            stack[-1] = t
            
        elif cmd [0] == 'rotate':
            angel = cmd[2] * ( math.pi / 180 )
            if cmd[1] == 'x':
                r = make_rotX( angel )
            elif cmd[1] == 'y':
                r = make_rotY( angel )
            elif cmd[1] == 'z':
                r = make_rotZ( angel )
            matrix_mult( stack[-1], r )
            stack[-1] = r
                                
        elif cmd [0] == 'scale':
            s = make_scale( cmd[1], cmd[2], cmd[3] )
            matrix_mult( stack[-1], s )
            stack[-1] = s
            
        elif cmd [0] == 'box':
            polygons = []
            add_box( polygons, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6] )
            matrix_mult(stack[-1], polygons)
            draw_polygons( polygons, screen, color )
            
        elif cmd [0] == 'sphere':
            polygons = []
            add_sphere( polygons, cmd[1], cmd[2], cmd[3] , cmd[4], 5 )
            matrix_mult(stack[-1], polygons)
            draw_polygons( polygons, screen, color )
        elif cmd [0] == 'torus':
            polygons = []
            add_torus( polygons, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], 5 )
            matrix_mult(stack[-1], polygons)
            draw_polygons( polygons, screen, color )
        elif cmd [0] == 'line':
            points = []
            add_edge( points, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6] )
            matrix_mult(stack[-1], points)
            draw_lines( points, screen, color)
        elif cmd [0] == 'save':
            save_extension( screen, cmd[1] )
            
        elif cmd [0] == 'display':
            #screen = new_screen()
            display( screen )
        else:
            print 'Invalid command: ' + cmd

        #print(stack)
        #print("\n")

run("robot2.mdl")

    
      
