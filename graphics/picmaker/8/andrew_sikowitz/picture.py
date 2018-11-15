import math

def nonzero(x):
    if int(x) == 0:
        return 1
    return int(x)

def getcolor(dire):
    sd = math.pi/3 #sixty degrees

    if dire > math.pi*5/3:
        x = 2*math.pi - dire
        r = 255
        g = 0
        b = x*255/sd
    elif dire > math.pi*4/3:
        x = 5.0/3*math.pi - dire
        r = 255-x*255/sd
        g = 0
        b = 255
    elif dire > math.pi:
        x = 4.0/3*math.pi - dire
        r = 0
        g = x*255/sd
        b = 255
    elif dire > math.pi*2/3:
        x = math.pi - dire
        r = 0
        g = 255
        b = 255-x*255/sd
    elif dire > math.pi/3:
        x = 2.0/3*math.pi - dire
        r = x*255/sd
        g = 255
        b = 0
    else:
        x = 1.0/3*math.pi - dire
        r = 255
        g = 255-x*255/sd
        b = 0

    return str(int(r)) + " " + str(int(g)) + " " + str(int(b)) + " "

s = "P3\n512 512\n255\n"

for i in range(512):
    for j in range(512):
        x = j-256
        y = 256-i
        mag = int(round(math.sqrt(x*x + y*y)))
        dire = math.atan2(y,x)
        tp = 2*math.pi
        if dire < 0:
            dire = tp+dire
        
        c = math.sqrt(dire)+1.5 #Thickness of lines
        d = 5 #How many rings (r = d*theta)

	#print x,y,dire

        if abs(mag - d*(tp*math.floor(mag/(d*tp))+dire)) < c:
            s += "0 0 0 "
        else:
            s += getcolor(dire)
    s += "\n"

f = open("pic.ppm","w")
f.write(s)
f.close()
