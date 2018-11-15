from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    f = open(fname,'r')
    commands = f.read()
    scomm = commands.split('\n')
    print scomm
    i = 0
    while (i<len(scomm)):
        if scomm[i]=="l":
            coor = scomm[i+1].split(' ')
            if len(coor) != 6:
                print "Incorrect amount of parameters"
            else:
                for p in range(len(coor)):
                    coor[p]=int(coor[p])
                add_edge(points, coor[0], coor[1], coor[2], coor[3], coor[4], coor[5])
            i = i + 2
        elif scomm[i]=="i":
            transform=ident(transform)
            i = i + 1
        elif scomm[i]=="s":
            scale = scomm[i+1].split(' ')
            if len(scale) != 3:
                print "Incorrect amount of parameters"
            else:
                for p in range(len(scale)):
                    scale[p]=float(scale[p])
                transform = matrix_mult(make_scale(scale[0],scale[1],scale[2]),transform)
            i = i + 2
        elif scomm[i]=="t":
            move = scomm[i+1].split(' ')
            if len(move) != 3:
                print "Incorrect amount of paramters"
            else:
                for p in range(len(move)):
                    move[p]=int(move[p])
                transform = matrix_mult(make_translate(move[0],move[1],move[2]),transform)
            i = i + 2
        elif scomm[i]=="x":
            if (len(scomm[i+1].split(' ')) != 1):
                print "Incorrect amount of parameters"
            else:
                angle = int(scomm[i+1])
                transform = matrix_mult(make_rotX(angle),transform)
            i = i + 2
        elif scomm[i]=="y":
            if (len(scomm[i+1].split(' ')) != 1):
                print "Incorrect amount of parameters"
            else:
                angle = int(scomm[i+1])
                transform = matrix_mult(make_rotY(angle),transform)
            i = i + 2
        elif scomm[i]=="z":
            if (len(scomm[i+1].split(' ')) != 1):
                print "Incorrect amount of parameters"
            else:
                angle = int(scomm[i+1])
                transform = matrix_mult(make_rotZ(angle),transform)
            i = i + 2
        elif scomm[i]=="a":
            points = matrix_mult(transform,points)
            i = i + 1
        elif scomm[i]=="v":
            screen = new_screen()
            draw_lines(points, screen, [255,255,255])
            display(screen)
            i = i + 1
        elif scomm[i]=="g":
            screen = new_screen()
            draw_lines(points, screen, [255,255,255])
            filename = scomm[i+1]
            save_ppm(screen, filename)
            i = i + 2
        else:
            print "Invalid command %s, moving on to the next one"%(scomm[i])
            i = i + 1

    
points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )

