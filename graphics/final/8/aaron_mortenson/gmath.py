<<<<<<< HEAD
def calculate_normal( ax, ay, az, bx, by, bz ):
=======
<<<<<<< HEAD
def calculate_normal( ax, ay, az, bx, by, bz ):
=======
from display import CAMERA

def normalize_vector(v):
    result = []
    mag = 0
    for component in v:
        mag += component * component
    mag = mag ** 0.5
    if mag == 0:
        return v
    for component in v:
        result.append(component / mag)
    return result

def calculate_normal(ax, ay, az, bx, by, bz):
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

<<<<<<< HEAD
def calculate_dot( points, i ):
=======
<<<<<<< HEAD
def calculate_dot( points, i ):
=======
def calculate_dot(points, i):
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[ i ][0] - points[ i + 2 ][0]
    by = points[ i ][1] - points[ i + 2 ][1]
    bz = points[ i ][2] - points[ i + 2 ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    #normalize the surface normal
    mag = ( (normal[0] * normal[0]) + 
            (normal[1] * normal[1]) + 
            (normal[2] * normal[2]) ) ** 0.5
    
    if mag == 0:
        return 0

    #normal[0] = normal[0] / mag
    #normal[1] = normal[1] / mag
    #normal[2] = normal[2] / mag

    #set up the view vector values
<<<<<<< HEAD
    vx = 0
    vy = 0
    vz = -1
=======
<<<<<<< HEAD
    vx = 0
    vy = 0
    vz = -1
=======
    vx = CAMERA[0]
    vy = CAMERA[1]
    vz = CAMERA[2]
>>>>>>> 621ec2bdaad0c76f791b80bdf528a45baea9fa85
>>>>>>> origin/master
    
    #calculate the dot product
    dot = normal[0] * vx + normal[1] * vy + normal[2] * vz
    
    return dot
