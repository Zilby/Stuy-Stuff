def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def calculate_normal_pts( points, i ):
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[ i ][0] - points[ i + 2 ][0]
    by = points[ i ][1] - points[ i + 2 ][1]
    bz = points[ i ][2] - points[ i + 2 ][2]
    
    normal = calculate_normal( ax, ay, az, bx, by, bz )
    return normal

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

def dot_product_light( normal, l ):
    #normalize the surface normal
    mag = ( (normal[0] * normal[0]) + 
            (normal[1] * normal[1]) + 
            (normal[2] * normal[2]) ) ** 0.5
    
    if mag == 0:
        return 0
    
    normal[0] = normal[0] / mag
    normal[1] = normal[1] / mag
    normal[2] = normal[2] / mag
    
    print "Normal: " + str(normal)
    dot = normal[0] * l[0] + normal[1] * l[1] + normal[2] * l[2]
    return dot
