from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):
    transform=ident(new_matrix())
    screen=new_screen()
    f=open(fname)
    lines=f.read().split('\n')
    for i in range(len(lines)):
        line=lines[i]
        line.strip()
        if line=="l":
            p=lines[i+1]
            p=p.split(' ')
            for x in range(len(p)):
                p[x]=int(p[x])
            add_edge(points,p[0],p[1],p[2],p[3],p[4],p[5])
        elif line=="i":
        elif line=="s":
        elif line=="t":
        elif line=="x":
        elif line=="y":
        elif line=="z":
        elif line=="a":
        elif line=="v":
        elif line=="g":
            draw_lines(points, screen, [0,0,255])
            save_ppm(screen, fname)
            save_extension(screen, fname)

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
