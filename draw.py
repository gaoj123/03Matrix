from display import *
from matrix import *

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    #Essentially just adding two points to matrix
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    #same # of rows, 2 more cols

def add_point( matrix, x, y, z=0 ):
    #same # of rows, 1 more col
    matrix.append([x,y,z])

def draw_line( x0, y0, x1, y1, screen, color ):
    x=x0
    y=y0
    A=y1-y0
    B=-(x1-x0)
    if x0==x1:  ##Vertical Line
        smallY=min(y0,y1)
        bigY=max(y0,y1)
        for i in range(smallY,bigY+1):
            plot(screen,color,x0,i)
    else:
        m=(A+0.0)/(-B) ##Calculate slope if not undefined
        if y0==y1:  ##Horizontal Line
            smallX=min(x0,x1)
            bigX=max(x0,x1)
            for i in range(smallX,bigX+1):
                plot(screen,color,i,y0)
        elif m>0 and m<1 and x1>x0:  ##Octant 1
            d=2*A+B
            while x<=x1:
                plot(screen,color,x,y)
                if d>0:
                    y+=1
                    d+=2*B
                x+=1
                d+=2*A
        elif m>1 and y1>y0:  ##Octant 2
            d=A+2*B
            while y<=y1:
                plot(screen,color,x,y)
                if d<0:
                    x+=1
                    d+=2*A
                y+=1
                d+=2*B
        elif m<0 and m>-1 and x1>x0:  ##Octant 8
            d=2*A-B
            while x<=x1:
                plot(screen,color,x,y)
                if d<0:
                    y-=1
                    d-=2*B
                x+=1
                d+=2*A
        elif m<-1 and y1<y0: ##Octant 7
            d=A-2*B
            while y>=y1:
                plot(screen,color,x,y)
                if d>0:
                    x+=1
                    d+=2*A
                y-=1
                d-=2*B
        elif m>1 and y1<y0:  ##Octant 6
            draw_line(x1,y1,x0,y0,screen,color)
        elif m>0 and m<1 and x1<x0:  ##Octant 5
            draw_line(x1,y1,x0,y0,screen,color)
        elif m<0 and m>-1 and x1<x0:  ##Octant 4
            draw_line(x1,y1,x0,y0,screen,color)
        elif m<-1 and y1>y0:  ##Octant 3
            draw_line(x1,y1,x0,y0,screen,color)
        elif m==1:
            smallX=min(x0,x1)
            bigX=max(x0,x1)
            if smallX==x0:
                y=y0
            else:
                y=y1
            while smallX<=bigX:
                plot(screen,color,smallX,y)
                smallX+=1
                y+=1
        elif m==-1:
            smallX=min(x0,x1)
            bigX=max(x0,x1)
            if smallX==x0:
                y=y0
            else:
                y=y1
            while smallX<=bigX:
                plot(screen,color,smallX,y)
                smallX+=1
                y-=1
            
            
def draw_lines( matrix, screen, color ):
    a=matrix
    cols=len(a)
    if cols==2:
        draw_line(a[0][0], a[0][1], a[1][0], a[1][1], screen, color)
    elif cols>2:
        i=0
        while(i<cols):
            draw_line(a[i][0],a[i][1],a[i+1][0],a[i+1][1],screen,color)
            i+=2

            
