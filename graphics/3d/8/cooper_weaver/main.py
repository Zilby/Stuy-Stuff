from display import *
from draw import *
from parser import *
screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []


points = []
transform = new_matrix()

parse_file("script", points, transform)