import math
import random

'''
f = open("script","w")
for n in range(31):
    f.write("b\n")
    f.write("0 0 " + str(100*math.sin(n)) + " " + str(100*math.cos(n)) + " " + str(100*math.cos(n)*(-1)) + " " + str(100*math.sin(n)*(-1)) + " 500 500 \n")
f.write("v\ng\nimage.png")
f.close
'''
f = open("script_d","w")
for x in xrange(25):
    f.write("b\n")
    f.write("0 250 " + str(random.randint(0,250)) + " " + str(random.randint(0,500)) + " " + str(random.randint(250,500)) + " " + str(random.randint(0,500))+ " 500 250"+ "\n")
    f.write("h\n")
    f.write("250 0 " + str(random.randint(0,500)) + " " + str(random.randint(0,250)) + " 250 500 " + str(random.randint(0,500)) + " " + str(random.randint(250,500))+ "\n")
f.write("c\n250 250 200\n")
f.write("v\ng\nimage.png")
f.close
