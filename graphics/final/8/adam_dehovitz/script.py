
import mdl
from display import *
from matrix import *
from draw import *

basename = ""
num_frames = 1
varies = {}
has_anim= False
def first_pass( commands ):
    global basename
    global num_frames
    global varies
    global has_anim
    has_anim= False
    for command in commands:
        cmd =command[0]
        if cmd == "frames":
            print "frames"
            print command[1]
            num_frames = int(command[1])
            print num_frames
        elif cmd == "basename":
            basename = command[1]
        elif cmd == "vary":
            if command[1] in varies.keys():
                varies[command[1]].append(command[2:])
            else:
                varies[command[1]]=[command[2:]]
            has_anim = True
    if (not num_frames == 0) and basename == "":
        basename = "default"
    if has_anim and num_frames == 0:
        exit(0)
    print num_frames
    print basename


knobs = []
def second_pass( commands, num_frames ):
    global varies
    print varies
    for frame in range(0,num_frames):
        knobs.append( {} )
        startsends={}

        for knob in varies:
            for variation in varies[knob]:
                if variation[0] <= frame and variation[1] >= frame:
                    knobs[frame][knob]= (((variation[3]-variation[2])/float(variation[1] - variation[0]))* (frame-variation[0] ))+ variation[2]
                startsends[frame- variation[0]]=(variation[2])
                startsends[frame- variation[1]]=(variation[3])
    
            if knob not in knobs[frame]:
                knobs[frame][knob]= startsends[min(startsends.keys())]
        
    print knobs



def run(filename):
    global basename
    global num_frames
    global varies
    global has_anim
    """
    This function runs an mdl script
    """
    color = [100, 100, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return
        
    stack = [new_matrix()]
    ident(stack[-1])

    screen = new_screen()
    first_pass(commands)
    print num_frames
    print basename
    second_pass(commands,num_frames)
    print "STACK: " + str(stack)
    for frame in range(0,num_frames):
        for command in commands:
            if command[0] == "pop":
                stack.pop()
                if not stack:
                    stack = [ tmp ]

            if command[0] == "push":
                stack.append(stack[-1][:] )

            if command[0] == "save":
                save_extension(screen, command[1])

            if command[0] == "display":
                display(screen)

            if command[0] == "sphere":
                m = []
                add_sphere(m, command[1], command[2], command[3], command[4], 5)
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "torus":
                m = []
                add_torus(m, command[1], command[2], command[3], command[4], command[5], 5)
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "box":                
                m = []
                add_box(m, *command[1:])
                matrix_mult(stack[-1], m)
                draw_polygons( m, screen, color )

            if command[0] == "line":
                m = []
                add_edge(m, *command[1:])
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "bezier":
                m = []
                add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'bezier')
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "hermite":
                m = []
                add_curve(m, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .05, 'hermite')
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )

            if command[0] == "circle":
                m = []
                add_circle(m, command[1], command[2], command[3], command[4], .05)
                matrix_mult(stack[-1], m)
                draw_lines( m, screen, color )
            if command[0] in ["move","scale","rotate"]:
                if command[0] == "move":
                    xval = command[1]
                    yval = command[2]
                    zval = command[3]
                    if command[len(command)-1]:
                        print "knobing the move"
                        xval*=knobs[frame][command[len(command)-1]]
                        yval*=knobs[frame][command[len(command)-1]]
                        zval*=knobs[frame][command[len(command)-1]]
                    t = make_translate(xval, yval, zval)

                    

                elif command[0] == "scale":
                    xval = command[1]
                    yval = command[2]
                    zval = command[3]
                    if command[len(command)-1]:
                        xval*=knobs[frame][command[len(command)-1]]
                        yval*=knobs[frame][command[len(command)-1]]
                        zval*=knobs[frame][command[len(command)-1]]
                    t = make_scale(xval, yval, zval)
                
                elif command[0] == "rotate":
                    angle = command[2] * (math.pi / 180)
                    print angle
                    if command[len(command)-1]:
                        angle*=knobs[frame][command[len(command)-1]]
                    if command[1] == 'x':
                        t = make_rotX( angle )
                    elif command[1] == 'y':
                        t = make_rotY( angle )
                    elif command[1] == 'z':
                        t = make_rotZ( angle )
 
                matrix_mult( stack[-1], t )
                stack[-1] = t


        if has_anim:
            print "Saving frame "+ str(frame)
            save_extension(screen, "animation/"+basename+str(frame).zfill(3)+".png" )
            screen = new_screen()
            stack = [new_matrix()]
            ident(stack[-1])


