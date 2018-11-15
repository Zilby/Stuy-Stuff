from matrix import *
from gmath import *
from script import *
from display import *
#from random import randint


def get_illumination(p0, p1, p2, point = False):

    if point:#phong
        pass
    else:#flat
        point = []
        point.append((p0[0]+p1[0]+p2[0])/3.0)
        point.append((p0[1]+p1[1]+p2[1])/3.0)
        point.append((p0[2]+p1[2]+p2[2])/3.0)

    Ia = ambient()
    Id = diffuse(point, p0, p1, p2)
    Is = specular(point, p0, p1, p2)
    
    illumination = []

    illumination.append(Ia[0]+Id[0]+Is[0])
    illumination.append(Ia[1]+Id[1]+Is[1])
    illumination.append(Ia[2]+Id[2]+Is[2])
    for i in range(len(illumination)):
        illumination[i] = int(illumination[i] + .5)
        if illumination[i] > 255:
            illumination[i] = 255
    return illumination
    #return [randint(0,255),randint(0,255),randint(0,255)]

def ambient():
    return AMBIENT_LIGHT

def diffuse(point, p0, p1, p2):
    Id = [0,0,0]
    ax = p1[0] - p0[0]
    ay = p1[1] - p0[1]
    az = p1[2] - p0[2]
    bx = p0[0] - p2[0]
    by = p0[1] - p2[1]
    bz = p0[2] - p2[2]
    N = normalize_vector(calculate_normal(ax, ay, az, bx, by, bz))
    for light in LIGHTS:
        L = normalize_vector([light[0]-point[0],light[1]-point[1],light[2]-point[2]])
        dot = L[0]*N[0] +L[1]*N[1] + L[2]*N[2]
        if dot > 0:
            Id[0] += dot*light[3]
            Id[1] += dot*light[4]
            Id[2] += dot*light[5]
    Id[0] *= DIFFUSE_LIGHT[0]
    Id[1] *= DIFFUSE_LIGHT[1]
    Id[2] *= DIFFUSE_LIGHT[2]
    return Id

def specular(point, p0, p1, p2):
    Is = [0,0,0]
    ax = p1[0] - p0[0]
    ay = p1[1] - p0[1]
    az = p1[2] - p0[2]
    bx = p0[0] - p2[0]
    by = p0[1] - p2[1]
    bz = p0[2] - p2[2]
    N = normalize_vector(calculate_normal(ax, ay, az, bx, by, bz))
    for light in LIGHTS:# 2N-L dot view move to gmath
        L = normalize_vector([light[0]-point[0],light[1]-point[1],light[2]-point[2]])
        if N[0] * L[0] + N[1] * L[1] + N[2] * L[2] > 0:
            R = [0,0,0]
            R[0] = 2*N[0] - L[0]
            R[1] = 2*N[1] - L[1]
            R[2] = 2*N[2] - L[2]
            dot = R[0]*CAMERA[0] +R[1]*CAMERA[1] + R[2]*CAMERA[2]
            if dot > 0:
                dot = dot**SPECULAR_CONSTANT
                Is[0] += dot*light[3]
                Is[1] += dot*light[4]
                Is[2] += dot*light[5]
    Is[0] *= SPECULAR_LIGHT[0]
    Is[1] *= SPECULAR_LIGHT[1]
    Is[2] *= SPECULAR_LIGHT[2]
    return Is
