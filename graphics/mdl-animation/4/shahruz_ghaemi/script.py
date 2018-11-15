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
    anim = False
    frames = 0
    vary = False
    knobs = []
    basename = "temp_basename"
    
    print filename
    print stack[-1]

    ##1
    for command in commands:
        cmd = command[0]
        if cmd == "frames":
			anim = True
			frames = command[1]
        elif cmd == "basename":
			basename = command[1]
        elif cmd == "vary":
			vary = True
	if (vary and not anim):
		exit()

    ##2
    for k in range (frames):
		knobs.append({})
    for command in commands:
        cmd = command[0]
        if cmd == "vary":
			n = command[1]
			first_frame = command[2]
			last_frame = command[3]
			start_value = command[4]
			end_value = command[5]
			d = (end_value - start_value) / float(last_frame - first_frame)
			for i in range (frames):
				if (i < first_frame):
					knobs[i][n] = 0
				elif (i > last_frame):
					knobs[i][n] = 1
				else: 
					knobs[i][n] = start_value + d * (i - first_frame)
    ##3
    for frame in range(frames):
        for command in commands:
            #print command
            #print stack
            cmd = command[0]
            
            if cmd == "push":
                tmp = new_matrix()
                ident(tmp)
                stack.append(tmp)
                top+=1
                
            elif cmd == "pop":
                stack.pop()
                top-=1
                
            elif cmd == "move":
                knob = 1
                if not (knobs == []) and command[4] in knobs[frame]:
                    knob = knobs[frame][command[4]]
                x = command[1] * knob
                y = command[2] * knob
                z = command[3] * knob

                tmp = make_translate( x, y, z)
                matrix_mult(stack[-1], tmp)
                stack[-1] = tmp
                
            elif cmd == "rotate":
                knob = 1
                if not (knobs == []) and command[3] in knobs[frame]:
                    knob = knobs[frame][command[3]]
                theta = command[2] * math.pi / 180
                theta *= knob
                if command[1] == "x":
                    tmp = make_rotX( theta )
                elif command[1] == "y":
                    tmp = make_rotY( theta )
                elif command [1] == "z":
                    tmp = make_rotZ( theta )
                else:
                    print "invalid/incomplete call to ROTATE"
                    matrix_mult(stack[-1], tmp)
                    stack[-1] = tmp
                    
            elif cmd == "scale":
                knob = 1
                if not (knobs == []) and command[4] in knobs[frame]:
                    knob = knobs[frame][command[4]]
                    
                x = ((command[1] - 1) * knob) + 1
                y = ((command[2] - 1) * knob) + 1
                z = ((command[3] - 1) * knob) + 1
                                
                tmp = make_scale(x,y,z)
                matrix_mult(stack[-1], tmp)
                stack[-1] = tmp
                    
            elif cmd == "box":
                add_box(polygons, command[1], command[2], command[3], command[4], command[5], command[6])
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, color)
                polygons = []
                stack[-1] = tmp
                    
            elif cmd == "sphere":
                add_sphere(polygons, command[1], command[2], command[3], command[4], step)
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, color)
                polygons = []
                stack[-1] = tmp
                    
            elif cmd == "torus":
                add_torus(polygons, command[1], command[2], command[3], command[4], command[5], step)
                matrix_mult(stack[-1], polygons)
                draw_polygons(polygons, screen, color)
                polygons=[]
                stack[-1] = tmp
                    
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
                    save_extension(screen, "img.png")
                    #else:
                #print "did not recognize the command: "+cmd
                #print "ignore if cmd = frames, basename, or vary"
        if anim:
            save_extension(screen, "anim/"+basename+"%03d"%frame+".png")
            screen = new_screen()
            tmp = new_matrix()
            stack = [ tmp ]

