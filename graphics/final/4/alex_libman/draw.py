from display import *
from matrix import *
import math

#Go through matrix 2 entries at a time and call
#draw_line on each pair of points
def draw_lines( matrix, screen, color):
    zbuffer = []
    for i in range(YRES):
        pixelRow = []
        for j in range(XRES):
            pixelRow.append(-maxint - 1)
        zbuffer.append(pixelRow)
    for i in range(len(matrix))[::2]:
        draw_line(screen,matrix[i][0],matrix[i][1],matrix[i][2],matrix[i+1][0],matrix[i+1][1],matrix[i+1][2],color,zbuffer)
        
#Add the edge (x0, y0, z0) - (x1, y1, z1) to matrix
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    
#Add the point (x, y, z) to matrix
def add_point( matrix, x, y, z=0 ):
    matrix.append([int(x),int(y),int(z),1])

def add_polygon(matrix, x0, y0, z0, x1, y1, z1, x2, y2, z2):
    add_point(matrix,x0,y0,z0)
    add_point(matrix,x1,y1,z1)
    add_point(matrix,x2,y2,z2)

def draw_polygons(matrix, screen, color, zbuffer, ambient_light, diffuse_light, spec_light):
    #colors = [[255,0,0],[0,255,0],[0,0,255],[122,122,34],[135,8,200],[0,122,122],[122,0,122],[0,122,122]]
    #g = 0
    for i in range(len(matrix))[::3]:
        #color = colors[g]
        if dotProductFace(matrix, i) >= 0:
            color = getColor(matrix[i:i+3], ambient_light, diffuse_light, spec_light)
            draw_line(screen,
                      matrix[i][0], matrix[i][1], matrix[i][2],
                      matrix[i+1][0], matrix[i+1][1], matrix[i+1][2],
                      color, zbuffer)
            draw_line(screen,
                      matrix[i+1][0], matrix[i+1][1], matrix[i+1][2],
                      matrix[i+2][0], matrix[i+2][1], matrix[i+2][2],
                      color, zbuffer)
            draw_line(screen,
                      matrix[i+2][0], matrix[i+2][1], matrix[i+2][2],
                      matrix[i][0], matrix[i][1], matrix[i][2],
                      color, zbuffer)
            scanline_convert(screen,
                             matrix[i][0], matrix[i][1], matrix[i][2],
                             matrix[i+1][0], matrix[i+1][1], matrix[i+1][2],
                             matrix[i+2][0], matrix[i+2][1], matrix[i+2][2],
                             color, zbuffer)
        #g += 1
        #if g >= len(colors):
        #    g = 0

def scanline_convert(screen, x1, y1, z1, x2, y2, z2, x3, y3, z3, color, zbuffer):
    if y2 > y1:
        if y3 > y2:
            bottomX = x1
            bottomY = y1
            bottomZ = z1
            middleX = x2
            middleY = y2
            middleZ = z2
            topX = x3
            topY = y3
            topZ = z3
        elif y3 > y1:
            bottomX = x1
            bottomY = y1
            bottomZ = z1
            middleX = x3
            middleY = y3
            middleZ = z3
            topX = x2
            topY = y2
            topZ = z2
        else:
            bottomX = x3
            bottomY = y3
            bottomZ = z3
            middleX = x1
            middleY = y1
            middleZ = z1
            topX = x2
            topY = y2
            topZ = z2
    else:
        if y3 > y1:
            bottomX = x2
            bottomY = y2
            bottomZ = z2
            middleX = x1
            middleY = y1
            middleZ = z1
            topX = x3
            topY = y3
            topZ = z3
        elif y3 > y2:
            bottomX = x2
            bottomY = y2
            bottomZ = z2
            middleX = x3
            middleY = y3
            middleZ = z3
            topX = x1
            topY = y1
            topZ = z1
        else:
            bottomX = x3
            bottomY = y3
            bottomZ = z3
            middleX = x2
            middleY = y2
            middleZ = z2
            topX = x1
            topY = y1
            topZ = z1
    i = bottomY + 1
    while i < middleY:
        x1 = bottomX + float(topX - bottomX) / (topY - bottomY) * (i - bottomY)
        x2 = bottomX + float(middleX - bottomX) / (middleY - bottomY) * (i - bottomY)
        x1 = round(x1)
        x2 = round(x2)
        z1 = bottomZ + float(topZ - bottomZ) / (topY - bottomY) * (i - bottomY)
        z2 = bottomZ + float(middleZ - bottomZ) / (middleY - bottomY) * (i - bottomY)
        draw_line(screen, x1, i, z1, x2, i, z2, color, zbuffer)
        i += 1
    while i < topY:
        x1 = bottomX + float(topX - bottomX) / (topY - bottomY) * (i - bottomY)
        x2 = middleX + float(topX - middleX) / (topY - middleY) * (i - middleY)
        x1 = round(x1)
        x2 = round(x2)
        z1 = bottomZ + float(topZ - bottomZ) / (topY - bottomY) * (i - bottomY)
        z2 = middleZ + float(topZ - middleZ) / (topY - middleY) * (i - middleY)
        draw_line(screen, x1, i, z1, x2, i, z2, color, zbuffer)
        i += 1

