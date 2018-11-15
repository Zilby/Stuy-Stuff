from rgbpoints import *

def plot_line(x0, y0, x1, y1, color=DEFAULT_COLOR):
    line_pts = []
    m = (float(y1)-y0) / (float(x1)-x0)
    if m > 0 and m <= 1:
        x = y0
        y = y0
        A = 2*(y1-y0)
        B = -2*(x1-x0)
        d = A + B/2
        while(x <= x1):
            line_pts.append(plot(x,y))
            if d > 0:
                y+=1
                A+=B
            x+=1
            d+=A
        return line_pts
    else:
        print 'Octant for line with slope {0} not supported yet'.format(m)
        return 0

if __name__ == "__main__":
    print plot_line(0,0,20,5)
    
    print DEFAULT_COLOR
