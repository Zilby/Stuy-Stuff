import math as m

f = open('pic.ppm', 'w+')
f.write('P3\n500 500\n256\n')

k = 0

for i in range(500):
    line = ''
    for j in range(500):
        if (k == 360):
            k = 0
        r = (m.cos(m.radians(k))*i)%256
        g = (m.sin(m.radians(k))*j)%256
        b = 255
        k += 1
        line += "%d %d %d "%(r,g,b)
    f.write(line+'\n')

f.close()
