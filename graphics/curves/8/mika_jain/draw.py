from display import *
import math
import itertools
import inspect

def add_edge(matrix,l0,l1,color):
	matrix.append([color]+l0)
	matrix.append([color]+l1)

def add_point(matrix,l,color):
	matrix.append([color]+l)
	matrix.append([color]+l)

def add_hypercube(matrix,x,d,color):
    vertices = []
    for i in xrange(d+1):
        l = map(list,list(itertools.permutations([-x/2.0]*i+[x/2.0]*(d-i))))
        l = map(str,l)
        vertices += map(lambda i:map(lambda j:float(j),i.replace("[","").replace("]","").split(",")),list(set(l)))
    for i in vertices:
        for j in xrange(len(i)):
            i2 = i[:j] + [-1*i[j]] + i[j+1:]  
            add_edge(matrix, i, i2, color)

def add_hyperspherical_graph(matrix,n,r,detail,color):
    sphcoords = []
    for l in itertools.product(xrange(int(detail+1+0.5)),repeat=n-2):
        for i in xrange(int(detail*2+1+0.5)):
            sphcoords.append(list(l)+[i,0])
    sphlines = []
    for m in xrange(len(sphcoords)):
        for j in sphcoords[m:]:
            d = map(lambda i: i[1]-i[0], zip(sphcoords[m],j))
            if d.count(0) == n-1 and (d.count(1) == 1 or d.count(-1) == 1):
                sphlines += [sphcoords[m],j]
    narg = len(inspect.getargspec(r).args[0])
    lines = []
    for i in sphlines:
        cartcoord = []
        radius = r(tuple([t*math.pi/detail for t in i[0:narg]]))
        for j in range(n+1)[1:]:
            coord = radius
            for k in xrange(j):
                if k < j-1:
                    coord *= math.sin(i[k]*math.pi/detail)
                else:
                    coord *= math.cos(i[k]*math.pi/detail)
            cartcoord.append(int(coord))
        lines += [cartcoord]
    lines = remove_close_sublist_pairs(lines,0.5) #previous value: 2
    lines = remove_points(lines,0.5) #previous value: 1
    lines = map(lambda i: [color]+i, lines)
    matrix.extend(lines)

def add_hermite_curve(matrix,x0,y0,x1,y1,dx0,dy0,dx1,dy1,detail,color):
    detail = int(detail+0.5)
    matrix.append([color,x0,y0])
    for i in xrange(detail-1):
        t = 1.0/detail*(i+1)
        h1 = 2*math.pow(t,3)-3*math.pow(t,2)+1
        h2 = -2*math.pow(t,3)+3*math.pow(t,2)
        h3 = math.pow(t,3)-2*math.pow(t,2)+t
        h4 = math.pow(t,3)-math.pow(t,2)
        x = h1*x0+h2*x1+h3*dx0+h4*dx1
        y = h1*y0+h2*y1+h3*dy0+h4*dy1
        matrix.append([color,x,y])
        matrix.append([color,x,y])
    matrix.append([color,x1,y1])

def add_bezier_object(matrix,l,detail,color):
    detail = int(detail+0.5)
    previous = map(lambda p: [color]+p, l[0])
    if len(previous) > 1:
        matrix.extend(previous)
    for i in xrange(detail-1):
        t = 1.0/detail*(i+1)
        object = map(lambda p: [color]+p, bezier_parametric(l,t))
        matrix.extend(list(reduce(lambda x,y:x+y,zip(*[previous]+[object]))))
        if len(object) > 1:
            matrix.extend(object)
        previous = object
    object = map(lambda p: [color]+p, l[-1])
    matrix.extend(list(reduce(lambda x,y:x+y,zip(*[previous]+[object]))))
    if len(object) > 1:
        matrix.extend(object)
    
def bezier_parametric(l,t):
    if len(l) == 2:
        object = []
        for i in xrange(min(len(l[0]),len(l[1]))):
            point = []
            for j in xrange(min(len(l[0][i]),len(l[1][i]))):
                point.append(l[0][i][j]*(1-t)+l[1][i][j]*t)
            object.append(point)
        return object
    else:
        l2 = []
        for obj in xrange(len(l)-1):
            object = []
            for i in xrange(min(len(l[obj]),len(l[obj+1]))):
                point = []
                for j in xrange(min(len(l[obj][i]),len(l[obj+1][i]))):
                    point.append(l[obj][i][j]*(1-t)+l[obj+1][i][j]*t)
                object.append(point)
            l2.append(object)
        return bezier_parametric(l2,t)

#===================================================================================================
#===================================================================================================

hyperspective = []

def dilate(matrix,l):
    for i in xrange(len(matrix)):
        for j in xrange(min(len(matrix[i])-1,len(l))):
            matrix[i][j+1] *= l[j]

def translate(matrix,l):
    for i in xrange(len(matrix)):
        for j in xrange(min(len(matrix[i])-1,len(l))):
            matrix[i][j+1] += l[j]

def apply_hyperspective(l):
    global hyperspective
    hyperspective = l

def project(l):
    hyperspective_scale_factor = 1
    for i in xrange(min(len(hyperspective),len(l))):
        hyperspective_scale_factor *= math.pow(hyperspective[i],math.copysign(math.pow(l[i],2),l[i]))
    return [l[0]*hyperspective_scale_factor,l[1]*hyperspective_scale_factor]

