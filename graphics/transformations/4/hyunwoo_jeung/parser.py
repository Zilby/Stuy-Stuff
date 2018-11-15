from display import *
from matrix import *
from draw import *

color = [255,255,0]

def parse_file( fname, points, transform ):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()

    m = 0
    while m < len(lines):
        line = lines[m].replace("\n","")
        if line == "l":
            n = lines[m+1].replace("\n","").split(' ')
            for a in range(len(n)):
                n[a] = float(n[a])
            add_edge(points,n[0],n[1],n[2],n[3],n[4],n[5])
        elif line == 'i':
            ident(transform)
        elif line == 's':
            n = lines[m+1].replace("\n","").split(' ')
            for a in range(len(n)):
                n[a] = float(n[a])
            matrix_mult(make_scale(n[0],n[1],n[2]),transform)
        elif line == 't':
            n = lines[m+1].replace("\n","").split(' ')
            for a in range(len(n)):
                n[a] = float(n[a])
            matrix_mult(make_translate(n[0],n[1],n[2]),transform)
        elif line == 'x':
            theta = lines[m+1].replace('\n','')
            matrix_mult(make_rotX(theta),transform)
        elif line == 'y':
            theta = lines[m+1].replace('\n','')
            matrix_mult(make_rotY(theta),transform)
        elif line == 'z':
            theta = lines[m+1].replace('\n','')
            matrix_mult(make_rotZ(theta),transform)
        elif line == 'a':
            matrix_mult(transform,points)
        elif line == 'v':
            screen = new_screen()
            draw_lines(points,screen,color)
            display(screen)
        elif line == 'g':
            fname = lines[m+1].replace('\n','')
            screen = new_screen()
            draw_lines(points,screen,color)
            save_ppm(screen,fname)
        m += 1

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
