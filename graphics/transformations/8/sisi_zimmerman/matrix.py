import math

def make_translate( x, y, z ):
    m = []
    m.append([1 , 0 ,0 ,0])
    m.append([0 , 1 ,0 ,0])
    m.append([0 , 0 ,1 ,0])
    m.append([x , y ,z ,1])
    return m

def make_scale( x, y, z ):
    m = []
    m.append([x , 0 ,0 ,0])
    m.append([0 , y ,0 ,0])
    m.append([0 , 0 ,z ,0])
    m.append([0 , 0 ,0 ,1])
    return m

def make_rotX( theta ):
    theta = math.radians(theta)   
    m = []
    m.append([1 , 0 ,0 ,0])
    m.append([0 ,math.cos(theta) , math.sin(theta) ,0])
    m.append([0, -math.sin(theta) , math.cos(theta)  ,0])
    m.append([0 , 0 ,0 ,1])
    return m


def make_rotY( theta ):
    theta = math.radians(theta)
    m = []
    m.append([math.cos(theta) ,0,math.sin(theta) ,0])
    m.append([0 , 1 ,0 ,0])
    m.append([-math.sin(theta),0, math.cos(theta)  ,0])
    m.append([0 , 0 ,0 ,1])
    
    return m


def make_rotZ( theta ):
    #make theta form degree to radian 
    theta = math.radians(theta)
    m = []
    m.append( [math.cos(theta) , math.sin(theta) ,0 ,0] )
    m.append( [-math.sin(theta) , math.cos(theta) ,0 ,0])
    m.append([0 , 0 ,1 ,0])
    m.append([0 , 0 ,0 ,1])
    
    return m


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
            m.append( [] )
            for r in range( rows ):
                    m[c].append( 0 )
                    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    m = []
    m.append( [1 , 0 ,0 ,0])
    m.append( [0 , 1 ,0 ,0])
    m.append( [0 , 0 ,1 ,0])
    m.append( [0 , 0 ,0 ,1])
    return m


def scalar_mult( matrix, x ):
    for p in matrix:
        for i in range(len( matrix[0] ) ):
            p[i] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
        m_final = []

        i = 0                
        while( i < len(m1[0])):
           
            #print "i:" + str(i) + "\n"
            k = 0
            
            while(k < len(m2)):
                if (i==0):
                    m_final.append([])
                #print "k:" + str(k) + "\n"
                sum = 0
                j = 0
                while(j < len(m1) ):
                    #print "j:" + str(j) + "\n"
                    #print "m1[j][i]:" + str(m1[j][i]) + "\n"
                    #print "m2[k][j]:" + str(m2[k][j]) + "\n"
                    sum += m1[j][i] * m2[k][j]
                    
                    j += 1
                #print "sum:" + str(sum) + "\n"
                m_final[k].append(sum)
                k += 1

            i += 1
        #print_matrix(m_final)
        #m2 = m_final
        return m_final
