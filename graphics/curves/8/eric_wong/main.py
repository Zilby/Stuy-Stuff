from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script_c", 'w')

for r in range(1, 100):
    if r%5 == 0:
        s = "250 250 "+str(r*5)+" "+str(r*10)+" 500 150 "+str(r*10)+" "+str(r*15)+" "
        f.write("h\n%s\n"%s)

for r in range(1, 100):
    if r%5 == 0:
        s = "250 250 "+str(r*5)+" "+str(r*10)+" 100 150 "+str(r*10)+" "+str(r*15)+" "
        f.write("h\n%s\n"%s)

for r in range(1, 100):
    if r%5 == 0:
        s = "500 150 "+str(r*5)+" "+str(r*10)+" 250 250 "+str(r*10)+" "+str(r*15)+" "
        f.write("b\n%s\n"%s)
    
for r in range(1, 100):
    if r%5 == 0:
        s = "100 150 "+str(r*5)+" "+str(r*10)+" 250 250 "+str(r*10)+" "+str(r*15)+" "
        f.write("b\n%s\n"%s)

for x in range(XRES):
    for y in range(YRES):
        if x%100 == 0 and y%100 == 0:
            s = str(x)+' '+str(y)+' 100'
            f.write("c\n%s\n"%s)
   

f.write("v\ng\ncircle.png")
