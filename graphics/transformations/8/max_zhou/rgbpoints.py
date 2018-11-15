import sys
RED = 0
BLUE = 1
GREEN = 2

import random
WHITE = [255,255,255]
DEFAULT_COLOR = [0,0,0]


class Point:
    def __init__(self, x, y, z=0, color=DEFAULT_COLOR):
        #rgb is 0-256
        self.color = color
        #self.red = red % 255
        #self.green = green % 255
        #self.blue = blue % 255
        self.x = x
        self.y = y
        self.z = z
        self.qwert = 1

    def plot_point(self):
        return "{0} {1} {2}\n".format(self.color[RED], self.color[BLUE], self.color[GREEN])

def plot(x,y,z=0,color=DEFAULT_COLOR):
    pt = "{0} {1} {2}\n".format(color[RED], color[BLUE], color[GREEN])
    return pt
    
def random_color():
    return [random.randint(127,255), random.randint(127,255), random.randint(127,255)]


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print 'Usage: {0} <xres> <yres> <output fname>'.format(sys.argv[0])
        sys.exit()

    xres = int(sys.argv[1])
    yres = int(sys.argv[2])
    f = open(sys.argv[3], 'wb')
    f.write("P3\n{0} {1}\n 1000\n".format(xres, yres)) #header
    matrix = []
    matrix.append(Point(5,5,5))
    matrix.append(Point(10,10,10))
    for point in matrix:
        f.write(point.plot_point())
    #print matrix

    
    print 'Done!'
    f.close()

