from display import *
from draw import *
from parser import *
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []

f = open("script", "w")
f.truncate()
f.write("p\n500 800 0 40 50 40\n")
f.write("d\n250 250 20 125\nd\n350 250 10 150\nd\n150 250 30 100\ni\nx\n90\ny\n-90\nt\n-300 250 0\na\n")
f.write("p\n750 450 0 50 50 50\n")
for i in range(0, 8):
    f.write("m\n")
    s = "{0} 250 {1}\n".format(i*100+150, i*10)
    f.write(s)
f.write("i\ny\n60\na\nt\n250 0 0\n")
f.write("v")

f.close()

points = []
transform = new_matrix()

parse_file("script", points, transform)