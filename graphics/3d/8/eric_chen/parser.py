from display import *
from matrix import *
from draw import *
import math

def parse_file( filename, points, transform ):
    screen = new_screen()
    f = open(filename, 'r')

    while 1:
        l = f.readline()
        if len(l) == 0:
            break
        elif l[0] == 'l':
            s = map(float, f.readline().split(' '))
            add_edge(points, s[0],s[1],s[2],s[3],s[4],s[5])
        elif l[0] == 'i':
            transform = ident(transform)
        elif l[0] == 's':
            s = map(float, f.readline().split(' '))
            transform = matrix_mult(scale(s[0],s[1],s[2]),transform)
        elif l[0] == 't':
            s = map(float, f.readline().split(' '))
            transform = matrix_mult(translate(s[0],s[1],s[2]),transform)
        elif l[0] == 'x':
            s = map(float, f.readline().split(' '))
            transform = matrix_mult(rotateX(s[0]),transform)
        elif l[0] == 'y':
            s = map(float, f.readline().split(' '))
            transform = matrix_mult(rotateY(s[0]),transform)
        elif l[0] == 'z':
            s = map(float, f.readline().split(' '))
            transform = matrix_mult(rotateZ(s[0]),transform)
        elif l[0] == 'a':
            points = matrix_mult(points, transform)
        elif l[0] == 'v':
            screen = new_screen()
            draw_lines(points, screen, [255,255,255])
            display(screen)
        elif l[0] == 'g':
            s = f.readline().split()
            draw_lines(points, screen, [255,255,255])
            save_extension(screen, s)
            clear_screen(screen)
        elif l[0] == 'c':
            s = map(float, f.readline().split(' '))
            addCircle(points, s[0], s[1], 0, s[2], .01)
        elif l[0] == 'b':
            s = map(float, f.readline().split(' '))
            print s
            addCurve(points, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7],
                     .01, "bezier")
        elif l[0] == 'h':
            s = map(float, f.readline().split(' '))
            addCurve(points, s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7],
                     .01, "hermite")
        elif l[0] == 'p':
            s = map(float, f.readline().split(' '))
            addBox(points, s[0], s[1], s[2], s[3], s[4], s[5])
        elif l[0] == 'm':
            s = map(float, f.readline().split(' '))
            addSphere(points, s[0], s[1], s[2], .01)
        elif l[0] == 'd':
            s = map(float, f.readline().split(' '))
            addTorus(points, s[0], s[1], s[2], s[3], .01)
        elif l[0] == 'w':
            points = []

points = []
transform = new_matrix()

parse_file('script_c', points, transform)