# Flat Shading
def getColor(polygon, ambient_light, diffuse_light, spec_light):
    #ambient lighting
    I_r = ambient_light[0]
    I_g = ambient_light[1]
    I_b = ambient_light[2]
    #diffuse lighting
    for light in diffuse_light:
        color_r = light[0][0]
        color_g = light[0][1]
        color_b = light[0][2]
        diffuse_multiplier = dotProductFace(polygon, 0, light[1])
        if diffuse_multiplier > 0:
            I_r += color_r * diffuse_multiplier
            I_g += color_g * diffuse_multiplier
            I_b += color_b * diffuse_multiplier
    for light in spec_light:
        color_r = light[0][0]
        color_g = light[0][1]
        color_b = light[0][2]
        faceNorm = getNormal(polygon)
        firstDot = dotProduct(faceNorm, light[1])
        scalar_mult([faceNorm], 2 * firstDot)
        faceNorm[0] -= light[1][0]
        faceNorm[1] -= light[1][1]
        faceNorm[2] -= light[1][2]
        spec_multiplier = dotProduct(faceNorm, [0, 0, -1])
        if spec_multiplier > 0:
            spec_multiplier = spec_multiplier ** 8
            I_r += color_r * spec_multiplier
            I_g += color_g * spec_multiplier
            I_b += color_b * spec_multiplier
    if I_r > 255:
        I_r = 255
    if I_g > 255:
        I_g = 255
    if I_b > 255:
        I_b = 255
    return [int(I_r), int(I_g), int(I_b)]
            
def parametric(matrix, step, f, g, h = None):
    if h == None:
        h = lambda x: 0
    t = 0
    oldX = f(0)
    oldY = g(0)
    oldZ = h(0)
    while t < 1.00001:
        t += step
        x = f(t)
        y = g(t)
        z = h(t)
        add_edge(matrix, oldX, oldY, oldZ, x, y, z)
        oldX = x
        oldY = y
        oldZ = z
    
#Add circle with center (x,y,z) and radius r to matrix
def add_circle(matrix, cx, cy, cz, r, step):
    def x(t):
        return r * math.cos(2 * math.pi * t) + cx
    def y(t):
        return r * math.sin(2 * math.pi * t) + cy
    parametric(matrix, step, x, y)

