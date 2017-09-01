import turtle;


def drawSprial(myTurtle, linelen):
    if linelen >0:
        myTurtle.forward(linelen);
        myTurtle.right(90);
        drawSprial(myTurtle, linelen-1)


myTurtle = turtle.Turtle()
myWin = turtle.Screen()
drawSprial(myTurtle, 100);
myWin.exitonclick();