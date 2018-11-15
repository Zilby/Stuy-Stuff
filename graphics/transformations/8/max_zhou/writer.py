import sys
from random import random
from rgbpoints import *
from line import *


#create 2d array, fill with blank points()
#then just access [x][y] or something and change the point to match
#create a function to write the entire array
#plot_line will call some plot() thing that replaces it I guess. very c-y


def plot_point(p, matrix):
    matrix[p.x][p.y] = p
    #print matrix[p.x][p.y].color

def plot_screen(f, matrix):
    #print matrix
    #for x in xrange(len(matrix)):
    #    for y in xrange(len(matrix[x])):
    #        f.write(matrix[x][y].plot_point())
    for y in xrange(len(matrix[0])):
        for x in xrange(len(matrix)):
            f.write(matrix[x][y].plot_point())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print 'Usage: {0} <xres> <yres> <output fname>'.format(sys.argv[0])
        sys.exit()

    xres = int(sys.argv[1])
    yres = int(sys.argv[2])
    matrix = [ [Point(x,y) for x in xrange(xres)] for y in xrange(yres)]
    f = open(sys.argv[3], 'wb')
    f.write("P3\n{0} {1}\n 255\n".format(xres, yres)) #header
    
    '''
    #plot_point(Point(1,2))
    plot_line(0,0,200,50, matrix, [255,0,0]) #octant 1
    plot_line(0,0,20,5, matrix, [0,255,0])
    plot_line(0,100,150,100, matrix, random_color()) #horizontal
    plot_line(100,0,100,175, matrix, random_color()) #vertical
    plot_line(150,130,0,0, matrix, random_color()) #octant 5
    plot_line(0,0, 50, 100, matrix, random_color()) #octant 2
    plot_line(120,40,30,10, matrix, random_color())#octant 6
    plot_line(0,100,100,75, matrix, random_color()) #octant 8
    plot_line(125,100,25,125, matrix, random_color()) #octant 4
    plot_line(0,150,50,50, matrix, random_color()) #octant 7
    plot_line(75,75,25,175, matrix, random_color()) #octant 3
    '''
    
    for x in xrange(300):
        plot_line(xres/2, yres/2,  random.randint(0,xres-1), random.randint(0,yres-1), matrix, random.choice([[255,0,0], [0,255,0], [0,0,255]]))
    
    plot_screen(f, matrix)
    #print matrix
    print 'Done!'
    f.close()
