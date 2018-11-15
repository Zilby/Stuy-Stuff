from display import *
from draw import *
from matrix import *
import time, math
import sys
if (len(sys.argv) != 2):
    print "Parameter missing. Please input script file name"
    sys.exit()
    
f = [x.strip() for x in open(sys.argv[1]).readlines()]
screen = new_screen()
color = [255,0,0]
matrix=[]
tm = []

tm = identity()
command = ""

for x in f:
    if x == "l":
        command = "l"
    elif command == "l":
        line = x.split(" ")
        add_edge(matrix,int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))
        command = ""
    elif x == "i":
        tm = identity()
    elif x == "t":
        command = "t"
    elif command == "t":
        line = [int(y) for y in x.split(" ")]
        tm = matadd(tm,translate(line[0],line[1],line[2]))
        command = ""
    elif x == "s":
        command = "s"
    elif command == "s":
        line = [float(y) for y in x.split(" ")] #make this a float
        tm = matmult(tm,scale(line[0],line[1],line[2]))
        command = ""
    elif x == "v":
        draw_lines(matrix,screen,color)
        display(screen)
        screen = new_screen()
        time.sleep(1)
    elif x == "z":
        command = "z"
    elif command == "z":
        line = float(x)
        tm = matmult(tm,rotz(line))
        command = ""
    elif x == "y":
        command = "y"
    elif command == "y":
        line = float(x)
        tm = matmult(tm,roty(line))
        command = ""
    elif x == "x":
        command = "x"
    elif command == "x":
        line = float(x)
        tm = matmult(tm,rotx(line))
        command = ""
    elif x == "a":
        matrix = [matmult(tm,[[z] for z in y]) for y in matrix ]
        matrix = [[z[0] for z in y] for y in matrix]
    elif x == "g":
        command = "g"
    elif command == "g":
        draw_lines(matrix,screen,color)
        save_ppm(screen,x)#not sure why save_extension doesnt work
        screen = new_screen()
        command = ""
    else:
        print "wat"
