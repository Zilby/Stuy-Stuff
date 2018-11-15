from display import *
from matrix import *
from draw import *
import time

def parse_file( fname, points, transform ):
    transform = ident(new_matrix())
    screen = new_screen()
    f=open(fname)
    lines = f.read().split('\n')
    n = 0

    #******* IMPORTANT NOTE ***********#

    # I have note gotten image magic to work (there is a piazza question evidencing this)
    # As a result, I have created an alternative where i just create a new image, from 0 to n, each time a or v is entered. I will try and fix my problems (with image magic, not the ones stemming from divorce and an uninterested mother) 

    
    for  i in range(0,len(lines)):
        line= lines[i]
        line.strip()

        i = i + 1
        #print_matrix(transform)
        
        if line == "l":
            p = lines[i].split(' ')
            for x in range(0,len(p)):
                p[x]=int(p[x])
            add_edge(points,p[0],p[1],p[2],p[3],p[4],p[5])
        elif line == "s":
            args = lines[i].split(' ')
            r = make_scale(float(args[0]),float(args[1]),float(args[2]))
            transform = matrix_mult(r,transform)
        elif line == "t":
            args = lines[i].split(' ')
            r = make_translate(float(args[0]),float(args[1]),float(args[2]))
            transform = matrix_mult(r,transform)
        elif line == "x":
            arg = lines[i]
            r = make_rotX(int(arg))
            transform = matrix_mult(r,transform)
        elif line == "y":
            arg = lines[i]
            r = make_rotY(int(arg))
            transform = matrix_mult(r,transform)
        elif line == "z":
            arg = lines[i]
            r = make_rotZ(int(arg))
            transform = matrix_mult(r,transform)
        elif line == "g":
            #save_extension(screen,lines[i])
            display(screen, str(n))
            n = n+1
        else:
            i = i - 1
            if line == "i":
                transform = ident(transform)
            elif line == "a":
                points = matrix_mult(transform,points)
            elif line == "v":
                clear_screen(screen)
                draw_lines( points, screen, [255,0,0] )
                display(screen, str(n))
                n = n+1
            
        

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )

