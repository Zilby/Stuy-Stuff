import random
import math
f = open("script_c","w")

i = 0
while i < 250:
    a = i + 100
    b = 3 * i
    c = 50 - 2 * i
    d = 3 * i
    f.write("b\n0 0 %d %d %d %d %d %d\n"%(a,b,265,265,c,d))
    f.write("h\n500 0 %d %d %d %d %d %d\n"%(a - 3 * i,b + i * math.log(i + 1),500,2 * i,600 - c,d))
    f.write("c\n250 %d %d\n"%(15 * math.sqrt(i),i))
    i += 15
    
f.write("v\ng\ntest.png")
