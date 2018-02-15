import math

#Prints matrix
def print_matrix( matrix ):
    ma=matrix
    s=""
    for i in range(len(ma[0])):
        for c in range(len(ma)):
            s+=str(ma[c][i])
            s+=" "
        s+="\n"
    print s

#Matrix identity element
def ident( matrix ):
    #num of cols in identity element = num of rows in matrix
    cols=len(matrix)
    ma=matrix
    m=[]
    for c in range(len(ma[0])):
        m.append([])
        for r in range(len(ma[0])):
            if r==c:
                m[c].append(1)
            else:
                m[c].append(0)
    return m
                

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m2Copy=[]
    for r in range(len(m2)):
        m2Copy.append([])
        for c in range(len(m2[0])):
            m2Copy[r].append(m2[r][c])
    numRows=len(m1)
    numCols=len(m2[0])
    #NOT FINISHED

    
#Creates matrix with 4 rows and 4 cols
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def matrix():
    m=[]
    m.append([])
    m[0].append(1)
    m[0].append(3)
    m[0].append(5)
    m.append([])
    m[1].append(2)
    m[1].append(4)
    m[1].append(6)
    return m

a=matrix()
print_matrix(a)
#n=new_matrix()
#print_matrix(n)
print print_matrix(ident(a))
