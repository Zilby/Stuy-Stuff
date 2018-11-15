from draw import *

def add_curvything():
    def add_circlething(points):
        r = ""
        radius = 50
        sign = 1
        for i in range(len(points)/25):
            p = points[i*25]
            r += "c\n%s %s %s\n" % (int(p[0]),int(p[1]),50-radius)
            radius -= 2*sign
            if radius == 50 or radius == 10: sign *= -1
        return r
    r = ""
    points = []
    add_curve(points,400,120,400,600,100,380,100,900,1000,"hermite")
    r += add_circlething(points)
    points = []
    add_curve(points,50,250,250,0,250,500,450,250,1000,"bezier")
    r += add_circlething(points)
    for i in range(15):
        r += "c\n250 250 %s\n" % (200+i*10)
    return r


ayylmao = open("ayylmao_c","w")
ayylmao.write(add_curvything())
s = """v
g
curvything.png"""
ayylmao.write(s)
ayylmao.close()
