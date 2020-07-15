import pygame, sys, math, random


width = height = 1000

triangle_side = width
triangle_height = (triangle_side * math.sqrt(3))/ 2
iterations = 8

pygame.init()

canvas = pygame.display.set_mode( ( width, height ) )


finished = False
clock = pygame.time.Clock()

def drawLine( a, b ):
    pygame.draw.line( canvas, (255,255,255), a, b )

def drawTriangle( a, b, c ):
    drawLine( a, b )
    drawLine( b, c )
    drawLine( c, a )

def getCenter( a, b ):
    center = ( (a[0]+b[0])/2, (a[1]+b[1])/2 )
    return center

def frac( order, a, b, c ):
    if( order == 0 ):
        drawTriangle( a, b, c )
    else:
        
        ab = getCenter( a, b )
        bc = getCenter( b, c )
        ca = getCenter( c, a )

        frac( order-1, a, ab, ca )
        frac( order-1, ab, b, bc )
        frac( order-1, bc, c, ca )
        
        pass

frac( iterations, (0,triangle_height), (triangle_side/2,0), (triangle_side, triangle_height) )


pygame.display.flip()




while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    



pygame.quit()
quit()
