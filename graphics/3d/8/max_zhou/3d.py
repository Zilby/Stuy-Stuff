import math
from rgpoints import *
import line
import matrix

def add_sphere(cx, cy, r, color=WHITE):
    step = 5
    p = 0
    c = 0
    while p <= 100:
        while c <= 100:
            x = r * math.cos(math.pi* 1/50 * t) + cx
            y = r * math.sin(math.pi* 1/50 * t) * math.cos(math.pi * 1/100 * t)+cy
            z = r * math.sin(math.pi* 1/50 * t) * math.sin(math.pi * 1/100 * t)+cy
            matrix.pt_matrix.append(Point(x, y, z, color))
            c+=step
        p+=step
