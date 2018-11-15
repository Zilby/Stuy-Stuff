"""========== script.py ==========

  This is the only file you need to modify in order
  to get a working mdl project (for now).

  my_main.c will serve as the interpreter for mdl.
  When an mdl script goes through a lexer and parser, 
  the resulting operations will be in the array op[].

  Your job is to go through each entry in op and perform
  the required action from the list below:

  frames: set num_frames for animation

  basename: set name for animation

  vary: manipluate knob values between two given frames
        over a specified interval

  set: set a knob to a given value
  
  setknobs: set all knobs to a given value

  push: push a new origin matrix onto the origin stack
  
  pop: remove the top matrix on the origin stack

  move/scale/rotate: create a transformation matrix 
                     based on the provided values, then 
		     multiply the current top of the
		     origins stack by it.

  box/sphere/torus: create a solid object based on the
                    provided values. Store that in a 
		    temporary matrix, multiply it by the
		    current top of the origins stack, then
		    call draw_polygons.

  line: create a line based on the provided values. Store 
        that in a temporary matrix, multiply it by the
	current top of the origins stack, then call draw_lines.

  save: call save_extension with the provided filename

  display: view the image live
  
  jdyrlandweaver
  ========================="""

import mdl
from display import *
from matrix import *
from draw import *
import os
from sys import exit

# GLOBAL STUFF
BASENAME = "base"
DIR = "anime"

# The Epic First Pass :)
def first_pass( commands ):
    # Booleans
    found_basename = False
    found_frames = False
    found_vary = False

    # Set Default Parameters
    num_frames = 1      # Start off with one frame

    # Loop through the commands
    for c in commands:
        if c[0] == "basename":
            found_basename = True
            BASENAME = c[1]
        elif c[0] == "frames":
            found_frames = True
            num_frames = c[1]
        elif c[0] == "vary":
            found_vary = True

    # Found vary, but frames doesn't exist
    if ( not found_frames ) and found_vary:
        print "When using vary, the 'frames' command is requred."
        print "Exiting with status cude 1."
        exit(1)

    # Found frames, but not basename
    if ( not found_basename ) and found_frames:
        print "No basename found, default is '%s'." %(BASENAME)
    
    # Check if 'anime' directory exists
    # If it doesn't, make it
    if not os.path.exists(DIR):
        os.mkdir(DIR, 0755)
    
    # Return number of frames
    return num_frames

# The Even more Epic Second pass! :)
def second_pass( commands, num_frames ):
    # Create num_frame dictionaries
    knobs = [ {} for i in range(num_frames) ]

    # Loop through each command
    for c in commands:
        if c[0] == "vary":
            # Handy Values
            name = c[1]
            
            start_frame = c[2]
            end_frame = c[3]
            start_value = c[4]
            end_value = c[5]
            
            diff = (end_value - start_value) /\
                   float(end_frame - start_frame)

            # Run through each frame
            for j in range(num_frames):
                if (j < start_frame):
                    knobs[j][name] = 0
                elif (j > end_frame):
                    knobs[j][name] = 1
                else:
                    knobs[j][name] = start_value + diff * (j - start_frame)

    return knobs

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 0]
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

    # Animation STuff
    num_frames = first_pass(commands)
    knobs = second_pass(commands, num_frames)

    # Frames
    print "Total # of Frames: %03d" %(num_frames)
    
    # Modified for animation
    for f in range(num_frames):
        for command in commands:
            # --- Calculate Knob --- #
            knob = 1 # Set default knob

            # Set knob (turn / twist)
            if len(knobs) > 0:
                if command[0] in ["move", "scale"]:
                    if command[4] in knobs[f]:
                        knob = knobs[f][ command[4] ]
                elif command[0] in ["rotate"]:
                    if command[3] in knobs[f]:
                        knob = knobs[f][ command[3] ]
            # --- Calculate Knob --- #

            # Continue
            if command[0] == "pop":
                stack.pop()
                
            if not stack:
                stack = [ tmp ]

            if command[0] == "push":
                stack.append( stack[-1][:] )

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

            # Transformation Animation Domination :)
            if command[0] == "move":
                xval = command[1] * knob
                yval = command[2] * knob
                zval = command[3] * knob
                    
                t = make_translate(xval, yval, zval)
                matrix_mult( stack[-1], t )
                stack[-1] = t

            if command[0] == "scale":
                # Handle the scaling issue
                xval = ( command[1] - 1 ) * knob + 1
                yval = ( command[2] - 1 ) * knob + 1
                zval = ( command[3] - 1 ) * knob + 1

                t = make_scale(xval, yval, zval)
                matrix_mult( stack[-1], t )
                stack[-1] = t
            
            if command[0] == "rotate":
                angle = command[2] * (math.pi / 180) * knob

                if command[1] == 'x':
                    t = make_rotX( angle )
                elif command[1] == 'y':
                    t = make_rotY( angle )
                elif command[1] == 'z':
                    t = make_rotZ( angle )            
                
                matrix_mult( stack[-1], t )
                stack[-1] = t

            # Print Command for Sanity
            # print command

        # Writing out the Animation
        if (num_frames > 1):
            save_extension( screen, "%s/%s_%03d.png" %(DIR, BASENAME, f) )
            screen = new_screen()
            stack = []
            print "Frame %03d out of %03d complete!" %(f + 1, num_frames)

    # Ending
    print
    print "Research Complete."
