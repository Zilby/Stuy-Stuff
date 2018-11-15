from subprocess import Popen, PIPE
from os import remove

#constants
XRES = 500
YRES = 500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2
MININT = 9223372036854775807

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> origin/master
ZBUFFER = []

DEFAULT_COLOR = [0, 0, 0]

def new_screen( width = XRES, height = YRES ):
<<<<<<< HEAD
=======
=======

ZBUFFER = []
LIGHTS = []
CAMERA = [0, 0, -1]
DEFAULT_COLOR = [0, 0, 0]
AMBIENT_LIGHT = [63, 63, 63]
DIFFUSE_LIGHT = [1, 1, 1]
SPECULAR_LIGHT = [0, 0, 0]
SPECULAR_CONSTANT = 8

def new_screen(width = XRES, height = YRES):
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    screen = []
    for y in range(height):
        row1 = []
        row2 = []
        screen.append(row1)
        ZBUFFER.append(row2)
        for x in range(width):
            screen[y].append(DEFAULT_COLOR[:])
            ZBUFFER[y].append(MININT)
    return screen

def plot(screen, color, x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    if ( x >= 0 and x < XRES and y >= 0 and y < YRES and z <= ZBUFFER[x][y]):
        screen[x][y] = color[:]
        ZBUFFER[x][y] = z

def clear_screen(screen):
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
    while len(LIGHTS) > 0:
        LIGHTS.pop()
    CAMERA[0], CAMERA[1], CAMERA[2] = 0,0,-1
    AMBIENT_LIGHT[0], AMBIENT_LIGHT[1], AMBIENT_LIGHT[2] = 127,127,127
    DIFFUSE_LIGHT[0], DIFFUSE_LIGHT[1], DIFFUSE_LIGHT[2] = 1,1,1
    SPECULAR_LIGHT[0], SPECULAR_LIGHT[1], SPECULAR_LIGHT[2] = 0,0,0
    SPECULAR_CONSTANT = 8
    
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    for y in range(len(screen)):
        for x in range(len(screen[y])):
            screen[x][y] = DEFAULT_COLOR[:]
            ZBUFFER[x][y] = MININT

def save_ppm(screen, fname):
    f = open(fname, 'w')
    ppm = 'P3\n' + str(len(screen[0])) +' '+ str(len(screen)) +' '+ str(MAX_COLOR) +'\n'
    for y in range( len(screen) ):
        row = ''
        for x in range( len(screen[y]) ):
            pixel = screen[x][y]
            row+= str( pixel[ RED ] ) + ' '
            row+= str( pixel[ GREEN ] ) + ' '
            row+= str( pixel[ BLUE ] ) + ' '
        ppm+= row + '\n'
    f.write( ppm )
    f.close()

def save_extension(screen, fname):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display(screen):
    ppm_name = 'pic.ppm'
    save_ppm( screen, ppm_name )
    Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )


