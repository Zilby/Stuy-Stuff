from display import *
from matrix import *
from draw import *

color = [0, 255, 0]

def parse_file( fname, points, transform ):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    i = 0
    while i < len(lines):
        l = lines[i].replace("\n","")
        if l == "l":
            coor = lines[i+1].replace("\n","").split(" ")
            coor = [float(q) for q in coor]
            add_edge(points, coor[0], coor[1], coor[2], coor[3], coor[4], coor[5])
        elif l == "i":
            ident(transform)
        elif l == "s":
            values = lines[i+1].replace("\n","").split(" ")
            values = [float(q) for q in values]
            matrix_mult(make_scale(values[0], values[1], values[2]),transform)
        elif l == "t":
            values = lines[i+1].replace("\n","").split(" ")
            values = [float(q) for q in values]
            matrix_mult(make_translate(values[0], values[1], values[2]),transform)
        elif l == "x":
            theta = float(lines[i+1].replace("\n",""))
            matrix_mult(make_rotX(theta),transform)
        elif l == "y":
            theta = float(lines[i+1].replace("\n",""))
            matrix_mult(make_rotY(theta),transform)
        elif l == "z":
            theta = float(lines[i+1].replace("\n",""))
            matrix_mult(make_rotZ(theta),transform)
        elif l == "a":
            matrix_mult(transform,points)
        elif l == "v":
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)
        elif l == "g":
            fname = lines[i+1].replace("\n","")
            screen = new_screen()
            draw_lines(points, screen, color)
            save_ppm(screen, fname)
        i += 1
        
         

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
