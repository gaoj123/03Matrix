from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 238, 130, 238 ]

##TEST CASES
print "DEFAULT MATRIX m1"
m1=new_matrix(4,4)
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

##DRAWING

##STEM
n=new_matrix(4,4)
x=250
y=0

color = [ 60, 179, 113 ]
add_edge(n,x-5,y,0,x-5,y+225,0)
add_edge(n,x-5,y+225,0,x+5,y+225,0)
add_edge(n,x+5,y+225,0,x+5,0,0)
draw_lines( n, screen, color )


##FLOWER
n=new_matrix(4,4)

color = [ 238, 130, 238 ]
x=x+5
y=y+225
add_edge(n,x,y,0,x+10,y+5,0)
add_edge(n,x+10,y+5,0,x+20,y+15,0)
add_edge(n,x+20,y+15,0,x+30,y+25,0)
add_edge(n,x+30,y+25,0,x+35,y+35,0)
add_edge(n,x+35,y+105,0,x+35,y+35,0)
add_edge(n,x+35,y+105,0,250,y+65,0)
add_edge(n,270,y+85,0,250,y+105,0)
         
x=245
y=225
add_edge(n,x,y,0,x-10,y+5,0)
add_edge(n,x-10,y+5,0,x-20,y+15,0)
add_edge(n,x-20,y+15,0,x-30,y+25,0)
add_edge(n,x-30,y+25,0,x-35,y+35,0)
add_edge(n,x-35,y+105,0,x-35,y+35,0)
add_edge(n,x-35,y+105,0,250,y+65,0)
add_edge(n,230,y+85,0,250,y+105,0)
draw_lines( n, screen, color )

##LEAVES
n=new_matrix(4,4)
color = [ 60, 179, 113 ]

x=255
y=40
add_edge(n,x,y,0,x+20,y+10,0)
add_edge(n,x+30,y+30,0,x+20,y+10,0)
add_edge(n,x+30,y+30,0,x+40,y+70,0)
add_edge(n,x+20,y+60,0,x+40,y+70,0)
add_edge(n,x+20,y+60,0,x+10,y+50,0)
add_edge(n,x,y+10,0,x+10,y+50,0)

add_edge(n,x+10,y+10,0,x+30,y+60,0)

x=245
y=60
add_edge(n,x,y,0,x-20,y+10,0)
add_edge(n,x-30,y+30,0,x-20,y+10,0)
add_edge(n,x-30,y+30,0,x-40,y+70,0)
add_edge(n,x-20,y+60,0,x-40,y+70,0)
add_edge(n,x-20,y+60,0,x-10,y+50,0)
add_edge(n,x,y+10,0,x-10,y+50,0)

add_edge(n,x-10,y+10,0,x-30,y+60,0)

draw_lines( n, screen, color )
display(screen)
save_extension(screen, 'img.png')
