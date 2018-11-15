from display import *
from matrix import *
from draw import *
from random import *
from parser import *

points = []
transform = new_matrix()


f= open ("script_c",'w')

for j in range (10):
    f.write("d\n0 0 " +
            str(randrange(50)) + " " +
            str(randrange(250)) + "\n" )
    f.write("m\n0 0 " +
            str(randrange(250)) + "\n")
    f.write("i\nx\n30\ny\n30\nz\n30\nt\n250 250 0\na\n")
    f.write("i\nx\n" +
            str(randrange(180)) + "\ny\n" +
            str(randrange(180)) + "\nz\n" +
            str(randrange(180)) +"\na\n")

f.write("v\ng\npic.png\n")
f.close()
parse_file( 'script_c', points, transform )