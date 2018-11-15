import math

f = open("pic.ppm" , "w")
f.write("P3 500 500 255\n")

for i in range(500):
    for j in range(500):
        r = (i+j) %256
        g = (i*j) %256
        b = ((i-j) * (i-j)) %256
        f.write( "%d %d %d "%(r,g,b))

f.close()
