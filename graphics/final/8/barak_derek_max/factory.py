import math

# Generates certain components of the picture, instead of doing it by hand
# Prerequisite: Python 2.6+ and a little bit of faith :^)


#box parameters: x y z width depth height

#going to assume the blocks are square faced

WIDTH = 10
DEPTH = 10
HEIGHT = 40


def make_plane (radius, plane):
    for angle in range(0, 360):
        rads = angle * 3.1415926 / 180
        r0 = 0
        while r0 < radius :
            parser_str = "box "
            parser_str += (str( (r0 - WIDTH/2) * math.cos(rads) ) + " ") # x
            parser_str += (str(plane) + " ") # y
            parser_str += (str( (r0 - DEPTH/2) * math.sin(rads) ) + " ") # z
            parser_str += (str(WIDTH) + " ")
            parser_str += (str(DEPTH) + " ")
            parser_str += str(HEIGHT)
            parser_str += "\n"
            f.write(parser_str);
            r0 += radius/WIDTH


def make_quadratic_landmass ( max_radius, init_plane ):
    r = max_radius
    p = init_plane
    while r >= WIDTH:
        make_plane(r, p)
        r = math.sqrt(r)
        r -= 1
        r = math.pow(r,2)
        p -= HEIGHT
        
f = open ('final.mdl', 'w')

f.write("frames 49\n")
f.write("basename final\n")
f.write("push\n")
#make_plane(200,0)
make_quadratic_landmass( 200, 0 )
f.write("display")



f.close()
