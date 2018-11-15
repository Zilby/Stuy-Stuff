import sys
from random import random
from rgbpoints import *

#create 2d array, fill with blank points()
#then just access [x][y] or something and change the point to match
#create a function to write the entire array
#plot_line will call some plot() thing that replaces it I guess. very c-y

def plot_screen(xres, yres):
    for x in xrange(xres): #fill bkg
        for y in xrange(yres):
            pass
    print matrix
        


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print 'Usage: {0} <xres> <yres> <output fname>'.format(sys.argv[0])
        sys.exit()

    xres = int(sys.argv[1])
    yres = int(sys.argv[2])
    matrix = [ [Point(x,y) for x in xrange(xres)] for y in xrange(yres)]
    f = open(sys.argv[3], 'wb')
    f.write("P3\n{0} {1}\n 1000\n".format(xres, yres)) #header
    
    plot_screen(xres,yres)
    print 'Done!'
    f.close()
