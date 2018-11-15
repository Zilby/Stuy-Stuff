import random

f = open('script_c','w')
x = 0
script = ""
while x < 36:
    script +='c\n0 0 200\n'
    script += 'i\ny\n10\na\n'
    x = x + 1
x = 0
while x < 36:
    script +='c\n0 0 200\n'
    script += 'i\nx\n10\na\n'
    x = x + 1
script += 'i\nt\n250 250 0\na\n'
x = 0
while x < 20:
    x1 = 200
    x2 = 350
    y1 = 25 + x*5
    y2 = 25 + x*5
    script += 'b\n50 150 '+str(x1)+' '+str(y1)+' '+str(x2)+' '+str(y2)+' 450 150\n'
    x = x + 1
x = 0
while x < 20:
    x1 = 250 - x*10
    x2 = 350 + x*10
    y1 = 100 - x*10
    y2 = 100 + x*10
    script += 'h\n200 250 '+str(x1)+' '+str(y1)+' 300 250 '+str(x2)+' '+str(y2)+'\n'
    x = x + 1
x = 0
while x < 5:
    r = 50 - x*5
    script += 'c\n325 325 '+str(r)+'\n'
    script += 'c\n175 325 '+str(r)+'\n'
    x = x + 1

script += 'v\ng\nterrance.png'
f.write(script)
f.close()
