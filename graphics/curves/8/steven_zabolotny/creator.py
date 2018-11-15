import math, random

s = ""
r = random.randrange(500)
for i in range(10):
    r1 = random.randrange(500)
    r2 = random.randrange(500)
    r3 = random.randrange(500)
    s = s + "c\n%d %d %d\n"%(r1, r2, r3)
for i in range(0, 500, 25):
    s = s + "h\n%d %d %d %d %d %d %d %d\n"%((i + r) % 500, abs(i - r), (500 - i + r) % 500, abs(500 - i - r), math.pow(i + r, 2) % 500, math.pow(abs(i - r), 2) % 500, math.pow(i + r, 0.5), math.pow(abs(i - r), 0.5))
for i in range(0, 500, 25):
    s = s + "b\n%d %d %d %d %d %d %d %d\n"%((i + r) % 500, abs(i - r), math.pow(i + r, 2) % 500, math.pow(abs(i - r), 2) % 500, math.pow(i + r, 0.5), math.pow(abs(i - r), 0.5), (500 - i + r) % 500, abs(500 - i - r))
s = s + "v\ng\nface.png\n"

f = open("script", "w")
f.write(s)
f.close()
