#Name: MergeSort
#Author: Mateen SA
#Comments:
#Complexity: A quick sort is O(n * logn), but may degrade to O(n  * n) ,
        #  if the split points are not near the middle of the list. It does not require additional space.


def quickSort(alist):

    pivotValue = alist[0];
    quickSortHelper(alist, pivotValue, 1, len(alist)-1);


def quickSortHelper(alist, pivotValue, first, last):

    if first < last:
        splitPosition = getPosition(alist, pivotValue, first, last);
        quickSortHelper(alist, pivotValue, first, splitPosition - 1);
        quickSortHelper(alist, pivotValue, splitPosition + 1, last);

def getPosition(alist, pivotValue, first, last):

    done = False;

    while not done:

        while first <= last and alist[first] <= pivotValue:
            first = first + 1;

        while last >= first and  alist[last] >= pivotValue:
                last = last - 1;

        if not first < last:
            done = True;
        else:
            temp = alist[first];
            alist[first] = alist[last];
            alist[last] = temp;

    temp = alist[first]
    alist[first] = alist[last]
    alist[last] = temp

    return last;


alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)