from matrix import *
from display import *


def addBox(points, x0, y0, z0, h, w, d):
    add_edge(points, x0, y0, z0, x0, y0, z0)
    add_edge(points, x0, y0 - h, z0, x0, y0 - h, z0)
    add_edge(points, x0, y0, z0 - d, x0, y0, z0 - d)
    add_edge(points, x0, y0 - h, z0 - d, x0, y0 - h, z0 - d)
    add_edge(points, x0 + w, y0 - h, z0, x0 + w, y0 - h, z0)
    add_edge(points, x0 + w, y0 - h, z0 - d, x0 + w, y0 - h, z0 - d)
    add_edge(points, x0 + w, y0, z0, x0 + w, y0, z0)
    add_edge(points, x0 + w, y0, z0 - d, x0 + w, y0, z0 - d)


def addSphere(points, cx, cy, r, step):
    p = 0
    while (p <= 1.000001):
        c = 0
        while (c <= 1.00001):
            x = r * math.cos(2 * math.pi * c) + cx
            y = r * math.sin(2 * math.pi * c) * math.cos(math.pi * p) + cy
            z = r * math.sin(2 * math.pi * c) * math.sin(math.pi * p)
            add_edge(points, x, y, z, x, y, z)
            c += step
        p += step


def addTorus(points, cx, cy, r1, r2, step):
    p = 0
    while (p <= 1.000001):
        c = 0
        while (c <= 1.000001):
            x = math.cos(2 * math.pi * p) * ((r1 * math.cos(2 * math.pi * c)) + r2) + cx
            y = (r1 * math.sin(2 * math.pi * c)) + cy
            z = math.sin(2 * math.pi * p) * ((r1 * math.cos(2 * math.pi * c)) + r2)
            add_edge( points, x, y, z, x, y, z)
            c += step
        p += step


def addCircle(points, cx, cy, cz, r, step):
    x0 = cx + r
    y0 = cy
    z0 = cz
    t = 0
    while (t <= 1.01):
        x1 = r * math.cos(2 * math.pi * t) + cx
        y1 = r * math.sin(2 * math.pi * t) + cy
        z1 = cz
        add_edge(points, x0, y0, z0, x1, y1, z1)
        x0 = x1
        y0 = y1
        z0 = z1
        t += step


def generatePoint(t, coef):
    coef = coef[0]
    return (coef[3]) + t * (coef[2] + t * (coef[1] + t * (coef[0])))


def addCurve(points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type):
    if curve_type == "bezier":
        addBezierCurve(points, x0, y0, x1, y1, x2, y2, x3, y3, step)
    elif curve_type == "hermite":
        addHermiteCurve(points, x0, y0, x1, y1, x2, y2, x3, y3, step)
    else:
        print "Bad curve type"


def addBezierCurve(points, x0, y0, x1, y1, x2, y2, x3, y3, step):
    t = 0
    x_coef = generateCurveCoefs(x0, x1, x2, x3, "bezier")
    y_coef = generateCurveCoefs(y0, y1, y2, y3, "bezier")
    while (t <= 1.000001):
        x = generatePoint(t, x_coef)
        y = generatePoint(t, y_coef)
        add_edge( points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step


def addHermiteCurve(points, x0, y0, x1, y1, x2, y2, x3, y3, step):
    t = 0
    dx0 = x1 - x0
    dx1 = x3 - x2
    dy0 = y1 - y0
    dy1 = y3 - y2
    x_coef = generateCurveCoefs(x0, x2, dx0, dx1, "hermite")
    y_coef = generateCurveCoefs(y0, y2, dy0, dy1, "hermite")
    while (t <= 1.000001):
        x = generatePoint(t, x_coef)
        y = generatePoint(t, y_coef)
        add_edge( points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t += step

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
