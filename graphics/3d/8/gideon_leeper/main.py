f = open("script", "w")
res = 100
n = 3
for i in range(res):
	f.write("i\n")
	f.write("m\n0 0 20\n")
	if n%2 == 0:
		f.write("y\n%f\n"%(360.0/res,))
	else:
		f.write("x\n%f\n"%(360.0/res,))
	for j in range(1,n+1):
		f.write("x\n-90\na\ni\n")
		f.write("d\n0 0 20 %d\n"%(50*j,))
		f.write("x\n90\n")
		if n%2 == j%2:
			f.write("y\n%f\n"%(i*360.0/res,))
		else:
			f.write("x\n%f\n"%(i*360.0/res,))
	f.write("a\ni\n")
	f.write("t\n250 250 0\na\n")
	f.write("g\np%02d.png\nw\n"%(i,))
f.close()
