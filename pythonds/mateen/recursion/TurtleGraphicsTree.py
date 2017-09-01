import turtle;
import time;

def tree(branchLength, t):
    if branchLength > 5:
        t.forward(branchLength)
        time.sleep(1);
        t.right(20)
        tree(branchLength-15,t)
        time.sleep(1);
        t.left(40)
        tree(branchLength-15,t)
        time.sleep(1);
        t.right(20)
        t.backward(branchLength)
        time.sleep(1);

def main():
    tur = turtle.Turtle();
    time.sleep(1);
    tur.left(90);
    tur.up();
    time.sleep(1);
    tur.backward(100)
    time.sleep(1);
    tur.down();
    tur.color("green");
    tree(75, tur);
    tur.getscreen().exitonclick();



main();