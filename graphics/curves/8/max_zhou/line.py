from rgbpoints import *
from writer import *
import math

def plot_line(x0, y0, x1, y1, matrix, color=WHITE, color2=None ):
    #print 'color:' + str(color)
    #print 'color2:' + str(color2)
    if color2 != None:
        dred = color2[0] - color[0]
        dblue = color2[1] - color[1]
        dgreen = color2[2] - color[2]
        def colorf():
            delt = math.sqrt((x1 -x0)**2 + (y1-y0)**2)
            cur = math.sqrt((x -x0)**2 + (y-y0)**2)
            return [int((cur/delt) * dred + color[0]), int((cur/delt) * dblue + color[1]), int((cur/delt) * dgreen + color[2])]
    else:
        colorf = lambda: color
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp

    if dx == 0:
        y = y0
        while y <= y1:
            #plot(screen, color,  x0, y)
            plot_point(Point(x0,y,0,colorf()),matrix)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot_point(Point(x,y0,0,colorf()),matrix)
            #plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot_point(Point(x,y,0,colorf()),matrix)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot_point(Point(x,y,0,colorf()),matrix)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot_point(Point(x,y,0,colorf()),matrix)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot_point(Point(x,y,0,colorf()),matrix)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx
'''
    line_pts = []
    if (x1-x0) != 0:
        m = (float(y1)-y0) / (float(x1)-x0)
    else:
        m = sys.maxint #still puts it into octant 2 range
    #print m
    if m >= 0 and m <= 1: #octant 1
        if x0 > x1 and y0 > y1: #octant 5
            tempx = x1
            x1 = x0
            x0 = tempx
            tempy = y1
            y1 = y0
            y0 = tempy
        x = x0
        y = y0
        A = 2*(y1-y0)
        B = -2*(x1-x0)
        d = A + B/2
        while(x <= x1):
            #line_pts.append(plot(x,y))b
            plot_point(Point(x,y,0,colorf()), matrix)
            #print 'x: ' + str(x) + ', y: ' + str(y)
            #print 'd: ' + str(d)
            #print matrix[x][y].color
            if d > 0:
                y+=1
                d+=B
            x+=1
            d+=A
        return matrix


    if m > 1: #octant 2
        if x0 > x1 and y0 > y1: #octant 6
            tempx = x1
            x1 = x0
            x0 = tempx
            tempy = y1
            y1 = y0
            y0 = tempy
        x = x0
        y = y0
        A = 2*(y1-y0)
        B = -2*(x1-x0)
        d = A - B/2
        while(y <= y1):
            plot_point(Point(x,y,0,colorf()), matrix)
            #print 'x: ' + str(x) + ', y: ' + str(y)
            #print 'd: ' + str(d)
            if (d < 0):
                x+=1
                d+=A
            y+=1
            d+=B
        return matrix

    if m < 0 and m >= -1: #octant 8
        if x0 > x1 and y0 < y1: #octant 4
            tempx = x1
            x1 = x0
            x0 = tempx
            tempy = y1
            y1 = y0
            y0 = tempy
        x = x0
        y = y0
        A = 2*(y1-y0)
        B = -2*(x1-x0)
        d = A + B/2
        while(x<=x1):
            plot_point(Point(x,y,0,colorf()), matrix)
            #print 'x: ' + str(x) + ', y: ' + str(y)
            #print 'd: ' + str(d)
            if(d < 0):
                y-=1
                d-=B
            x+=1
            d+=A
        return matrix
    if m < -1: #octant 7
        if x0 > x1 and y0 < y1: #octant 3
            tempx = x1
            x1 = x0
            x0 = tempx
            tempy = y1
            y1 = y0
            y0 = tempy
        x = x0
        y = y0
        A = 2*(y1-y0)
        B = -2*(x1-x0)
        d = A/2 + B
        while(y>=y1):
            plot_point(Point(x,y,0,colorf()), matrix)
           # print 'x: ' + str(x) + ', y: ' + str(y)
            #print 'd: ' + str(d)
            if(d>0):
                x+=1
                d+=A
            y-=1
            d-=B
    else:
        print 'Octant for line with slope {0} not supported yet'.format(m)
        return 0
'''
if __name__ == "__main__":
    print plot_line(0,0,200,50, [ [Point(x,y, WHITE) for x in xrange(40)] for y in xrange(40)])

    
    #print DEFAULT_COLOR
