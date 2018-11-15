from display import *
from matrix import *
from draw import *

cmds_args = ['l','s','t','x','y','z','g']
cmds_noargs = ['i','a','v']
screen = new_screen()

def parse_file( fname, points, transform ):
    f = open(fname, 'r')
    cmd = f.readline().rstrip()

    while(cmd):
        if cmd in cmds_args:
            args = f.readline().rstrip()
            if cmd == 'g':
                #print args
                draw_lines(points, screen, [0,255,0])
                #save_extension(screen,args)
                save_ppm(screen,args)
            else:
                #print args
                args = map(float,args.split(" "))
                #print args
                i = ident(new_matrix()) #in case bad things happen
                if cmd == 'l':
                    add_edge(points, args[0],args[1],args[2],args[3],args[4],args[5])
                elif cmd == 's':
                    i = make_scale(args[0],args[1],args[2])
                elif cmd == 't':
                    i = make_translate(args[0],args[1],args[2])
                elif cmd == 'x':
                    i = make_rotX(args[0])
                elif cmd == 'y':
                    i = make_rotY(args[0])
                elif cmd == 'z':
                    i = make_rotZ(args[0])
                transform = matrix_mult(i, transform)

        elif cmd in cmds_noargs:
            if cmd == 'i':
                transform = ident(transform)
            elif cmd == 'a':
                points = matrix_mult(transform,points)
            elif cmd == 'v':
                draw_lines(points,screen,[0,255,0])
                display(screen)
        cmd = f.readline().rstrip()
    f.close()
    
points = []
transform = new_matrix()

#parse_file( 'script_c', points, transform )
parse_file( 'script2_c', points, transform )
