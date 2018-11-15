from display import *
from matrix import *
from draw import *
import random

color = [ random.randint(0,255), random.randint(0,255), random.randint(0,255) ]
def parse_file( fname, points, transform ):
    
    f = open( fname )
    commands = f.readlines()
    f.close()
    
    screen = new_screen()
    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()
        if cmd in 'lstxyzcbh':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                
            elif cmd == 'c':
                add_circle( points, args[0], args[1], 0, args[2], .01 )
            
            elif cmd == 'b':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'bezier' )

            elif cmd == 'h':
                add_curve( points, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], .01, 'hermite' )

            elif cmd == 's':
                s = make_scale( args[0], args[1], args[2] )
                matrix_mult( s, transform )

            elif cmd == 't':
                t = make_translate( args[0], args[1], args[2] )
                matrix_mult( t, transform )

            else:
                angle = args[0] * ( math.pi / 180 )
                if cmd == 'x':
                    r = make_rotX( angle )
                elif cmd == 'y':
                    r = make_rotY( angle )
                elif cmd == 'z':
                    r = make_rotZ( angle )
                matrix_mult( r, transform )

        elif cmd == 'i':
            ident( transform )
            
        elif cmd == 'a':
            matrix_mult( transform, points )

        elif cmd in 'vg':
            screen = new_screen()
            draw_lines( points, screen, color )
            
            if cmd == 'v':
                display( screen )

            elif cmd == 'g':
                c+= 1
                save_extension( screen, commands[c].strip() )
        else:
            print 'Invalid command: ' + cmd
        c+= 1

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )

###########################################
points = []
transform = new_matrix()
retStr = ""
#for i in range(25):
#    retStr += "c\n250 250 " + str(i*25) + "\n"

for i in range(50):
    r1 = random.randint(0, 250)
    r2 = random.randint(0, 250)
    r3 = random.randint(250, 500)
    r4 = random.randint(250, 500)
    retStr += "b\n250 0 " + str(r1) + " " + str(r2) + " " + str(r3) + " " + str(r4) + " 250 500\n"
   
for i in range(50):
    r1 = random.randint(0, 500)
    r2 = random.randint(0, 500)
    r3 = random.randint(0, 500)
    r4 = random.randint(0, 500)
    retStr += "h\n0 250 " + str(r1) + " " + str(r2) + " " + str(r3) + " " + str(r4) + " 500 250\n"

for i in range(50):
    r1 = random.randint(0, 500)
    r2 = random.randint(0, 500)
    r3 = random.randint(0, 500)
    r4 = random.randint(0, 500)
    retStr += "h\n500 250 " + str(r1) + " " + str(r2) + " " + str(r3) + " " + str(r4) + " 0 250\n"

retStr += "v\ng\nwee.png"
f = open("script_a", "w")
f.write(retStr)
f.close() 
parse_file( 'script_a', points, transform )
