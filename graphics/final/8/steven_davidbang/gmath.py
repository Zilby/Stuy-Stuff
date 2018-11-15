def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def z_normal(p0, p1, p2):
    a = [p1[0]-p0[0], p1[1]-p0[1], p1[2]-p0[2]]
    b = [p2[0]-p0[0], p2[1]-p0[1], p2[2]-p0[2]]
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def calculate_dot( points, i ):
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
    vx = 0
    vy = 0
    vz = -1
    
    #calculate the dot product
    dot = normal[0] * vx + normal[1] * vy + normal[2] * vz
    
    return dot
