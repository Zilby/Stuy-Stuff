from display import *
from draw import *
from matrix import *
from parser import *

points = []
transform = new_matrix()

parse_file('script_c', points, transform)
