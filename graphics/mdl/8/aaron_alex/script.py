import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    base = [0,0,0]
    tmpbase = [0,0,0]
    tmp = new_matrix()
    ident(tmp)

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [tmp]
    screen = new_screen()
        
    for cmd in commands:
        
        if cmd[0] == 'push':
            stack.append(new_matrix())
            ident(stack[len(stack) - 1])
            matrix_mult(stack[len(stack) - 2], stack[len(stack) - 1])
            base = [tmpbase[0],tmpbase[1],tmpbase[2]]
        elif cmd[0] == 'pop':
            stack.pop()
        
        elif cmd[0] in ['move', 'scale', 'rotate']:
            if cmd[0] == 'move':
                mat = make_translate(cmd[1], cmd[2], cmd[3])
                tmpbase = [tmpbase[0]+cmd[1], tmpbase[1]+cmd[2], tmpbase[2]+cmd[3]]

            elif cmd[0] == 'scale':
                mat = make_translate(-base[0], -base[1], -base[2])
                matrix_mult(make_scale(cmd[1], cmd[2], cmd[3]), mat)
                matrix_mult(make_translate(base[0], base[1], base[2]), mat)
 
            elif cmd[0] == 'rotate':
                mat = make_translate(-base[0], -base[1], -base[2])

                if cmd[1] == 'x':
                    matrix_mult(make_rotX(cmd[2]), mat)
                elif cmd[1] == 'y':
                    matrix_mult(make_rotY(cmd[2]), mat)
                elif cmd[1] == 'z':
                    matrix_mult(make_rotZ(cmd[2]), mat)

                matrix_mult(make_translate(base[0], base[1], base[2]), mat)

            matrix_mult(mat, stack[len(stack) - 1])

        elif cmd[0] in ['box', 'sphere', 'torus', 'line']:
            points = []
            cmds = cmd[:1]
            if cmd[0] == 'box':
                add_box(points, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
            if cmd[0] == 'sphere':
                add_sphere(points, cmd[1], cmd[2], cmd[3], cmd[4])
            if cmd[0] == 'torus':
                add_torus(points, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
            matrix_mult(stack[len(stack) - 1], points)
            draw_polygons(points, screen, color)

        elif cmd[0] == 'line':
            points = []
            add_edge(points, cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
            matrix_mult(stack[len(stack) - 1], points)
            draw_lines(points, screen, color)
            
        elif cmd[0] == 'save':
            fname = cmd[1]
            save_extension(screen, fname)

        elif cmd[0] == 'display':
            display(screen)
            
