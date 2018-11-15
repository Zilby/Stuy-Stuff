import math

xSize = 600
ySize = 600
text = "P3\n%d %d\n255\n"%(xSize,ySize)
for i in range(ySize):
    for j in range(xSize):
        a = abs(math.sin(math.sqrt(j) * i / ySize * math.pi)) * 255
        b = abs(math.cos(math.sqrt(i) * j / xSize * math.pi)) * 255
        c = math.sqrt(1. * (i ** 2 + j ** 2) / (xSize ** 2 + ySize ** 2)) * 255
        text += "%d %d %d "%(a,b,c)
f = open("img.ppm","w")
f.write(text)
f.close()
