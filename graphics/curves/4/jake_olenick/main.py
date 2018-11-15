from display import *
from draw import *
from matrix import *

f = open("script_c","w")

for i in range(0,500,5):
    f.write("c\n")
    rad = (250 - abs(250-i))**2 / 250
    f.write("%d 250 %d\n"%(i, rad))

f.write("v")
