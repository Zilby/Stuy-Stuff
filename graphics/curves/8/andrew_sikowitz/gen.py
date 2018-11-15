s = ""
from random import random
for i in range(1,10):
	s+="c\n250 250 " + str(i*20) + "\n"

for i in range(1,5):
	s += "h\n250 250 " + str(random()*500) + " " + str(random()*500) + " 250 250 " + str(random()*500) + " " + str(random()*500) + "\n"

for i in range(1,5):
	s += "b\n150 150 " + str(random()*500) + " " + str(random()*500) + " 150 150 " + str(random()*500) + " " + str(random()*500) + "\n"

s += "v\ng\npic.png"

f = open("script_c","w")
f.write(s)
