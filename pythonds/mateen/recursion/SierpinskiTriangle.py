import turtle;
import time;

def getMidPoint(pointX, pointY, level):
    # level = 2;
    return [(pointX[0] + pointY[0])/level, (pointX[1] + pointY[1])/level];

def sleep():
    time.sleep(1);

def drawTraingle(point1, point2, point3, myTurtle, degree):

    color = ["red", "green", "blue"]
    myTurtle.fillcolor(color[degree-1]);
    myTurtle.up();
    myTurtle.goto(point1[0], point1[1]);
    myTurtle.down();
    myTurtle.begin_fill();
    myTurtle.goto(point2[0], point2[1]);
    myTurtle.goto(point3[0], point3[1]);
    myTurtle.goto(point1[0], point1[1]);
    myTurtle.end_fill()
    degree = degree - 1;
    if degree > 0:
        drawTraingle(getMidPoint(point1, point2, 2), getMidPoint(point2, point3, 2), getMidPoint(point3, point1, 2), myTurtle, degree);
        drawTraingle(getMidPoint(point1, point2, 3), getMidPoint(point2, point3, 3), getMidPoint(point3, point1, 3), myTurtle, degree);


def main():
    t = turtle.Turtle();
    point1 = [-200, -100];
    point2 = [0, 200];
    point3 = [200, -100];
    drawTraingle(point1, point2, point3, t, 3);
    t.getscreen().exitonclick();

main();