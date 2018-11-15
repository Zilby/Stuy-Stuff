from display import *
from draw import *
import math
import sys

XRES = 500
YRES = 500
DEFAULT_EDGE_COLOR = [255,255,255]

path = sys.argv[1]

print "rendering "+path+"..." 

f = open(path,"r")
s = f.read()
f.close

l = s.split("\n")

matrix = []

for i in xrange(len(l)):
	if l[i] == "l":
		print "adding edge..."
		parameters = map(float,l[i+1].split())
		add_edge(matrix, parameters[:len(parameters)/2], parameters[len(parameters)/2:], DEFAULT_EDGE_COLOR)
	
	elif l[i] == "s":
		print "dilating..."
		dilate(matrix, map(float,l[i+1].split()))

	elif l[i] == "t":
		print "translating..."
		translate(matrix, map(float,l[i+1].split()))
	
	elif l[i] == "x":
		print "rotating about x..."
		rotate(matrix,3,[0,0,float(l[i+1])])
	
	elif l[i] == "y":
		print "rotating about y..."
		rotate(matrix,3,[0,float(l[i+1]),0])
	
	elif l[i] == "z":
		print "rotating about z..."
		rotate(matrix,3,[float(l[i+1]),0,0])

	elif l[i] == "v":
		print "plotting..."
		screen = new_screen(XRES,YRES)
		plot(matrix,screen)
		print "saving..."
		save_ppm(screen, "img.ppm")
	
	elif l[i] == "g":
		print "plotting..."
		screen = new_screen(XRES,YRES)
		plot(matrix,screen)
		print "saving..."
		save_ppm(screen, l[i+1])

	elif l[i] == "c":
		print "adding circle..."
		parameters = map(float,l[i+1].split())
		edges = []
		add_hyperspherical_graph(edges, 2, lambda r: parameters[2], 64, DEFAULT_EDGE_COLOR)
		matrix.extend(map(lambda i: [i[0]]+[i[1]+parameters[0]-XRES/2.0]+[i[2]+parameters[1]-YRES/2.0]+i[3:],edges))

	elif l[i] == "h":
		print "adding hermite curve..."
		parameters = map(float,l[i+1].split())
		add_hermite_curve(matrix,parameters[0]-XRES/2.0,parameters[1]-YRES/2.0,parameters[4]-XRES/2.0,parameters[5]-YRES/2.0,
						  parameters[2]-parameters[0],parameters[3]-parameters[1],parameters[6]-parameters[4],parameters[7]-parameters[5],
						  64,DEFAULT_EDGE_COLOR)

	elif l[i] == "b":
		print "adding bezier curve..."
		parameters = map(float,l[i+1].split())
		add_bezier_object(matrix,[[[parameters[0]-XRES/2.0,parameters[1]-YRES/2.0]], 
								  [[parameters[2]-XRES/2.0,parameters[3]-YRES/2.0]], 
								  [[parameters[4]-XRES/2.0,parameters[5]-YRES/2.0]]],64,DEFAULT_EDGE_COLOR)
