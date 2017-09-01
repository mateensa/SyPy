__author__ = "Mateen"

from timeit import Timer;

def test1(): #Concat
    l = []
    for i in range(1000):
        l = l + [i]

def test2(): #Append

    l = [];
    for i in range(1000):
        l.append(i);

def test3(): #Comprehension
    l = [i for i in range(1000)];

def test4(): #Range
    l = list(range(1000));

def test5():
    #empty function
    pass


timer1 = Timer("test1()", "from __main__ import test1");
print("concat ",timer1.timeit(number=1000), "milliseconds");

timer2 = Timer("test2()", "from __main__ import test2");
print("append ",timer2.timeit(number=1000), "milliseconds");

timer3 = Timer("test3()", "from __main__ import test3");
print("comprehension ",timer3.timeit(number=1000), "milliseconds");

timer4 = Timer("test4()", "from __main__ import test4");
print("range ",timer4.timeit(number=1000), "milliseconds");

timer5 = Timer("test5()", "from __main__ import test5");
print("range ",timer5.timeit(number=1000), "milliseconds");



