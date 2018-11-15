import math, random

f = open ("script_c", 'w')
s = ""
for i in range (0, 500, 7):
    if (i **2) % 2 == 0:
        s = s +  ( "c\n" + str(250) + " " + str (i - 20) + " " + str(i/2) + "\n")


for i in range (0, 500, 16):
    s = s + ("b\n" + str (0 + i ) + " " + str (0) + " " + str (0 + i/6 + i %10) + " " + str (500 - i /6 + i % 10) + " " + str (350 + i/2 - i%100) + " " + str (350 + i/2 - i%100) + " " + str (500 - i/2 + i% 20) + " " + str (500 - i/3 + i % 20) + "\n" )
    s = s + ("h\n" + str (220 + i/7) + " " + str (390 + i/17) + " " + str (0 + i/6) + " " + str (i /6 - 500) + " " + str (350 - i/2 + i%100) + " " + str (350 + i/2 - i%100) + " " + str (500 + i/2 - i% 20) + " " + str (500 + i/3 - i % 20) + "\n" )


s = s + "v\ng\nface.png"
                   
f.write(s)
f.close()
