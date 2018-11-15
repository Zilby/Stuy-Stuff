from display import *
from matrix import *
from draw import *

color = [0, 255, 0]

def parse_file( fname, points, transform ):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    screen = new_screen()
    i = 0
    while i < len(lines):
        l = lines[i].replace("\n","")
        if l == "l":
            coor = lines[i+1].replace("\n","").split(" ")
            coor = [float(q) for q in coor]
            add_edge(points, coor[0], coor[1], coor[2], coor[3], coor[4], coor[5])
            
        elif l == "c":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_circle(points, values[0], values[1], 0, values[2], 0.01)
        elif l == "h":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_curve(points,values[0],values[1],values[2],values[3],values[4],
                      values[5],values[6],values[7],0.01,"hermite")
        elif l == "b":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_curve(points,values[0],values[1],values[2],values[3],values[4],
                      values[5],values[6],values[7],0.01,"bezier")

        elif l == "p":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_prism(points,values[0],values[1],values[2],values[3],values[4],values[5])
        elif l == "m":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_sphere(points,values[0],values[1],values[2],0.02)
        elif l == "d":
            values = [float(q) for q in lines[i+1].replace("\n","").split(" ")]
            add_torus(points,values[0],values[1],values[2],values[3],0.02)
            
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
            
        elif l == "w":
            points = []
        elif l == "vn":
            draw_lines(points, screen, color)
        elif l == "v":
            draw_lines(points, screen, color)
            display(screen)
        elif l == "g":
            fname = lines[i+1].replace("\n","")
            draw_lines(points, screen, color)
            save_ppm(screen, fname)
        i += 1
        
         

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
