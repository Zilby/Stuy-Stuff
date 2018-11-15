from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform ):

    f = open("scrip_c","r").read()
    lines = f.splitlines()

    
    for i in range(len(lines)):
        input = lines[i]
    
        if (input == "l"):
            #draw line
            i+=1
            #do something with lines[i]
        
        elif (input == "i"):
            transform = ident(transform)
            
        elif (input == "s"):
            i+=1
            #do something to break up lines[i]
            
            matrix_mult(make_scale(x,y,z),transform)

        elif (input == "t"):
            i+=1
            #do something to break up lines[i]
    
            points = matrix_mult(make_translate(x,y,z),transform)
            
        elif (input == "x"):
            i+=1
            theta = lines[i]##get rid of new line
    
            points = matrix_mult(make_translate(theta),transform)

            
        elif (input == "y"):
    
        elif (input == "z"):

        elif (input == "a"):

        elif (input == "v"):

        elif (input == "g"):
        
            
points = []
transform = new_matrix()

parse_file( 'script_c', points, transform )
