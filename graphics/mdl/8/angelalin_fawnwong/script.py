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
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ] #initializes origin stack with identity matrix pushed on
    screen = new_screen()
        
    for command in commands:
        if command[0] == 'push':
            push(stack)
        elif command[0] == 'pop':
            pop(stack)
        elif command[0] == 'move':
            stack[-1] = move(stack[-1], command[1], command[2], command[3])
        elif command[0] == 'rotate':
            stack[-1] = rotate(stack[-1], command[1], command[2])
        elif command[0] == 'scale':
            stack[-1] = scale(stack[-1], command[1], command[2], command[3])
        elif command[0] == 'box':
            box(stack[-1], command[1], command[2], command[3], command[4], command[5], command[6], screen, color)
        elif command[0] == 'torus':
            torus(stack[-1], command[1], command[2], command[3], command[4], screen, color)
        elif command[0] == 'sphere':
            sphere(stack[-1], command[1], command[2], command[3], command[4], screen, color)
        elif command[0] == 'line':
            line(stack[-1], command[1], command[2], command[3], command[4], command[5], command[6], screen, color)
        elif command[0] == 'save':
            save_extension(screen, command[1])
        elif command[0] == 'display':
            display(screen)
        else:
            pass
        #print command

#push: push a copy of the current top of the origins stack onto the origins stack (a full copy, not just a reference to the current top)
def push(stack):
    current = stack[-1]
    stack.append(current)

#pop: removes the top of the origins stack (nothing needs to be done with this data)
def pop(stack):
    stack.pop()

#move/rotate/scale: create a translation/rotation/scale matrix and multiply the current top by it
def move(stack, x, y, z):
    t = make_translate(x, y, z)
    matrix_mult(stack, t)
    return t

def rotate(stack, axis, theta):
    angle = theta * (math.pi/180)
    if axis == 'x':
        x = make_rotX(angle)
        matrix_mult(stack, x)
        return x
    elif axis == 'y':
        y = make_rotY(angle)
        matrix_mult(stack, y)
        return y
    elif axis == 'z':
        z = make_rotZ(angle)
        matrix_mult(stack, z)
        return z
    
def scale(stack, x, y, z):
    s = make_scale(x, y, z)
    matrix_mult(stack, s)
    return s

#box/sphere/torus: add a box/sphere/torus to a temporary polygon matrix, multiply it by the current top and draw it to the screen
def box(stack, x, y, z, width, height, depth, screen, color):
    temp = []
    add_box(temp, x, y, z, width, height, depth)
    matrix_mult(stack, temp)
    draw_polygons(temp, screen, color)
    
def torus(stack, x, y, rad1, rad2, screen, color):
    temp = []
    add_torus(temp, x, y, 0, rad1, rad2, 5)
    matrix_mult(stack, temp)
    draw_polygons(temp, screen, color)

def sphere(stack, x, y, z, r, screen, color):
    temp = []
    add_sphere(temp, x, y, z, r, 5)
    matrix_mult(stack, temp)
    draw_polygons(temp, screen, color)

#line: add a line to a temporary edge matrix, multiply it by the current top and draw it to the screen (note a line is not a solid, so avoid draw_polygons)
def line(stack, x1, y1, z1, x2, y2, z2, screen, color):
    temp = []
    add_edge(temp, x1, y1, z1, x2, y2, z2)
    matrix_mult(stack, temp)
    draw_line(screen, x1, y1, x2, y2, color)

run("pic.mdl")
