import Deque;

def paliandromeCheck(str):

    dq = Deque.Deque();

    isPaliandrome = False;

    for c in str:
        dq.addFront(c);

    while not isPaliandrome and dq.size() > 1 :
        frontElement = dq.removeFront();
        rearElement = dq.removeRear()
        isPaliandrome = frontElement == rearElement;

    return isPaliandrome;

print(paliandromeCheck("radar"));