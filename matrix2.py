import math

#Prints matrix
def print_matrix( matrix ):
    ma=matrix
    s=""
    for r in range(len(ma)): #num of rows
        for c in range(len(ma[0])):
            s+=str(ma[r][c])
            s+=" "
        s+="\n"
    print s

#Matrix identity element
def ident( matrix ):
    #num of cols in identity element = num of rows in matrix
    cols=len(matrix)
    #ma=matrix
    m=[]
    for r in range(cols): #r is row in identity matrix
        m.append([])
        for c in range(cols): #c is col in identity matrix
            if r==c:
                m[r].append(1)
            else:
                m[r].append(0)
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

n=new_matrix()
print_matrix(n)
print print_matrix(ident(n))
