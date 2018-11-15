from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    
    f = open( fname )
    commands = f.readlines()
    f.close()
    screen = new_screen()
    colors = [[ 138, 43, 226],[ 0, 255, 0 ],[ 0, 0, 255],[255, 0, 0],[ 0, 255, 255 ],[255, 0, 0]]
    co = 0
    c = 0
    while c  <  len(commands):
        color = colors[co]
        cmd = commands[c].strip()

        if cmd[0] == '#':
            pass

        elif cmd in 'lstxyzcbhmdp':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                add_edge( points, args[0], args[1], args[2], args[3], args[4], args[5] )
                
            elif cmd == 'm':
                add_sphere( points, args[0], args[1], 0, args[2], 5 )

            elif cmd == 'd':
                add_torus( points, args[0], args[1], 0, args[2], args[3], 5 )

            elif cmd == 'p':
                add_box( points, args[0], args[1], args[2], args[3], args[4], args[5] )

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

        elif cmd in 'vgwk':
            if cmd in 'vgw':
                draw_polygons( points, screen, color )            
            if cmd == 'v':
                display( screen )
            elif cmd == 'g':
                c+= 1
                save_extension( screen, commands[c].strip() )
            elif cmd == 'w':
                points = []
            elif cmd == 'k':
                co+=1
        else:
            print 'Invalid command: ' + cmd
        c+= 1


points = []
transform = new_matrix()

def writer():
    f= open ("script_c",'w')
    y= "x\n30\ny\n5\nz\n10\nt\n250 250 250\na\n"
    x= y+"w\nk\n"
    d= "d\n0 0 10 140\ni\n"
    f.write("d\n0 200 20 100\nd\n0 -200 20 100\n")
    angle=45
    while(angle<225):
        f.write(d+"z\n"+str(angle)+"\n"+x)
        angle+=45
    f.write("m\n0 0 150\ni\n"+y)
    f.write("v\ng\npic.png\n")
    f.close

writer()
parse_file( 'script_c', points, transform )

#parse_file( 'temp', points, transform )
