from display import *
from draw import *

retStr = ""
for i in range(50):
    retStr += "c\n250 250 " + str(i*10) + "\n"


retStr += "v\ng\nwee.png"
f = open("script_a", "w")
f.write(retStr)
f.close()
