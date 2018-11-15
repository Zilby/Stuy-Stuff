import math
import sys
from display import plot
from matrix import generate_curve_coefs

EPSILON = sys.float_info.epsilon


def add_circle(points, cx, cy, cz, r, step):
    x0 = cx + r
    y0 = cy
    z0 = cz
    t = 0
    while (t <= 1 + EPSILON * 10):
        x1 = r * math.cos(2 * math.pi * t) + cx
        y1 = r * math.sin(2 * math.pi * t) + cy
        z1 = cz
        add_edge(points, x0, y0, z0, x1, y1, z1)
        x0 = x1
        y0 = y1
        z0 = z1
        t += step


def add_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    if curve_type == "bezier":
        add_bezier_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step)
    elif curve_type == "hermite":
        add_hermite_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step)
    else:
        print "Bad curve type"


def add_bezier_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step):
    t = 0
    x_coef = generate_curve_coefs(x0, x3, x1, x2, "bezier")
    y_coef = generate_curve_coefs(y0, y3, y1, y2, "bezier")
    x_next = x0
    y_next = y0
    while (t <= 1 + EPSILON * 10):
        x_prev = x_next
        x_next = next_point(t, x_coef)
        y_prev = y_next
        y_next = next_point(t, y_coef)
        add_edge(points, x_prev, y_prev, 0, x_next, y_next, 0)
        t += step


def add_hermite_curve(points, x0, y0, x1, y1, x2, y2, x3, y3, step):
    t = 0
    dxi = x1 - x0
    dyi = y1 - y0
    dxf = x3 - x2
    dyf = y3 - y2
    x_coef = generate_curve_coefs(x0, x2, dxi, dxf, "hermite")
    y_coef = generate_curve_coefs(y0, y2, dyi, dyf, "hermite")
    x_next = x0
    y_next = y0
    while (t <= 1 + EPSILON * 10):
        x_prev = x_next
        x_next = next_point(t, x_coef)
        y_prev = y_next
        y_next = next_point(t, y_coef)
        add_edge(points, x_prev, y_prev, 0, x_next, y_next, 0)
        t += step


def next_point(t, coeff):
    return coeff[0][0] * math.pow(t, 3) + \
        coeff[0][1] * math.pow(t, 2) + \
        coeff[0][2] * t + \
        coeff[0][3]


def draw_lines(matrix, screen, color):
    if len(matrix) < 2:
        print "Need at least 2 points to draw a line"

    p = 0
    while p < len(matrix) - 1:
        draw_line(screen, matrix[p][0], matrix[p][1],
                  matrix[p+1][0], matrix[p+1][1], color)
        p += 2


def add_edge(matrix, x0, y0, z0, x1, y1, z1):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)


def add_point(matrix, x, y, z=0):
    matrix.append([x, y, z, 1])


def draw_line(screen, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0

    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp

    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx
