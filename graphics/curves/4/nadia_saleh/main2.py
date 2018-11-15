from display import *
from matrix import *
from draw import *
from parser import *
from random import *

points = []
transform = new_matrix()


f= open ("script_c",'w')

params = [-40, 510, 60, 340, 210, 510, 185, 340]

f.write("a\n")

for i in range(25):
    f.write ("h\n")
    for j in range (len(params)):
        f.write(str(params[j]) + " ")
        if j % 2 == 0:
            params[j] += 20
        else:
            params[j] -= 20
    f.write("\n")

for q in range (10):
    f.write("c\n250 250 " + str(q*30) + " \n")


for k in range(10):
    randoms = []
    for j in range(4):
        randoms.append(randrange(500))
    f.write("b\n 0 0 " +
        str(randoms[0]) + " " +
        str(randoms[1]) + " " +
        str(randoms[2]) + " " +
        str(randoms[3]) + " " + "500 500 \n")
        
    

f.write("v\ng\nface.png\n")
f.close()

parse_file( 'script_c', points, transform )
