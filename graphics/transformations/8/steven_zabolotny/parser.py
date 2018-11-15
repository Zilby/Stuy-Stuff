from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    f = open(fname, "r")
    screen = new_screen()
    c = f.readline()
    c = c[0:len(c) - 1]
    while(c != ""):
        print(c)
        if (c == "l"):
            c = f.readline()
            c = c[0:len(c) - 1]
            pts = c.split(" ")
            points.append([int(pts[0]), int(pts[1]), int(pts[2]), 1])
            points.append([int(pts[3]), int(pts[4]), int(pts[5]), 1])
        elif (c == "v"):
            #print(points)
            draw_lines(points, screen, [0, 255, 0])
            display(screen)
        elif (c == "i"):
            ident(transform)
        elif (c == "t"):
            c = f.readline()
            c = c[0:len(c) - 1]
            t = c.split(" ")
            transform = matrix_mult(make_translate(int(t[0]), int(t[1]), int(t[2])), transform)
            #print(transform)
        elif (c == "s"):
            c = f.readline()
            c = c[0:len(c) - 1]
            s = c.split(" ")
            transform = matrix_mult(make_scale(float(s[0]), float(s[1]), float(s[2])), transform)
        elif (c == "x"):
            c = f.readline()
            c = c[0:len(c) - 1]
            transform = matrix_mult(make_rotX(int(c)), transform)
        elif (c == "y"):
            c = f.readline()
            c = c[0:len(c) - 1]
            transform = matrix_mult(make_rotY(int(c)), transform)
        elif (c == "z"):
            c = f.readline()
            c = c[0:len(c) - 1]
            transform = matrix_mult(make_rotZ(int(c)), transform)
        elif (c == "a"):
            print(points)
            for p in range(0, len(points)):
                for x in range(0, len(points[p])):
                    points[p][x] = [points[p][x]]
                points[p] = matrix_mult(transform, points[p])
                for x in range(0, len(points[p])):
                    points[p][x] = points[p][x][0]
            print(points)
        elif (c == "g"):
            c = f.readline()
            c = c[0:len(c) - 1]
            draw_lines(points, screen, [0, 255, 0])
            save_ppm(screen, c)
        else:
            print("Invalid script entry: " + c)
        c = f.readline()
        c = c[0:len(c) - 1]

points = []
transform = new_matrix()

parse_file( 'script', points, transform )
