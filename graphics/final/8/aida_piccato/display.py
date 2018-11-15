from subprocess import Popen, PIPE
from os import remove
import sys
#constants
XRES = 500
YRES = 500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]
def new_screen( width = XRES, height = YRES ):
    screen = []
    for y in range( height ):
        row = []
        screen.append( row )
        for x in range( width ):
            screen[y].append( DEFAULT_COLOR[:] )
    return screen

def new_z_buffer( width = XRES, height = YRES):
    zbuffer = []
    for y in range(height):
        row = []
        zbuffer.append(row)
        for x in range(width):
            zbuffer[y].append(-sys.maxint)
    return zbuffer

zbuffer = new_z_buffer()
def plot( screen, color, x, y, z):
    global zbuffer
    x = int(x)
    y = int(y)
    z = int(z)
    newy = YRES - 1 - y
    
    if ( z > zbuffer[x][newy]):
        if(x >= 0 and x < XRES and newy >= 0 and newy < YRES  ):
            #print "DRAWN", z, zbuffer[x][newy]
            screen[x][newy] = color[:]
            zbuffer[x][newy] = z

    # else:
    #     print z, zbuffer[x][newy]



def clear_screen( screen ):
    for y in range( len(screen) ):
        for x in range( len(screen[y]) ):
            screen[x][y] = DEFAULT_COLOR[:]

def save_ppm( screen, fname ):
    f = open( fname, 'w' )
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

def save_extension( screen, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screen ):
    ppm_name = 'pic.ppm'
    save_ppm( screen, ppm_name )
    Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )


