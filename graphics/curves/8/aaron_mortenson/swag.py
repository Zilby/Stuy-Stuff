import math

#cx, cy, r = 350, 350, 125
cx, cy, r = 250, 350, 125

print '''c
%i %i %i''' % (cx, cy, r)


for t in range(100):
    theta = 2*math.pi*(t+75)/100.0
    x0 = cx + r*math.cos(theta)
    y0 = cy + r*math.sin(theta)
    x1 = cx + r*3*math.cos(theta)
    y1 = cy + r*3*math.sin(theta)
    if t > 50:
        theta = 2*math.pi*(t+75+1)/100.0
    else:
        theta = 2*math.pi*(t+75-1)/100.0
    #dx0 = cx + r*math.cos(theta) - x0
    #dy0 = cy + r*math.sin(theta) - y0
    #dx1 = cx + r*3*math.cos(theta) - x1
    #dy1 = cy + r*3*math.sin(theta) - y1
    dx0 = cx + r*math.cos(theta)
    dy0 = cy + r*math.sin(theta)
    dx1 = cx + r*abs(50-t)*math.cos(theta)/10.0
    dy1 = cy + r*abs(50-t)*math.sin(theta)/10.0
    dx0 += (dx0 - x0) * 25
    dy0 += (dy0 - y0) * 25
    dx1 += (dx1 - x1) * 25
    dy1 += (dy1 - y1) * 25
    print 'b'
    print '%i %i %i %i %i %i %i %i' % (x0, y0, dx0, dy0, dx1, dy1, x1, y1)
    
print '''v
g
swag.png
q'''
