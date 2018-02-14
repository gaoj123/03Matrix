import math


def print_matrix( matrix ):
    s=""
    for i in len(matrix):
        ##for c in matrix len:
            s+=str(c[i])+" "
        s+="\n"
    print s

def ident( matrix ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

n=new_matrix
print_matrix(n)
