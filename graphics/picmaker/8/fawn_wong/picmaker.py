import os, sys, math

pic = open("pic.ppm", "w")
pic.write("P3 \n")
pic.write("500 500 \n")
pic.write("255 \n")

for x in range(500):
    for y in range(500):
        if (2 * x + 3 * y) % 500 < 300:
            r = 0
            g = x + y % 255
            b = x + y % 255
        else:
            r = x + y % 255
            g = x + y % 255
            b = x + y % 255
        
        pic.write("%d %d %d "%(r, g, b))
    pic.write("\n")

pic.close()    
