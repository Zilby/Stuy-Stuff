from display import *
from matrix import *
from draw import *
import time

def parse_file( fname, points, transform ):
    
    transform = ident(new_matrix())
    screen = new_screen()
    f=open(fname)
    edge_matrix = []
    lines = f.read().split('\n')
    for  i in range(0,len(lines)):
        line= lines[i]
        
        line.strip()
        if line == "l":
           
            p = lines[i+1].split(' ')
            for x in range(0,len(p)):
                p[x]=int(p[x])
            add_edge(edge_matrix,p[0],p[1],p[2],p[3],p[4],p[5])
            i+=1
        elif line == "i":
            transform = ident(transform)
            #print_matrix(transform)
        elif line == "s":
            args = lines[i+1].split(' ')
            s = make_scale(float(args[0]),float(args[1]),float(args[2]))
            matrix_mult(s,transform)
        elif line == "t":
            args = lines[i+1].split(' ')
            t = make_translate(float(args[0]),float(args[1]),float(args[2]))
            matrix_mult(t,transform)
        elif line == "x":
            args = lines[i+1]
            r = make_rotX(int(args))
            matrix_mult(r,transform)
            i+=1
        elif line == "y":
            args = lines[i+1]
            r = make_rotY(int(args))
            i+=1
            matrix_mult(r,transform)
        elif line == "z":
            args = lines[i+1]
            r = make_rotZ(int(args))
            matrix_mult(r,transform)
        elif line == "a":
            matrix_mult(transform,edge_matrix)
            ident(transform)
        elif line == "v":
            clear_screen(screen)
<<<<<<< HEAD
  
            #print_matrix( transform)
=======
            print_matrix( transform)
>>>>>>> 5d0676880f5ba6f747e5055a0f7228b381a58d5f
            draw_lines( edge_matrix, screen, [0,255,0] )
            display(screen)
            
            time.sleep(2)
        elif line == "g":
            save_extension(screen,lines[i+1])
def writeDesign():
    w= open("script_c","w")
    i=0
    while i<XRES:
        '''
        w.write("l\n")
        w.write(" ".join([str(XRES-1),"0",str(XRES/2),str(50+(i/4)),str(YRES - i),str(YRES/2)])+"\n")
        
        w.write("l\n")
        w.write(" ".join([str(XRES-1),"0",str(XRES/2),str(i),str(YRES - 50-(i/4)), str(YRES/2)])
+"\n")
        '''
        w.write("l\n")
        w.write(" ".join(["0", "0", "0", str(XRES - 50- (i/4)), str(YRES - i), "0" ])+"\n")
        w.write("l\n")
        w.write(" ".join(["0", "0", "0", str(XRES - i), str(YRES - 50- (i/4)), "0"])+"\n")
        '''
        w.write("l\n")
        w.write(" ".join([str(XRES-1), str(YRES - 1), "0", str(50+(i/4)), str(YRES - i), "0" ])+"\n")
        w.write("l\n")
        w.write(" ".join([str(XRES-1), str(YRES - 1), "0", str(i), str(YRES - 50-(i/4)), "0"])+"\n")
        '''
        i+=50
    w.write("z\n45\n")
    w.write("a\nv\ng\npic.png")
    w.close()


points = []
transform = new_matrix()
#writeDesign()
parse_file( 'script_c', points, transform )
