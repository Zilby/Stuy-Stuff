from display import *
from draw import *
import random

retStr = "i\n"

for i in range(25):
    r1 = random.randrange(40)
    r2 = random.randrange(50) + 40
    retStr += "d\n250 " + str(50*i-200) + " " + str(r1) + " " + str(r2) + "\n"


retStr += "z\n30\na\nv\ng\ndonut.png"

f = open("script_a", "w")
f.write(retStr)
f.close()
