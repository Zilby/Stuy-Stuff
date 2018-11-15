import math

def dist(x1,y1,x2,y2):
    return math.sqrt( ((x1-x2)**2) + ((y1-y2)**2))

def add_testcylinder():
    r = ""

    #focus 1
    f1x = 250
    f1y = 150

    #focus 2
    f2x = 250
    f2y = 350

    z1 = 100 #face1
    z2 = 300 #face2

    edge = []
    d = 400 #total dist from focii

    face1a = []
    face2a = []
    face1b = []
    face2b = []
    #i_cant_do_math.jpg
    #brute_force.png
    for y in range(100):
        y = y*5
        for x in range(500):
            f1d = dist(x,y,f1x,f1y)
            f2d = dist(x,y,f2x,f2y)
            curd = f1d + f2d
            if abs(curd-d)<1:
                face1a+=[ [x,y,z1] ]
                face2a+=[ [x,y,z2] ]
                break
        for x in range(500):
            x = 500-x
            f1d = dist(x,y,f1x,f1y)
            f2d = dist(x,y,f2x,f2y)
            curd = f1d + f2d
            if abs(curd-d)<1:
                face1b+=[ [x,y,z1] ]
                face2b+=[ [x,y,z2] ]
                break

    face1b.reverse()
    face2b.reverse()
    face1 = face1a + face1b
    face2 = face2a + face2b

    for i in range(len(face1)):
        f1 = face1[i]
        f2 = face2[i]
        if i+1<len(face1):
            f1n = face1[i+1]
            f2n = face2[i+1]
        else:
            f1n = face1[0]
            f2n = face2[0]
        r+="l\n%s %s %s %s %s %s\n" % \
            (f1[0],f1[1],f1[2],f2[0],f2[1],f2[2])
        r+="l\n%s %s %s %s %s %s\n" % \
            (f1[0],f1[1],f1[2],f1n[0],f1n[1],f1n[2])
        r+="l\n%s %s %s %s %s %s\n" % \
            (f2[0],f2[1],f2[2],f2n[0],f2n[1],f2n[2])
        
    return r


ayylmao = open("ayylmao_c","w")
ayylmao.write(add_testcylinder())
s = """i
x
20
y
20
z
20
t
150 50 0
a
v
g
cylinder.png"""
ayylmao.write(s)
ayylmao.close()
