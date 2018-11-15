import math
import random

width = 512
height = 512
code = "P3\n%d %d\n255\n"%(width,height)
r=random.randint(0,255)
for i in range(width):
    for j in range(height):
        r=(((((i-10)**2)+((j-10)**2))**.5))%256
        g=((math.fabs(((i-10)**2)-((j-10)**2))**.5))%256
        b=(((((r-10)**2)+((g-10)**2))**.5)+r)%256
        code+="%d %d %d "%(r,g,b)

f = open("circle-stuff.ppm","w")
f.write(code)
f.close()
