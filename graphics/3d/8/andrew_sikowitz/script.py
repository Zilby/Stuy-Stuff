f = open("script_c","w")

for i in range(1,100):
    f.write("p\n350 350 0 %02d %02d %02d\nm\n150 350 %02d\nd\n250 250 30 %02d\ni\nx\n20\ny\n20\na\ng\ntorus%02d.png\nw\n"%(i,i,i,i,i,i))
