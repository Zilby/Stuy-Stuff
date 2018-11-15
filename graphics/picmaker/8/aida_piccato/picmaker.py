import math
def picmaker(filename, pixels):
    headers = "P3 500 500 255"
    f = open(filename+".ppm", 'w')
    f.truncate()
    f.write(headers)
    f.write(pixels)
    f.close()

def stripes():
    pixels = ""
    for i in range(0,500):
        for j in range(0,500):
            if j % 2 == 0:
                pixels += "(%d, %d, %d)" % (0,0,0)
            else:
                pixels += "(%d, %d, %d)" % (23, 234, 0)
    return pixels

def sqrt():
    pixels = ""
    for i in range(0,500):
        for j in range(0,500):
            pixels += "(%d, %d, %d)" % (math.sqrt(i),math.sqrt(i),math.sqrt(i))
    return pixels
    
picmaker("stripes", sqrt());
