from rgbpoints import *
from writer import *


def plot_line(x0, y0, x1, y1, matrix, color=WHITE ):
    #print color
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
            plot_point(Point(x,y,0,color), matrix)
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
        d = A/2 + B
        while(y <= y1):
            plot_point(Point(x,y,0,color), matrix)
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
            plot_point(Point(x,y,0,color), matrix)
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
            plot_point(Point(x,y,0,color), matrix)
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

if __name__ == "__main__":
    print plot_line(0,0,200,50, [ [Point(x,y, WHITE) for x in xrange(40)] for y in xrange(40)])

    
    #print DEFAULT_COLOR
