# MateenSA
# N Squared Algortihm : To find smallest number in list

from random import randrange;
import time;

def findMin(alist):

    small = None;
    for i in alist:
        found = True;
        for j in alist:
            if i > j:
                found = False;
        if found:
            small = i;
    return small;


def findMinLinear(alist):
    minSoFar = alist[0];
    for item in alist:
        if item < minSoFar:
            minSoFar = item;
    return minSoFar;

li = [5, 4, -1, 2, 1, 0]
# print(findMin(li))
# print(findMinLinear(li))

print("------------Non Linear Output using NSquared Approach of Big-O notation------------\n")
for listsize in range(1000, 10001, 1000):
    alist = [randrange(10000) for x in range(listsize)]
    starttime = time.time();
    minNumber = findMin(alist);
    endtime = time.time();
    print(" Found min number %d from list size %d in time %f" %(minNumber, listsize, (endtime-starttime)) )

print("\n------------ Linear Approach ------------\n")
for listsize in range(1000, 10001, 1000):
    alist = [randrange(10000) for x in range(listsize)]
    starttime = time.time();
    minNumber = findMinLinear(alist);
    endtime = time.time();
    print(" Found min number %d from list size %d in time %f" %(minNumber, listsize, (endtime-starttime)) )

