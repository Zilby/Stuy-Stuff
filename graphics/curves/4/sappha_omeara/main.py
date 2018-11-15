from display import *
from matrix import *
from draw import *
from parser import *
from random import *

points = []
transform = new_matrix()

f = open ("script_c",'w')

for i in range (50):
    f.write("c\n")
    f.write(str(i*5) + " " + str(i * 5) + " " + str(i) + "\n")


params = [-40, 510, 60, 340, 210, 510, 185, 340]

for i in range(14, 25):
    f.write ("h\n")
    for j in range (8):
        f.write(str(params[j]) + " ")
        if j % 2 == 0:
            params[j] += 20
        else:
            params[j] -= 20
    f.write("\n")

for i in range(15):
    randoms = []
    for j in range(4):
        randoms.append(randrange(500))
    f.write("b\n 0 0 " +
            str(randoms[0]) + " " +
            str(randoms[1]) + " " +
            str(randoms[2]) + " " +
            str(randoms[3]) + " " + "500 500 \n")

f.write("v\ng\nimage.png\n")
f.close()

parse_file( 'script_c', points, transform )
