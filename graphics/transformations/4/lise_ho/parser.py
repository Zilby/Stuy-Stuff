from display import *
from matrix import *
from draw import *
'''

l: add a line to the point matrix -  takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
i: set the transform matrix to the identity matrix
s: create a scale matrix, then multiply the transform matrix by the scale matrix -  takes 3 arguments (sx, sy, sz)
t: create a translation matrix, then multiply the transform matrix by the translation matrix - takes 3 arguments (tx, ty, tz)
x: create an x-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
y: create an y-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
z: create an z-axis rotation matrix, then multiply the transform matrix by the rotation matrix - takes 1 argument (theta)
a: apply the current transformation matrix to the edge matrix
v: draw the lines of the point matrix to the screen, display the screen (not applicable for java)
g: draw the lines of the point matrix to the screen/frame save the screen/frame to a file - takes 1 argument (file name)

'''
def parse_file( fname, points, transform ):
    f = open (fname,'r')
    commands = f.read()

    #read in each line and parse and do specific transformation
    print commands
    print commands.split('\n')
    line = 0
    length = len(commands)
    while line < length:
    #six arguments all in one list
        if commands[line] == 'l':

            line = line + 2
        elif commands[line] in "stxyz":   
            #three arguments all in one list
            if commands[line] == 's':
                pass
            elif commands[line] == 't':
                pass
            elif commands[line] == 'x':
                pass
            elif commands[line] == 'y':
                pass
            elif commands[line] == 'z':
                pass
            line += 1
        #one argument-> as in one element in the list
        else:
            if commands[line] == 'i':
                pass
            elif commands[line] == 'a':
                pass
            elif commands[line] == 'v':
                pass
            elif commands[line] == 'g':
                pass
            else:
                pass
            line = line + 1

points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )


#make_rotX(30)
#make_rotY(30)
#make_rotZ(30)