def rotate_about_axis(a,b,dtheta):
    a*=1.0
    b*=1.0
    if a > 0:
        newTheta = (math.atan(b/a)+dtheta)%(2*math.pi)
    if a < 0:
        newTheta = (math.pi+math.atan(b/a)+dtheta)%(2*math.pi)
    if a == 0 and b > 0:
        newTheta = (math.pi/2+dtheta)%(2*math.pi)
    if a == 0 and b < 0:
        newTheta = (3*math.pi/2+dtheta)%(2*math.pi)
    if a == 0 and b == 0:
        newTheta = 0
    mag = math.sqrt(a*a+b*b)    
    newA = mag * math.cos(newTheta)
    newB = mag * math.sin(newTheta)
    return [newA,newB]

def rotate(matrix,n,l): #need to map
    for point in matrix:
        i = 0
        a = 0
        if len(point)-1 < n:
            point += [0]*(n-len(point)+1)
        while i < n:
            j = i+1
            while j < n:
                if a < len(l):
                    l2 = rotate_about_axis(point[i+1],point[j+1],l[a]*math.pi/180)
                    point[i+1] = l2[0]
                    point[j+1] = l2[1]            
                a+=1
                j+=1
            i+=1

#===================================================================================================
#===================================================================================================

def plot(matrix,screen):
    i = 0
    while i < len(matrix):
        if matrix[i] == matrix[i+1]:
            point = project(matrix[i][1:])
            plot_point(screen, matrix[i][0], point[0], point[1])
        else:
            point0 = project(matrix[i][1:])
            point1 = project(matrix[i+1][1:])
            plot_line(screen, matrix[i][0], point0[0], point0[1], point1[0], point1[1])
        i += 2

def plot_point(screen,color,x,y):
    x = int(len(screen[0])/2 + x + 0.5)
    y = int(len(screen)/2 - y + 0.5)
    if ( x >= 0 and x < len(screen[0]) and y >= 0 and y < len(screen)):
        screen[y][x] = color[:]

def plot_line(screen,color,x0,y0,x1,y1):
    if y1-y0 > x1-x0 >= 0:
        octant = 2
        x0,y0=y0,x0
        x1,y1=y1,x1
    elif y1-y0 > abs(x1-x0) and x1-x0 < 0:
        octant = 3
        x0,y0=y0,-x0
        x1,y1=y1,-x1
    elif abs(x1-x0) >= y1-y0 > 0 and x1-x0 < 0:
        octant = 4
        x0,y0=-x0,y0
        x1,y1=-x1,y1
    elif abs(x1-x0) > abs(y1-y0) and x1-x0 < 0 and y1-y0 <= 0:
        octant = 5
        x0,y0=-x0,-y0
        x1,y1=-x1,-y1
    elif abs(y1-y0) >= abs(x1-x0) and x1-x0 < 0 and y1-y0 < 0:
        octant = 6
        x0,y0=-y0,-x0
        x1,y1=-y1,-x1
    elif abs(y1-y0) > abs(x1-x0) and x1-x0 >= 0 and y1-y0 < 0:
        octant = 7
        x0,y0=-y0,x0
        x1,y1=-y1,x1
    elif abs(x1-x0) >= abs(y1-y0) and x1-x0 > 0 and y1-y0 < 0:
        octant = 8
        x0,y0=x0,-y0
        x1,y1=x1,-y1
    else:
        octant = 1
        x = x0
        y = y0
    x = x0
    y = y0
    a = 2*(y1-y0)     
    b = 2*(x0-x1)       
    d = a + 0.5*b       
    while x <= x1:
        if octant == 2:
            plot_point( screen, color, y, x )
        elif octant == 3:
            plot_point( screen, color, -y, x )
        elif octant == 4:
            plot_point( screen, color, -x, y )
        elif octant == 5:
            plot_point( screen, color, -x, -y )
        elif octant == 6:
            plot_point( screen, color, -y, -x )
        elif octant == 7:
            plot_point( screen, color, y, -x )
        elif octant == 8:
            plot_point( screen, color, x, -y )
        else:
            plot_point( screen, color, x, y )
        if d>0:
            y+=1
            d+=b
        x+=1
        d+=a

#===================================================================================================
#===================================================================================================

def remove_close_sublist_pairs(l,e):
    l = map(lambda i: l[i*2:i*2+2], xrange(len(l)/2))
    ret = []
    prev = []
    for i in l:
        add = True
        for j in prev:
            if sum(map(lambda k: abs(k[1]-k[0]),zip(i[0]+i[1],j[0]+j[1]))) <= e or sum(map(lambda k: abs(k[1]-k[0]),zip(i[1]+i[0],j[0]+j[1]))) <= e:
                add *= False
        if add:
            ret += i
            prev += [i]
    return ret

def remove_points(l,e):
    ret = []
    for i in xrange(len(l)/2):
        if sum(map(lambda j: abs(j[1]-j[0]), zip(l[i*2],l[i*2+1]))) > e:
            ret.extend([l[i*2],l[i*2+1]])
    return ret
