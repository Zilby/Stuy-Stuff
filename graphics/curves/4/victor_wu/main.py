from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script_c","w")

for i in range(250,501,10):
    j = (i - 250) * 8
    f.write("h\n")
    f.write("%d %d %d %d %d %d %d %d\n"%(0,250,2000-j,2250-j,500,250,2500-j,2250-j))

for r in range(0,200,5):
        f.write("h\n 0 "+str(250+r)+" 250 400 250 100 500 "+str(250+r)+"\n")
        f.write("h\n 250 "+str(250-r)+" 250 100 250 400 0 "+str(250-r)+"\n")
    
f.write("v\ng\nimg.png")

display(screen)
