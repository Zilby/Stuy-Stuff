from display import *
from draw import *
from matrix import *
import sys

r1 = [[0, 1, 1.618], [0, -1, 1.618], [0, -1, -1.618], [0, 1, -1.618]]
r2 = [[1.618, 0, -1], [1.618, 0, 1], [-1.618, 0, 1], [-1.618, 0, -1]]
r3 = [[-1, 1.618, 0], [1, 1.618, 0], [1, -1.618, 0], [-1, -1.618, 0]]

def make_command(command, args):
    s = command
    if len(args) > 0:
        s+='\n'
        for arg in args:
            s+=str(arg)+' '
    print s

def make_icos(s,x,y,z,rx,ry,rz,fname):
    rectangles = [r1,r2,r3]
    for rect in rectangles:
        args = rect[0]+rect[1]
        make_command('l',args)
        args = rect[2]+rect[3]
        make_command('l',args)
    make_command('l',r1[0]+r2[1])
    make_command('l',r1[0]+r2[2])
    make_command('l',r1[0]+r3[0])
    make_command('l',r1[0]+r3[1])
    make_command('l',r1[1]+r2[1])
    make_command('l',r1[1]+r2[2])
    make_command('l',r1[1]+r3[2])
    make_command('l',r1[1]+r3[3])
    make_command('l',r1[2]+r2[0])
    make_command('l',r1[2]+r2[3])
    make_command('l',r1[2]+r3[2])
    make_command('l',r1[2]+r3[3])
    make_command('l',r1[3]+r2[0])
    make_command('l',r1[3]+r2[3])
    make_command('l',r1[3]+r3[0])
    make_command('l',r1[3]+r3[1])
    make_command('l',r2[2]+r3[0])
    make_command('l',r2[2]+r3[3])
    make_command('l',r2[3]+r3[0])
    make_command('l',r2[3]+r3[3])
    make_command('l',r2[0]+r3[1])
    make_command('l',r2[0]+r3[2])
    make_command('l',r2[1]+r3[1])
    make_command('l',r2[1]+r3[2])
    make_command('i',[])
    make_command('s',[s,s,s]) 
    make_command('y',[ry])
    make_command('x',[rx])   
    make_command('z',[rz])
    make_command('t',[x,y,z])
    make_command('a',[])
    make_command('g',[fname])
 
make_icos(*sys.argv[1:])


