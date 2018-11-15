import mdl
from display import *
from matrix import *
from draw import *
import copy
import sys

def first_pass(commands):
    pass

def second_pass(commands):
    pass
            
def run(filename):
    """
    This function runs an mdl script
    """
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    num_frames = 1
    animation_frames = []
    basename = "img%03d"
    color = [255, 255, 255]

    #first pass
    for command in commands:
        operator = command[0]
        if operator == "frames":
            num_frames = command[1]
        elif operator == "basename":
            basename = command[1] + "%03d"
    if basename == "img%03d":
        print "No animation basename specified, using 'img*'"

    #second pass
    for command in commands:
        operator = command[0]
        for i in range(num_frames):
            animation_frames.append({})
        if operator == "vary":
            if num_frames <= 1:
                print "Frames not set, but vary used"
                sys.exit()
            if command[1] not in animation_frames[0]:
                for i in range(num_frames):
                    animation_frames[i][command[1]] = 0
            start = command[2]
            end = command[3]
            startVal = command[4]
            endVal = command[5]
            for i in range(start, end + 1):
                animation_frames[i][command[1]] = startVal + 1. * (endVal - startVal) / (end - start) * (i - start)
    
    #third pass
    for i in range(num_frames):
        stack = [ tmp ]
        screen = new_screen()
        for command in commands:
            #print command
            operator = command[0]
            if operator == "push":
                stack.append(copy.deepcopy(stack[-1])) #deepcopy required to copy an independent matrix
            elif operator == "pop":
                stack.pop()
            elif operator == "move":
                v = 1
                if command[4] != None:
                    v = animation_frames[i][command[4]]
                M = make_translate(command[1] * v, command[2] * v, command[3] * v)
                matrix_mult(stack[-1], M)
                stack[-1] = M
            elif operator == "rotate":
                v = 1
                if command[3] != None:
                    v = animation_frames[i][command[3]]
                if command[1] == "x":
                    M = make_rotX(command[2] * v)
                elif command[1] == "y":
                    M = make_rotY(command[2] * v)
                elif command[1] == "z":
                    M = make_rotZ(command[2] * v)
                matrix_mult(stack[-1], M)
                stack[-1] = M
            elif operator == "scale":
                v = 1
                if command[4] != None:
                    v = animation_frames[i][command[4]]
                M = make_scale(command[1] * v, command[2] * v, command[3] * v)
                matrix_mult(stack[-1], M)
                stack[-1] = M
            elif operator == "box":
                points = []
                add_prism(points, command[1], command[2], command[3], command[4], command[5], command[6])
                matrix_mult(stack[-1], points)
                draw_polygons(points, screen, color)
            elif operator == "sphere":
                points = []
                add_sphere(points, command[1], command[2], command[3], command[4])
                matrix_mult(stack[-1], points)
                draw_polygons(points, screen, color)
            elif operator == "torus":
                points = []
                add_torus(points, command[1], command[2], command[3], command[4], command[5])
                matrix_mult(stack[-1], points)
                draw_polygons(points, screen, color)
            elif operator == "line":
                points = []
                add_edge(points, command[1], command[2], command[3], command[4], command[5], command[6])
                matrix_mult(stack[-1], points)
                draw_lines(points, screen, color)
            elif operator == "hermite":
                points = []
                add_curve(points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12], 0.03, "hermite")
                matrix_mult(stack[-1], points)
                draw_lines(points, screen, color)
            elif operator == "bezier":
                points = []
                add_curve(points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], command[9], command[10], command[11], command[12], 0.03, "bezier")
                matrix_mult(stack[-1], points)
                draw_lines(points, screen, color)
            elif operator == "display":
                display(screen)
            elif operator == "save":
                save_ppm(screen, command[1])
        save_ppm(screen, ("animations/" + basename + ".ppm")%i)