def add_curve(matrix, x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3, step, curve_type):
    if curve_type == "hermite":
        h = [[2, -3, 0, 1],
             [-2, 3, 0, 0],
             [1, -2, 1, 0],
             [1, -1, 0, 0]]
        g = [[x0, x2, x1 - x0, x3 - x2],
             [y0, y2, y1 - y0, y3 - y2],
             [z0, z2, z1 - z0, z3 - z2]]
        matrix_mult(h,g)
        def x(t):
            return g[0][0] * t ** 3 + g[0][1] * t ** 2 + g[0][2] * t + g[0][3]
        def y(t):
            return g[1][0] * t ** 3 + g[1][1] * t ** 2 + g[1][2] * t + g[1][3]
        def z(t):
            return g[2][0] * t ** 3 + g[2][1] * t ** 2 + g[2][2] * t + g[2][3]
        parametric(matrix,step,x,y,z)
    elif curve_type == "bezier":
        b = [[-1, 3, -3, 1],
             [3, -6, 3, 0],
             [-3, 3, 0, 0],
             [1, 0, 0, 0]]
        g = [[x0, x1, x2, x3],
             [y0, y1, y2, y3],
             [z0, z1, z2, z3]]
        matrix_mult(b,g)
        def x(t):
            return g[0][0] * t ** 3 + g[0][1] * t ** 2 + g[0][2] * t + g[0][3]
        def y(t):
            return g[1][0] * t ** 3 + g[1][1] * t ** 2 + g[1][2] * t + g[1][3]
        def z(t):
            return g[2][0] * t ** 3 + g[2][1] * t ** 2 + g[2][2] * t + g[2][3]
        parametric(matrix,step,x,y,z)
    else:
        print "Curve type not found"

#3D shapes
def add_prism(matrix, x, y, z, width, height, depth):
    add_polygon(matrix, x, y, z, x, y - height, z, x + width, y - height, z)
    add_polygon(matrix, x, y, z, x + width, y - height, z, x + width, y, z)
    add_polygon(matrix, x, y, z, x + width, y, z, x + width, y, z + depth)
    add_polygon(matrix, x, y, z, x + width, y, z + depth, x, y, z + depth)
    add_polygon(matrix, x, y, z + depth, x, y - height, z + depth, x, y - height, z)
    add_polygon(matrix, x, y, z + depth, x, y - height, z, x, y, z)
    add_polygon(matrix, x + width, y, z, x + width, y - height, z, x + width, y - height, z + depth)
    add_polygon(matrix, x + width, y, z, x + width, y - height, z + depth, x + width, y, z + depth)
    add_polygon(matrix, x + width, y, z + depth, x + width, y - height, z + depth, x, y - height, z + depth)
    add_polygon(matrix, x + width, y, z + depth, x, y - height, z + depth, x, y, z + depth)
    add_polygon(matrix, x, y - height, z, x, y - height, z + depth, x + width, y - height, z + depth)
    add_polygon(matrix, x, y - height, z, x + width, y - height, z + depth, x + width, y - height, z)

def add_sphere(matrix, cx, cy, cz, r, step=0.05):
    j = 0
    while j < 1.00001 - step:
        k = 0
        a = j + step
        #edge case 1
        x1 = r * math.cos(math.pi * k) + cx
        y1 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * j) + cy
        z1 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * j) + cz
        x2 = r * math.cos(math.pi * (k + step)) + cx
        y2 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * a) + cy
        z2 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * a) + cz
        x3 = r * math.cos(math.pi * (k + step)) + cx
        y3 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * j) + cy
        z3 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * j) + cz
        add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
        x1 = x3
        y1 = y3
        z1 = z3
        k += step
        while k < 1.00001 - 2 * step:
            #p_i+n
            x2 = r * math.cos(math.pi * k) + cx
            y2 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
            z2 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
            k += step
            #p_i+n+1
            x3 = r * math.cos(math.pi * k) + cx
            y3 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
            z3 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
            add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
            #p_i+1
            x4 = r * math.cos(math.pi * k) + cx
            y4 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * j) + cy
            z4 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * j) + cz
            add_polygon(matrix, x1, y1, z1, x3, y3, z3, x4, y4, z4)
            #update p_i
            x1 = x4
            y1 = y4
            z1 = z4
        #edge case 2
        x2 = r * math.cos(math.pi * k) + cx
        y2 = r * math.sin(math.pi * k) * math.cos(2 * math.pi * a) + cy
        z2 = r * math.sin(math.pi * k) * math.sin(2 * math.pi * a) + cz
        x3 = r * math.cos(math.pi * (k + step)) + cx
        y3 = r * math.sin(math.pi * (k + step)) * math.cos(2 * math.pi * a) + cy
        z3 = r * math.sin(math.pi * (k + step)) * math.sin(2 * math.pi * a) + cz
        add_polygon(matrix, x1, y1, z1, x2, y2, z2, x3, y3, z3)
        j += step

