def calculate_normal( ax, ay, az, bx, by, bz ):
    nx = ax*bz - az*by
    ny = az*bx - ax*bz
    nz = ax*by - ay*bx
    normal = [nx,ny,nz]
    return normal

#what is this supposed to return?
def calculate_dot( points, i ):
    dot = 0    
    return dot
