import math
from math import pi

img = open('img.ppm','wb')

img.write("P3 500 500 255 \n")

xres = 500
yres = 500

for x in range(xres):
    for y in range(yres):

        #xarg = x/float(xres)
        #yarg = y/float(yres)
    
        #Sin & cos
        #r = int(math.fabs(math.sin(2*pi*xarg) * 255))
        #b = int(math.fabs(math.cos(2*pi*yarg) * 255))
        #g = 255

        #Circle
        r = int(math.sqrt(math.pow(x-250, 2) + math.pow(y-250, 2))%255)
        g = int(math.sqrt(math.pow(x-250, 2) + math.pow(y-250, 2))%255)
        b = 190
        
        img.write("{0} {1} {2} ".format(r, g, b))

img.close()