def add_torus(matrix, cx, cy, cz, r1, r2, step=0.05):
    j = 0
    while j < 1.00001 - step:
        k = 0
        a = j + step
        while k < 1.00001:
            #p_i
            x1 = math.cos(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y1 = r1 * math.sin(2 * math.pi * k) + cy
            z1 = -math.sin(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cz
            #p_i+n
            x2 = math.cos(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y2 = r1 * math.sin(2 * math.pi * k) + cy
            z2 = -math.sin(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cz
            k += step
            #p_i+n+1
            x3 = math.cos(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y3 = r1 * math.sin(2 * math.pi * k) + cy
            z3 = -math.sin(2 * math.pi * a) * (r1 * math.cos(2 * math.pi * k) + r2) + cz
            #p_i+1
            x4 = math.cos(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cx
            y4 = r1 * math.sin(2 * math.pi * k) + cy
            z4 = -math.sin(2 * math.pi * j) * (r1 * math.cos(2 * math.pi * k) + r2) + cz
            add_polygon(matrix, x1, y1, z1, x3, y3, z3, x2, y2, z2)
            add_polygon(matrix, x1, y1, z1, x4, y4, z4, x3, y3, z3)
        j += step

def add_custom_shape(matrix, fileName):
    f = open(fileName, "r")
    line = f.readline()
    while line:
        if line.strip() == "outer loop":
            v1 = f.readline().split(" ")
            v2 = f.readline().split(" ")
            v3 = f.readline().split(" ")
            add_polygon(matrix,
                        float(v1[1]), float(v1[2]), float(v1[3].strip()),
                        float(v3[1]), float(v3[2]), float(v3[3].strip()),
                        float(v2[1]), float(v2[2]), float(v2[3].strip()))
        line = f.readline()
    f.close()
        
#Plot all the pixels needed to draw line (x0, y0, z0) - (x1, y1, z1)
#to screen with color
def draw_line( screen, x0, y0, z0, x1, y1, z1, color, zbuffer):
    x0 = round(x0)
    x1 = round(x1)
    y0 = round(y0)
    y1 = round(y1)
    z0 = z0
    z1 = z1
    if (x1 >= x0):
        x = x0
        y = y0
        z = z0
        a = 2 * (y1 - y0)
        b = -2 * (x1 - x0)
        if x1 != x0:
            dz = float(z1 - z0) / (x1 - x0)
        elif y1 != y0:
            dz = float(z1 - z0) / (y1 - y0)
        else:
            dz = 0
        if y1 >= y0:
            if x1 - x0 >= y1 - y0:
                d = a + b/2
                while (x <= x1):
                    plot(screen, color, x, y, z, zbuffer)
                    if d > 0:
                        y += 1
                        d += b
                    x += 1
                    d += a
                    z += dz
            else:
                d = a/2 + b
                while (y <= y1):
                    plot(screen, color, x, y, z, zbuffer)
                    if d < 0:
                        x += 1
                        d += a
                    y += 1
                    d += b
                    z += dz
        else:
            if y0 - y1 <= x1 - x0:
                d = a - b/2
                while (x <= x1):
                    plot(screen, color, x, y, z, zbuffer)
                    if d < 0:
                        y -= 1
                        d -= b
                    x += 1
                    d += a
                    z += dz
            else:
                d = a/2 - b
                while (y >= y1):
                    plot(screen, color, x, y, z, zbuffer)
                    if d > 0:
                        x += 1
                        d += a
                    y -= 1
                    d -= b
                    z += dz
    else:
        draw_line(screen,x1,y1,z1,x0,y0,z0,color,zbuffer)        
