#TurtleGraphics.py
#Name:Mauricio
#Date:0/21/25
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
#hideTurtle()#hides the default turtle in codeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.foward(50)
        bob.right(360/sides)

def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
     
     if corner==1:
         alice.begin_fill()
        drawsquare(alice, 50)
        alice.end_Fill()
        elif corner ==2:
            alice.forward(50)
            alice.begin_fill()
            drawSquare(alice, 50)
            alice.end_fill()

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
        
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
