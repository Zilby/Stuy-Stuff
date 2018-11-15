def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def magnitude( v ):
    return ( ( v[0] * v[0] ) + ( v[1] * v[1] ) + ( v[2] * v[2] ) )**0.5

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

def calculate_light_dot( points, i, l ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[ i ][0] - points[ i + 2 ][0]
    by = points[ i ][1] - points[ i + 2 ][1]
    bz = points[ i ][2] - points[ i + 2 ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    #normalize the surface normal
    mag = magnitude( normal) * magnitude( l )
   
    if mag == 0:
        return 0

    normal[0] = normal[0] / mag
    normal[1] = normal[1] / mag
    normal[2] = normal[2] / mag

    #calculate the dot product
    dot = normal[0] * l[0] + normal[1] * l[1] + normal[2] * l[2]
    return dot

def get_norm( points, i ):
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[ i ][0] - points[ i + 2 ][0]
    by = points[ i ][1] - points[ i + 2 ][1]
    bz = points[ i ][2] - points[ i + 2 ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )
    return normal

def dot_prod( v1, v2 ):
    dot = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
    mag = magnitude( v1 ) * magnitude( v2 )
    return dot/mag
