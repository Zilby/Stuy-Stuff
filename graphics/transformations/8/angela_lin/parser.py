from display import *
from matrix import *
from draw import *

'''
* l: add a line to the point matrix -  takes 6 arguments (x0, y0, z0, x1, y1, z1)
* i: set the transform matrix to the identity matrix
* s: create a scale matrix, then multiply the transform matrix by the scale matrix -  takes 3 arguments (sx, sy, sz)
* t: create a translation matrix, then multiply the transform matrix by the translation matrix - takes 3 arguments (tx, ty, tz)
* x: create an x-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
* y: create an y-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
* z: create an z-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
* a: apply the current transformation matrix to the edge matrix
* v: draw the lines of the point matrix to the screen, display the screen (not applicable for java)
* g: draw the lines of the point matrix to the screen/frame save the screen/frame to a file - takes 1 argument (file name)
'''

def parse_file( fname, points, transform ):
    input = open(fname).read().splitlines() #parses using \n
    i = 0
    screen = new_screen()
    color = [255, 100, 100]
           
    while (i < len(input)):
        if (input[i] == 'l'):
            #adds a line to the point matrix
            i += 1
            a = input[i].split() #split string by whitespace
            add_edge(points, float(a[0]), float(a[1]), float(a[2]), float(a[3]), float(a[4]), float(a[5]))

        elif (input[i] == 'i'):
            #set the transform matrix to identity matrix
            transform = ident()

        elif (input[i] == 's'):
            #create a scale matrix, then multiply transform by scale
            i += 1
            a = input[i].split()
            scale = make_scale(float(a[0]), float(a[1]), float(a[2]))
            transform = matrix_mult(scale, transform)

        elif (input[i] == 't'):
            #creates a translation matrix, then multiply transform by trans
            i += 1
            a = input[i].split()
            trans = make_translate(float(a[0]), float(a[1]), float(a[2]))
            transform = matrix_mult(trans, transform)

        elif (input[i] == 'x'):
            #create an x-axis rotation matrix, then multiply the transform matrix by the rotation matrix 
            i += 1
            angle = float(input[i])
            rotX = make_rotX(angle)
            transform = matrix_mult(rotX, transform)

        elif (input[i] == 'y'):
            #create an y-axis rotation matrix, then multiply the transform matrix by the rotation matrix 
            i += 1
            angle = float(input[i])
            rotY = make_rotY(angle)
            transform = matrix_mult(rotY, transform)

        elif (input[i] == 'z'):
            # create an z-axis rotation matrix, then multiply the transform matrix by the rotation matrix 
            i += 1
            angle = float(input[i])
            rotZ = make_rotZ(angle)
            transform = matrix_mult(rotZ, transform)

        elif (input[i] == 'a'):
            #apply the current transformation matrix to the edge matrix
            points = matrix_mult(transform, points)

        elif (input[i] == 'v'):
            #draw the lines of the point matrix to the screen, display the screen
            draw_lines(points, screen, color)
            display(screen)
            clear_screen(screen)

        elif (input[i] == 'g'):
            #draw the lines of the point matrix to the screen/frame save the screen/frame to a file
            draw_lines(points, screen, color)
            display(screen)
            #save_ppm(screen, "pic.ppm")
        i += 1

#points is our list of points to perform on
points = []
transform = new_matrix()
parse_file( 'script_c', points, transform )
points = []
transform = new_matrix()
parse_file( 'script_t', points, transform )
