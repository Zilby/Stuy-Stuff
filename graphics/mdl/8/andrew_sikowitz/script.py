import mdl, copy
from display import *
from matrix import *
from draw import *

def run(filename):
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
        
    for command in commands:
        points = []
        print command
        cmd = command[0]
        args = command[1:]
        top = stack[-1]
        if cmd == "push":
            stack.append(copy.deepcopy(top))
        elif cmd == "pop":
            stack.pop()
        elif cmd in ["move","rotate","scale"]:
            if cmd == "move":
                x = make_translate(args[0], args[1], args[2])
            elif cmd == "rotate":
                x = get_rot(args[0],args[1]*(math.pi/180))
            elif cmd == "scale":
                x = make_scale(args[0], args[1], args[2])
            matrix_mult(top, x)
            stack[-1] = x
        elif cmd in ["box","sphere","torus"]:
            if cmd == "box":
                add_box(points, args[0], args[1], args[2], args[3], args[4], args[5])
            elif cmd == "sphere":
                add_sphere(points, args[0], args[1], args[2], args[3], 5)
            elif cmd == "torus":
                add_torus(points, args[0], args[1], args[2], args[3], args[4], 5)
            matrix_mult(top, points)
            draw_polygons(points, screen, color)
        elif cmd == "line":
            add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            matrix_mult(top, points)
            draw_lines(points, screen, color)
        elif cmd == "save":
            save_extension(screen, args[0])
        elif cmd == "display":
            display(screen)

def get_rot(arg,angle):
    if arg == 'x':
        return make_rotX(angle)
    elif arg == 'y':
        return make_rotY(angle)
    elif arg == 'z':
        return make_rotZ(angle)

run("test.mdl")
