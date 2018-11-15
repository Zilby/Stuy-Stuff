import random

f = open("script_c", 'w+')
script = ""

for i in range(10):
    a = random.randint(0,500)
    b = random.randint(0,500)
    c = random.randint(0,500)
    d = random.randint(0,500)
    script += 'h\n%d %d %d %d %d %d %d %d\nc\n%d %d %d\n'%(0,0,500,500,a,b,c,d,a,b,30)
    script += 'b\n%d %d %d %d %d %d %d %d\nc\n%d %d %d\n'%(0,0,500,500,a,b,c,d,c,d,30)
    
script += 'v\ng\npic.png'
f.write(script)
f.close()
