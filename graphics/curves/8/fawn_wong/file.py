f = open('script_c', 'w')

s = ""
c = "b\n300 150 150 410 260 500 30 350\n"

s += c
s += "i\n"
s += "t\n-250 -250 0\n"
s += "y\n10\n"
s += "z\n10\n"
s += "x\n10\n"
s += "t\n250 250 0\n"

for x in range(36):
    s += "a\n"
    s += c
    
s += "a\nv\ng\npic.png\n"

f.write(s)
