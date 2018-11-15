import random

f = open ("pic.ppm", 'w')
f.write ("P3\n500 500\n255\n")

i = 500 * 500
n = random.randint (0, 255)
x = n%3

while i > 0:
    
    r = i%255
    g = n
    b = n
    t = ("%d %d %d "%(r, g, b))
    i = i - 1
    f.write (t)

f.close()
