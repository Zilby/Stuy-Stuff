from display import *
from draw import *
from parser import *
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script_d", "w")
f.truncate()
for i in range(-2, 10):
    f.write("b\n")
    args = [i*50, 150, i*50+50, 200, i*50+100, 50, i*5 + 200, 150]
    f.write(" ".join(map(str, args)) + "\n")
f.write("i\nt\n20 0 0\na\n")
f.write("c\n250 250 200\nc\n175 325 50\nc\n325 325 50\nc\n175 325 10\nc\n325 325 10\nh\n150 120 150 20 350 120 350 270\nb\n200 250 150 50 300 250 300 250\nv\n")

f.write("g\nmustache.png")
f.close()

points = []
transform = new_matrix()
parse_file( 'script_d', points, transform )
