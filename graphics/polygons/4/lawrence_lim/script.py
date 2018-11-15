from draw import *

def add_idkthing():
    r = ""
    r += "i\n"
    r += "x\n%s\n" % (180.0/100)
    r += "y\n%s\n" % (90.0/100)
    r += "z\n%s\n" % (180.0/100)
    r += "m\n0 0 25\n"
    r += "d\n200 200 10 50\n"
    r += "d\n-200 -200 10 50\n"
    for i in range(100):
        i = i*2 + 50
        r += "p\n%s %s %s %s %s %s\n" % (-i/2,-i/2,-i/2,i,i,i)
        r += "a\n"
    r += "i\n"
    r += "t\n250 250 0\n"
    r += "a\n"
    return r
    

ayylmao = open("ayylmao_c","w")
ayylmao.write(add_idkthing())
s = """v
g
idkthing.png"""
ayylmao.write(s)
ayylmao.close()
