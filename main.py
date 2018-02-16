from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 255 ]
matrix = new_matrix()

##TEST CASES
print "DEFAULT MATRIX m1"
m1=new_matrix()
print_matrix(m1)

print "IDENTITY ELEMENT OF MATRIX m1"
iden=ident(m1)
print_matrix(iden)

print "RANDOM MATRIX m2 WITH SPECIFIED # OF ROWS/COLUMNS (IN THIS CASE 4 ROWS BY 4 COLUMNS SINCE WE NEED RESULT TO HAVE SAME DIMENSIONS AS SECOND ELEMENT)"
m2=new_random_matrix(4,4)
print_matrix(m2)

print "RANDOM MATRIX m3 WITH SPECIFIED # OF ROWS/COLUMNS (IN THIS CASE 4 ROWS BY 4 COLUMNS SINCE WE NEED RESULT TO HAVE SAME DIMENSIONS AS SECOND ELEMENT)"
m3=new_random_matrix(4,4)
print_matrix(m3)

print "MATRIX MULTIPLICATION m2*m3"
matrix_mult(m2,m3)
print_matrix(m3)

print "RANDOM MATRIX m4 WITH SPECIFIED # OF ROWS/COLUMNS (e.g. 3 ROWS BY 4 COLUMN, LIKE 4 POINTS WITH X, Y, and Z COORDINATES)"
m4=new_random_matrix(3,4)
print_matrix(m4)

print "ADD POINT (100,220,5) TO MATRIX m4"
m5=add_point(m4, 100, 220, 5)
print_matrix(m5)

print "ADD EDGE (100,220,5) -> (6,8,240) TO MATRIX m4"
m5=add_edge(m4, 100, 220, 5, 6, 8, 240)
print_matrix(m5)


#draw_lines( n, screen, color )
#display(screen)
#save_extension(screen, 'img.png')
