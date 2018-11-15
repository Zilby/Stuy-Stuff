from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    
    f = open( fname )
    commands = f.readlines()
    f.close()
    screen = new_screen()
    colors = [[ 0, 255, 0 ],[ 0, 0, 255],[7, 242, 144],[255, 0, 0]]
    co = 0
    c = 0
    while c  <  len(commands):
        color = colors[co]
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
            draw_lines( points, screen, color )
            points=[]
            co+=1
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

def writer():
    f= open ("script_c",'w')
    for r in range(0,500,10):
        f.write("b\n0 0 "+str(r*2)+" "+str(r/2)+" "+str(500-(r*2))+" "+str(500-(r/2))+" 500 500\n")
    f.write("vg\n")
    for r in range(0,500,10):
        f.write("b\n500 0 "+str(500-(r/2))+" "+str(r*2)+" "+str(r/2)+" "+str(500-(r*2))+" 0 500\n")
    f.write("vg\n")
    for r in range(25,60,1):
        f.write("c\n250 250 "+str(r)+"\n")
    for r in range(80,115,1):
        f.write("c\n250 250 "+str(r)+"\n")
    f.write("vg\n")
    for r in range(0,10,1):
        f.write("c\n250 250 "+str(r)+"\n")
    f.write("v\ng\npic.png\n")
    f.close

writer()
parse_file( './script_c', points, transform )

