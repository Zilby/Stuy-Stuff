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

        elif line == "w":
            points = new_matrix()
        elif line == "p":
            p = []
            for x in f.readline().strip().split():
                p.append(int(x))
            make_prism(points, p[0], p[1], p[2], p[3], p[4], p[5])
        elif line =="m":
            p = []
            for x in f.readline().strip().split():
                p.append(int(x))
            make_sphere(points, p[0], p[1], p[2])
        elif line =="d":
            p = []
            for x in f.readline().strip().split():
                p.append(int(x))
            make_torus(points, p[0], p[1], p[2], p[3])
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
            draw_polygons( points, screen, color )
        elif line == "g":
            save_ppm(screen, f.readline().strip().strip())
            display(screen)
        line = f.readline().strip()
        #print_matrix( points)
    f.close()

points = []
transform = new_matrix(4,4)

parse_file( 'script_c', points, transform )
