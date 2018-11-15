import sys
from random import random
from rgbpoints import *
from line import *
from matrix import *
from parser import *

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
    #print matrix
    #for x in xrange(len(matrix)):
    #    for y in xrange(len(matrix[x])):
    #        f.write(matrix[x][y].plot_point())
    for y in xrange(len(pmatrix[0])):
        for x in xrange(len(pmatrix)):
            #print pmatrix[x][y].plot_point()
            f.write(pmatrix[x][y].plot_point())
'''
def parse(script):
    lines = script.readlines()
    for i in len(lines):
        if lines[i] == "l":# add a line
            params = lines[i+1].split()
            #x1, y1, x2, y2, color1, color2, z1, z2
            
            if params.length == 7: #one color, weird vars...
                add_edge(matrix, params[0], params[1], params[3], params[4], params[5], params[2], params[3]) 
'''
            
            
            
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print 'Usage: {0} <xres> <yres> <output fname> <script file>'.format(sys.argv[0])
        sys.exit()
    xres = int(sys.argv[1])
    yres = int(sys.argv[2])
    f = open(sys.argv[4])
    commands = f.readlines()
    f.close()



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
                add_edge( pt_matrix, args[0], args[1], args[3], args[4], z1=args[2],z2=args[5] )

            elif cmd == 'c':
                add_circle(args[0], args[1], args[2], pt_matrix )

            elif cmd == 'b':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'BEZIER' )

            elif cmd == 'h':
                add_curve(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], pt_matrix, 'HERMITE' )


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

        elif cmd == 'a':
            #m_mult( transform, points )
            pt_matrix = apply_transformations()

        elif cmd in 'vg':
            print 'When finished, files are automatically saved to the desired directory in command-line args.  Sorry, no viewing.'
            break
        else:
            print 'Invalid command: ' + cmd
        c+= 1

    #add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "HERMITE", random_color(), random_color()) #endpoint is 400, 100
    #add_curve(40, 100, 0, 0, 400, 100, 300, 300, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 300, 300
    #add_curve(40, 100, 0, 0, 300, 300, 400, 100, pt_matrix, "BEZIER", random_color(), random_color()) #endpoint is 400, 100

    for x in xrange(0,155,3):
        add_circle(250, 250, 50 + x, pt_matrix, [0,0,0], [x+100,x,x+50])


    for x in xrange(128):
        add_curve(0, 350, x, 500-x, 500, 350, 350-x, 350+x, pt_matrix, "HERMITE", [0,127+x,0], [127+x, 0, 0])
        add_curve(0, 250, x, 500-x, 500, 250, 250-x, 250+x, pt_matrix, "HERMITE", [0,0,127+x], [0, 127+x, 0])
        add_curve(0, 150, x, 500-x, 500, 150, 150-x, 150+x, pt_matrix, "HERMITE", [127+x,0,0], [0, 0, 127+x])

        add_curve(0, 350, x, 500, 500, 350, 350, 350, pt_matrix, "BEZIER", [0,127+x,127+x], [127+x, 127+x, 0])
        add_curve(0, 250, x, 500, 500, 250, 250, 250, pt_matrix, "BEZIER", [127+x,0,127+x], [0, 127+x, 127+x])
        add_curve(0, 150, x, 500, 500, 150, 150, 150, pt_matrix, "BEZIER", [127+x,127+x,0], [127+x, 0, 127+x])


    pt_matrix = apply_transformations()
    screen = [ [Point(x,y) for x in xrange(xres)] for y in xrange(yres)]
    plot_edge_lines(pt_matrix, screen)
    f = open(sys.argv[3], 'wb')
    f.write("P3\n{0} {1}\n 255\n".format(xres, yres)) #header
    
    #pt_matrix = parse(sys.argv[4], sys.argv[3], xres, yres)

    #print pt_matrix
    #for x in xrange(300):
    #    plot_line(xres/2, yres/2,  random.randint(0,xres-1), random.randint(0,yres-1), matrix, random.choice([[255,0,0], [0,255,0], [0,0,255]]))
    
    plot_screen(f, screen)
    #print matrix
    print 'Done!'
    f.close()
