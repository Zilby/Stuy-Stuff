from display import *
from draw import *

screen = new_screen()
matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []

for i in range(0,500,20):
    add_edge(matrix1, XRES, YRES, 0, XRES - i, i, 0 )
    draw_lines(matrix1, screen, [255,0,0])
    
    add_edge(matrix2, 0, 0, 0, XRES - i, i, 0 )
    draw_lines(matrix2, screen, [0,255,0])

    add_edge(matrix3, 0, YRES, 0, i, i, 0 )
    draw_lines(matrix3, screen, [0,0,255])

    add_edge(matrix4, XRES, 0, 0, i, i, 0 )
    draw_lines(matrix4, screen, [255,255,0])
    
    draw_line(screen, 0, 0, XRES, YRES, [255,255,255])
    draw_line(screen, XRES, 0, 0, YRES, [255,255,255])
    draw_line(screen, XRES/2, 0, XRES/2, YRES, [255,255,255])
    draw_line(screen, 0, YRES/2, XRES, YRES/2, [255,255,255])
    
display(screen)
  
save_ppm(screen,"line.ppm")
