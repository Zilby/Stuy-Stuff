from display import *
from matrix import *
from draw import *

screen = new_screen()
color = [255, 255, 255]

def parse_file( fname, points, transform ):
    f = open(fname, 'r')
    l = f.readline().strip()
    while l:
        if l != "g":
            screen = new_screen()
        if l == "l":
            l = f.readline().strip()
            p = []
            for x in l.split(" "):
                p.append(int(x))
            add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5])
        elif l == "i":
            transform = ident(transform)
        elif l == "s":
            l = f.readline().strip()
            p = []
            for x in l.split(" "):
                try:
                    p.append(int(x))
                except:
                    p.append(float(x))
            s = make_scale(p[0], p[1], p[2])
            transform = matrix_mult(s, transform)
        elif l == "t":
            l = f.readline().strip()
            p = []
            for x in l.split(" "):
                try:
                    p.append(int(x))
                except:
                    p.append(float(x))
            t = make_translate(p[0], p[1], p[2])
            transform = matrix_mult(t, transform)
        elif l == "x":
            l = f.readline().strip()
            x = make_rotX(int(l))
            transform = matrix_mult(x, transform)
        elif l == "y":
            l = f.readline().strip()
            y = make_rotY(int(l))
            transform = matrix_mult(y, transform)
        elif l == "z":
            l = f.readline().strip()
            z = make_rotZ(int(l))
            transform = matrix_mult(z, transform)
        elif l == "a":
            points = matrix_mult(transform, points)
        elif l == "v":
            draw_lines(points, screen, color)
            display(screen)
        elif l == "g":
            l = f.readline().strip()
            save_ppm(screen, l)
            display(screen)
        l = f.readline().strip()
        
            
transform = new_matrix()
points = []

parse_file( 'script_c', points, transform )
