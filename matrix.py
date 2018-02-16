import math
from random import random

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
    numRows=len(m1[0])
    numCols=len(m2)
    result=new_matrix(numRows, numCols)
    for c in range(numCols):
        for r in range(numRows):
            for k in range(len(m2[0])):
                result[c][r]+=m1[k][r]*m2[c][k]
    for r in range(len(result)):
        for c in range(len(result[0])):
            m2[r][c]=result[r][c]
    return m2

    
#Creates matrix (default is 4 rows by 4 cols)
def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#Creates matrix with random ints (default is 4 rows by 4 cols)
def new_random_matrix(rows=4, cols=4):
    m=[]
    for r in range(cols):
        m.append([])
        for c in range(rows):
            m[r].append( int(random()*8)+1 )
    return m
