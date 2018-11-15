import sys
from random import random
from rgbpoints import *
from line import *
from matrix import *
from parser import *
from threedee import *

#create 2d array, fill with blank points()
#then just access [x][y] or something and change the point to match
#create a function to write the entire array
#plot_line will call some plot() thing that replaces it I guess. very c-y


def plot_point(p, pmatrix):
    try:
        pmatrix[p.x][p.y] = p
    except:
        pass
    #print matrix[p.x][p.y].color

def plot_screen(f, pmatrix):
    for y in xrange(len(pmatrix[0])):
        for x in xrange(len(pmatrix)):
            #print pmatrix[x][y].plot_point()
            f.write(pmatrix[x][y].plot_point())
            
            
            
if __name__ == "__main__":
    pt_matrix = []
    if len(sys.argv) != 5:
        print 'Usage: {0} <xres> <yres> <output fname> <script file>'.format(sys.argv[0])
        sys.exit()
    xres = int(sys.argv[1])
    yres = int(sys.argv[2])
 #   '''
    f = open(sys.argv[4])
    commands = f.readlines()
    f.close()



    c = 0
    while c  <  len(commands):
        cmd = commands[c].strip()

        if cmd in 'lstxyzcbhpmd':
            c+= 1
            args = commands[c].strip().split(' ')
            i = 0
            while i < len( args ):
                args[i] = float( args[i] )
                i+= 1

            if cmd == 'l':
                add_edge( pt_matrix, args[0], args[1], args[3], args[4], z1=args[2],z2=args[5] )

            elif cmd == 'c':
                add_circle(args[0], args[1], args[2], pt_matrix )

            elif cmd == 'b':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'BEZIER' )

            elif cmd == 'h':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'HERMITE' )

            elif cmd == 'p':
                add_box(args[0], args[1], args[2], args[3], args[4], args[5], pt_matrix, random_color(), random_color())

            elif cmd == 'm':
                add_sphere(args[0], args[1], args[2], pt_matrix, random_color(), random_color())

            elif cmd == 'd':
                add_torus(args[0], args[1], args[2], args[3], pt_matrix, random_color(), random_color())

            elif cmd == 's':
                s = scale( args[0], args[1], args[2] )
                m_mult(master, s )

            elif cmd == 't':
                t = translate( args[0], args[1], args[2] )
                m_mult(master, t)

            else:
                angle = args[0]
                if cmd == 'x':
                    r = rot_x( angle )
                elif cmd == 'y':
                    r = rot_y( angle )
                elif cmd == 'z':
                    r = rot_z( angle )
                m_mult(master, r )

        elif cmd == 'i':
            master = identity

        elif cmd == 'w':
            pt_matrix = []

        elif cmd == 'a':
            #m_mult( transform, points )
            pt_matrix = apply_transformations()

        elif cmd in 'vg':
            print 'When finished, files are automatically saved to the desired directory in command-line args.  Sorry, no viewing.'
            break
        else:
            print 'Invalid command: ' + cmd
        c+= 1
#    '''

    #add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "HERMITE", random_color(), random_color()) #endpoint is 400, 100
    #add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 300, 300
    #add_curve(40, 100, 0, 0, 300, 300, 400, 100, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 400, 100
    #add_sphere(250,250,150, pt_matrix, random_color(), random_color())
    #add_torus(250, 250, 50, 150, pt_matrix, random_color(), random_color())
    #add_box(400,400,100, 200,200,200, pt_matrix, random_color(), random_color())

    r = rot_x(45)
    r2 = rot_y(45)
    t = translation(150,0,0)
    t2 = translation(150,400,100)
    s = scale(2,2,2)
    print r
    master = m_mult(master, r)
    master = m_mult(master, r2)
    #master = m_mult(master, t)
    #master = m_mult(master, s)
    master = m_mult(master, t2)
    print t2
    print 'master:' + str(master)
    new_pt_matrix = apply_transformations(pt_matrix, master)
    print pt_matrix[5].x
    #print new_pt_matrix[5].x
    screen = [ [Point(x,y) for x in xrange(xres)] for y in xrange(yres)]
    plot_edge_lines(new_pt_matrix, screen)
    f = open(sys.argv[3], 'wb')
    f.write("P3\n{0} {1}\n 255\n".format(xres, yres)) #header    
    plot_screen(f, screen)
    #print matrix
    print 'Done!'
    f.close()
