import mdl
from display import *
from matrix import *
from draw import *
import copy

color = [255, 255, 255]
tmp = new_matrix()
ident( tmp )
stack = [ tmp ]
screen = new_screen()

def run(filename):
    """
    This function runs an mdl script
    """

    p = mdl.parseFile(filename)
    
    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    for command in commands:
        cmd = command[0]
        if cmd == "push":
            stack.append(copy.deepcopy(stack[len(stack)-1]))
        if cmd == "pop":
            stack.pop()
        if cmd == "move":
            mult(make_translate(command[1], command[2], command[3]))
        if cmd == "rotate":
            t = command[2]*math.pi/180
            axis = command[1]
            if axis == 'x':
                mult(make_rotX(t))
            if axis == 'y':
                mult(make_rotY(t))
            if axis == 'z':
                mult(make_rotZ(t))
        if cmd == "scale":
            mult(make_scale(command[1], command[2], command[3]))
        if cmd in ["box", "sphere", "torus"]:
            polygons = []
            if cmd == "box":
                add_box(polygons, command[1],command[2],command[3],command[4],command[5],command[6])
            if cmd == "sphere":
                add_sphere(polygons, command[1],command[2],command[3],command[4],5)
            if cmd == "torus":
                add_torus(polygons, command[1],command[2],command[3],command[4],command[5],5)
            matrix_mult(stack[len(stack)-1], polygons)
            draw_polygons(polygons, screen, color)
        if cmd == "line":
            points = []
            add_edge(points, command[1],command[2],command[3],command[4],command[5],command[6])
            matrix_mult(stack[len(stack)-1], points)
            draw_lines(polygons, screen, color)
        if cmd == "save":
            save_extension(screen, cmd[1])
        if cmd == "display":
            display(screen)
        
def mult(m):
    matrix_mult(stack[len(stack)-1], m)
    stack[len(stack)-1] = m
    
run("script.mdl")
