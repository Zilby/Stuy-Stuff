print "rm rotation/*"
for i in range(73):
    print "python main.py 100 250 250 0 %i 30 -60 'rotation/icos%02d.gif' > script_c" % (i*2, i)
    print "python parser.py"

print "animate rotation/*"
#s = "convert "
#for i in range(30):
#    s+="rotation/icos%02d.gif " % i
#s+= "-loop 0 icos.gif"
