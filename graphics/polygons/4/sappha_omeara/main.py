from display import *
from matrix import *
from draw import *
from parser import *
from random import *

points = []
transform = new_matrix()

#f = open ("script_c",'w')

#f.write("v\ng\nimage.png\n")
#f.close()

parse_file( 'script_test', points, transform )