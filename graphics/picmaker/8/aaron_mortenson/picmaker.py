import os,sys,math


pic = open('pic.ppm','w')
pic.write('''P3 512 512 255 ''')


pixels = []

for i in range(512) :
    pixels.append([])
    for j in range(512) :
        
        x = i - j - 128#rotate by 45 degrees
        y = i + j - 640#and translate
        n = (int)(((x*y) + .1)%((x+y) + .1))#mathimagic!
        hue = n%256#this is based off of something I did early on in
        sat = n%30#netlogo. I originally used %140 and %10 to try to emulate my netlogo results
        r = (int)(sat*abs(hue-0)/29)#that's why I do all this hue-sat stuff...
        g = (int)(sat*abs(hue-127)/29)
        b = (int)(sat*abs(hue-255)/29)
        pixels[i].append([r,g,b])

for i in range(512) :#make the "sun" and it's reflection
    for j in range(384) :
        dist = math.sqrt((i-256)*(i-256) + (j-394)*(j-394))     
        red = (int)(100-dist)
        if red > 0:
            pixels[j][i][0]+= (int)(255-pixels[j][i][0])*.01*red
            pixels[768-j][i][0]+= (int)(255-pixels[768-j][i][0])*.005*red

for i in range(512-169,512) :#make cliffs and their reflections
    for j in range(380) :
        if j < 3*math.log((170-512) + i)/math.log(2):
            pixels[380-j][i] = [pixels[380+j][i][0]/16,pixels[380+j][i][1]/4,pixels[380+j][i][2]/16]
            pixels[380+j][i] = [pixels[380-j][i][0],pixels[380-j][i][1],pixels[380-j][i][2]]
            pixels[380-j][511-i] = [pixels[380-j][i][0],pixels[380-j][i][1],pixels[380-j][i][2]]
            pixels[380+j][511-i] = [pixels[380-j][i][0],pixels[380-j][i][1],pixels[380-j][i][2]]
        
for i in range(512) : #darken sky
    for j in range(384) :
        dist = math.sqrt((i-256)*(i-256) + (j-394)*(j-394)*100)
        b = ((5000-dist)/5000)
        pixels[j][i] = [(int)(pixels[j][i][0]*b),(int)(pixels[j][i][1]*b),(int)(pixels[j][i][2]*(3.0/4.0)*(b + (1.0/3.0)))]

s = ''

for i in range(512) : #put the actual string together
    for j in range(512) :
        s+="%i %i %i " % tuple(pixels[i][j])

pic.write(s)        
pic.close()
