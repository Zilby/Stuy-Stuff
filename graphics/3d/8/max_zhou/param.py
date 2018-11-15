import math

import matrix
from rgbpoints import *

def add_circle(cx, cy, r, pmatrix, color=WHITE, color2=None):
    step = 2
    t = 0
    if color2 != None:
    #if 1 == 1: #default
        #color = random_color()
        #color2 = random_color()
        dred = color2[0] - color[0]
        dblue = color2[1] - color[1]
        dgreen = color2[2] - color[2]
        def colorf():
            delt = 1000
            cur = float(t) / float(delt) * 1000
             
            return [int((cur/delt) * dred + color[0]), int((cur/delt) * dblue + color[1]), int((cur/delt) * dgreen + color[2])]
    else:
        colorf = lambda: color
    x0 = r + cx
    y0 = cy
    x = r * math.cos(math.pi * 1/500 * t) + cx
    y = r * math.sin(math.pi * 1/500 * t) + cy
    while t <= 1000:
        x = r * math.cos(math.pi * 1/500 * t) + cx
        y = r * math.sin(math.pi * 1/500 * t) + cy
        matrix.add_edge(pmatrix, x0, y0, x, y, colorf())
        #print colorf()
        x0 = x
        y0 = y
        t+= step


def add_curve(x0, y0, x1, y1, x2, y2, x3, y3, pmatrix, curve, color=WHITE, color2=None):
    step = 5
    t = 0.0
    #between (x0,y0) and (x2,y2)
    if color2 != None:
    #if 1 == 1:
        #color = random_color()
        #color2 = random_color()
        dred = color2[0] - color[0]
        dblue = color2[1] - color[1]
        dgreen = color2[2] - color[2]
        def colorf():
            delt = 1000
            cur = float(t) / float(delt) * 1000
             
            return [int((cur/delt) * dred + color[0]), int((cur/delt) * dblue + color[1]), int((cur/delt) * dgreen + color[2])]
    else:
        colorf = lambda: color
        
    if curve == "HERMITE":
        hermite = [[2, -2, 1, 1],
                   [-3, 3, -2, -1],
                   [0, 0, 1, 0],
                   [1, 0, 0, 0]]
        xpoints = [[x0], [x2], [x1], [x3]]
        xabcd = matrix.m_mult(hermite, xpoints)
        xa = xabcd[0][0]
        xb = xabcd[1][0]
        xc = xabcd[2][0]
        xd = xabcd[3][0]
        ypoints = [[y0], [y2], [y1], [y3]]
        yabcd = matrix.m_mult(hermite, ypoints)
        ya = yabcd[0][0]
        yb = yabcd[1][0]
        yc = yabcd[2][0]
        yd = yabcd[3][0]
        param_x = lambda t: xa*((t/1000)**3) + xb*((t/1000)**2) + xc*(t/1000) + xd
        param_y = lambda t: ya*((t/1000)**3) + yb*((t/1000)**2) + yc*(t/1000) + yd

    if curve == "BEZIER":
        bezier = [[-1, 3, -3, 1],
                  [3, -6, 3, 0],
                  [-3, 3, 0, 0],
                  [1, 0, 0, 0]]
        xpoints = [[x0], [x1], [x2], [x3]]
        xabcd = matrix.m_mult(bezier, xpoints)
        xa = xabcd[0][0]
        xb = xabcd[1][0]
        xc = xabcd[2][0]
        xd = xabcd[3][0]
        ypoints = [[y0], [y1], [y2], [y3]]
        yabcd = matrix.m_mult(bezier, ypoints)
        ya = yabcd[0][0]
        yb = yabcd[1][0]
        yc = yabcd[2][0]
        yd = yabcd[3][0]
        param_x = lambda t: xa*((t/1000)**3) + xb*((t/1000)**2) + xc*(t/1000) + xd
        param_y = lambda t: ya*((t/1000)**3) + yb*((t/1000)**2) + yc*(t/1000) + yd
        
    while t <= 1000:
        x = param_x(t)
        y = param_y(t)
        #print x
        #print y
        matrix.add_edge(pmatrix, x0, y0, x, y, colorf())
        x0 = x
        y0 = y
        t+=step
