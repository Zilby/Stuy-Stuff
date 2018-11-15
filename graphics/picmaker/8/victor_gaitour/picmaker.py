s="P3\n512 512\n 255\n"
s1=""
for k in range(4):
    for i in range(256):
        for j in range(256):
            s1=s1+str(i)+" "+str(j)+" "+str(k*64)+" "

with open("pic.ppm","w") as f:
    f.write(s+s1)
    f.close
