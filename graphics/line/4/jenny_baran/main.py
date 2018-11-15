from display import *
from draw import *

screen = new_screen()

#### BLUE ####

color = [ 0, 255, 255 ]
blue_matrix = []

for x in range ( 1, YRES, 5 ):
    add_edge( blue_matrix, 0, x, 0, x, YRES - 1, 0 )

draw_lines( blue_matrix, screen, color )

#### PINK ####

color = [ 247, 36, 120 ]
pink_matrix = []

for x in range ( 1, XRES, 5 ):
    add_edge( pink_matrix, x, YRES - 1, 0, XRES - 1, YRES - x, 0 )

draw_lines( pink_matrix, screen, color )

#### PURPLE ####

color = [ 138, 43, 226 ]
purple_matrix = []

for x in range ( 1, XRES, 5 ):
    add_edge( purple_matrix, x, 0, 0, XRES - 1, x, 0 )

draw_lines( purple_matrix, screen, color )

#### GREEN ####

color = [ 128, 255, 0 ]
green_matrix = []

for x in range ( 1, XRES, 5 ):
    add_edge( green_matrix, 0, YRES - x, 0, x, 0, 0 )

draw_lines( green_matrix, screen, color )


display( screen )