from display import *
from matrix import *
from draw import *
from math import *
from types import *
# I had a neurotic need for everything to match the math notation of 
# matrices being defined as rows x columns, so my matrix items I read
# as matrix[row][column] 
# Since this would mean our point matrix is an n by 4 matrix, 
# not a 4 by n matrix, in order to make this work, I flipped...
# everything. So every single transformation is... flipped.
# As is the order of the multiplication (I do points x transform).
# Fortunately this only means my transform matrix is flipped along 
# a diagonal and should only be mildly instead of hair-wrenchingly confusing.
# Enjoy!

def parse_file( fname, points, transform ):
    screen = new_screen()
    color = [ 0, 255, 0 ]
    f = open(fname, "r")
    line = f.readline().strip()
    while line:
        if line == "l":
            p = []
            for x in f.readline().strip().split(' '):
                p.append(int(x))
            add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5])
        elif line == "i":
            for x in range(4):
                for y in range(4):
                    transform[x][y] = 0
                transform[x][x] = 1
        elif line == "s":
            p = []
            for x in f.readline().strip().split():
                p.append(float(x))
            for n in range(3):
                transform[n][n] *= p[n]
        elif line == "t":
            p = []
            for x in f.readline().strip().split():
                p.append(int(x))
            for n in range(3):
                transform[3][n] += p[n]
        elif line == "c":
            p = []
            for x in f.readline().strip().split():
                p.append(float(x))
            make_circle(points, p[0], p[1], p[2])
        elif line == "h":
            p = []
            for x in f.readline().strip().split():
                p.append(float(x))
            make_spline(points, "hermite",p)
        elif line == "b":
            p = []
            for x in f.readline().strip().split():
                p.append(float(x))
            make_spline(points, "bezier",p)


        elif line == "x":
            transform = rotate("x", f.readline().strip(), points,  transform)
        elif line == "y":
            transform = rotate("y", f.readline().strip(), points,  transform)
        elif line == "z":
            transform = rotate("z", f.readline().strip(), points,  transform)
        elif line == "a":
            #print "transform: "
            #print_matrix(transform)
            points = mult(points, transform, True)
        elif line == "v":
            clear_screen(screen)
            draw_lines( points, screen, color )
            display(screen)
        elif line == "g":
            save_ppm(screen, f.readline().strip().strip())
            display(screen)
        line = f.readline().strip()
        #print_matrix( points)
    f.close()
def rotate(axis, theta, points, transform):
    theta = float(theta) * pi / 180
    #print cos(theta)
    if axis == "x":
        t = new_matrix()
        t[0][0] = 1
        t[1][1] = cos(theta)
        t[1][2] = sin(theta)
        t[2][1] = -1.0 * sin(theta)
        t[2][2] = cos(theta)
    elif axis == "y":
        t = new_matrix()
        t[1][1] = 1
        t[0][0] = cos(theta)
        t[0][2] = -1.0 * sin(theta)
        t[2][0] = sin(theta)
        t[2][2] = cos(theta)
    elif axis == "z":
        t = new_matrix()
        t[2][2] = 1
        t[0][0] = cos(theta)
        t[0][1] = sin(theta)
        t[1][0] = -1.0 * sin(theta)
        t[1][1] = cos(theta)
    t[3][3] = 1
    #print_matrix(t)
    #print_matrix(transform)
    transform = mult(t, transform, False)
    #print_matrix(transform)
    return transform

points = []
transform = new_matrix(4,4)
f = open("script_c", "w")
f.write('''c
150 250 100
''')
for i in range(5):
    f.write("b\n{0} {1} {2} {3} {4} {5} {6} {7}\n".format(
            str(i * 100), str(0), str( i * 100 + 25), str(i * 85 + 50), 
            str(i * 100 + 75), str(i * 15 + 50), str(i * 100 + 100), str(0)))
for i in range(5):
    f.write("h\n{0} {1} {2} {3} {4} {5} {6} {7}\n".format(
            str(i * 100), str(500), str( i * 100-100), str(i * -250 - 50),
            str(i * 100 + 100), str(500), str(i * 100-100), str(i * 250 + 50)))
f.write('''v
g
pic.png
''')
f.close()
parse_file( 'script_c', points, transform )
