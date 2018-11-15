from display import *
from draw import *
from math import *

# TORUS KNOT (a, b)
# 	x = (r2 + r1*sin(at)) * cos(bt)
# 	y = (r2 + r1*sin(at)) * sin(bt)
# 	z = r1*cos(at)
# 	dx/dt = -b*sin(bt) * (r2 + r1*sin(at)) + a*r1*cos(at)*cos(bt)
# 	dy/dt = b*cos(bt) * (r2 + r1*sin(at)) + a*r1*cos(at)*sin(bt)
# 	dz/dt = -a*r1*sin(at)
a = 3
b = 2
rres = 16 		#radial resolution
kres = 180 		#linear resolution
r1 = 60 		#radius of central torus
r2 = 150 		#radius of torus cross-section
r3 = 50 		#radius of knot
deg = 6 		#degrees per rotation
rots = 20 		#rotations per cycle; deg * rots = 360/a
viewangle = 30 	

def gencircle(x, dxs):
	dx, dy, dz = dxs[0], dxs[1], dxs[2]
	r = dx*dx + dy*dy
	sl = sqrt(r)
	# l = <dy/dt, -dx/dt, 0> with length r3
	l = [(r3 * dy) / sl, -(r3 * dx) / sl,  0]
	su = sqrt(r * (r + dz*dz))
	# u = <-dx/dt * dz/dt, -dy/dt * dz/dt, (dx/dt)^2 + (dy/dt)^2> with length r3
	u = [(-dx * dz * r3) / su, (-dy * dz * r3) / su, (r * r3) / su]
	return [[x[i] + l[i]*cos((2*pi*j)/rres) + u[i]*sin((2*pi*j)/rres) for i in range(3)] for j in range(rres)]

def xv(t):
	return [(r2 + r1*sin(a*t))*cos(b*t), (r2 + r1*sin(a*t))*sin(b*t), r1*cos(a*t)]

def dxv(t):
	return [-b*sin(b*t)*(r2 + r1*sin(a*t)) + a*r1*cos(a*t)*cos(b*t), b*cos(b*t)*(r2 + r1*sin(a*t)) + a*r1*cos(a*t)*sin(b*t), -a*r1*sin(a*t)]

x = [xv((2*pi*t)/kres) for t in range(kres)]
dx = [dxv((2*pi*t)/kres) for t in range(kres)]

f = open("script_c", "w")

for i in range(kres):
	a = gencircle(x[i], dx[i])
	b = gencircle(x[(i+1)%kres], dx[(i+1)%kres])
	for j in range(rres):
		f.write("l\n" + str(a[j][0]) + " " + str(a[j][1]) + " " + str(a[j][2]) + " " + str(a[(j+1)%rres][0]) + " " + str(a[(j+1)%rres][1]) + " " + str(a[(j+1)%rres][2]) + "\n")
		f.write("l\n" + str(a[j][0]) + " " + str(a[j][1]) + " " + str(a[j][2]) + " " + str(b[j][0]) + " " + str(b[j][1]) + " " + str(b[j][2]) + "\n")

f.write("i\n")
f.write("x\n" + str(-viewangle) + "\n")
f.write("t\n250 250 800\n")
for i in range(rots):
	f.write("a\ng\npic%02d.png\n"%(i,))
	f.write("i\n")
	f.write("t\n-250 -250 -800\n")
	f.write("x\n" + str(viewangle) + "\n")
	f.write("z\n" + str(deg) + "\n")
	f.write("x\n" + str(-viewangle) + "\n")
	f.write("t\n250 250 800\n")

f.close()


