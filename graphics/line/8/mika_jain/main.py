from display import *
from draw import *

screen = new_screen(500,500)
matrix = []

for i in xrange(26):
	add_edge(matrix, [0,0], [100,4*i], [255,255,255])
	add_edge(matrix, [0,0], [4*i,100], [255,255,255])
	add_edge(matrix, [0,0], [-4*i,100], [255,255,255])
	add_edge(matrix, [0,0], [-100,4*i], [255,255,255])
	add_edge(matrix, [0,0], [-100,-4*i], [255,255,255])
	add_edge(matrix, [0,0], [-4*i,-100], [255,255,255])
	add_edge(matrix, [0,0], [4*i,-100], [255,255,255])
	add_edge(matrix, [0,0], [100,-4*i], [255,255,255])

plot(matrix,screen)
save_ppm( screen, "lines.ppm" )

# for i in xrange(36):
# 	print i
# 	screen = new_screen(3750,1000)
# 	matrix = []
# 	set_rotations([i*10]*36)
# 	set_hyperspective([1,1]+[1.001]*7)
# 	add_hypercube( matrix, 300, 3, [0, 255, 255])
# 	translate_plot(-1275 ,)
# 	plot(matrix,screen)
# 	matrix = []
# 	add_hypercube( matrix, 268, 4, [85, 170, 170])
# 	translate_plot(-425 ,)
# 	plot(matrix,screen)
# 	matrix = []
# 	add_hypercube( matrix, 243, 5, [170, 85, 85])
# 	translate_plot(425 ,)
# 	plot(matrix,screen)
# 	matrix = []
# 	add_hypercube( matrix, 180, 9, [255, 0, 0])
# 	translate_plot(1275 ,)
# 	plot(matrix,screen)
# 	save_ppm( screen, "frames/"+str(i)+".ppm" )

#NOTE: GENERALIZED HYPERDIMENSIONAL TRANFORMATION ALGORITHMS NOT IN THESE FILES 
