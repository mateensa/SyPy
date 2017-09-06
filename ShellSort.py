#Name: SelectionSort
#Author: Mateen SA
#Comments: this is very similar to insertion sort but exchange items with gap, gap = n/2... where n=len(alist)
#Complexity: O(n * log (n) ) which means, A shell sort improves on the insertion sort by sorting incremental sublists.
    # It falls between O(n) and O(n2)




def shellSort(alist):

    sublistCount = len(alist) // 2;
    while sublistCount > 0 :

        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount);
            print("After increments of size", sublistCount, "The list is", alist)
        sublistCount = sublistCount // 2;


#This method is very similar to insertion sort in InsertionSort.py except it jumps for replacing cell values with gap not sequentially

def gapInsertionSort(alist, start, gap):


    for index in range(start+gap, len(alist), gap):

        startPosition = index;
        currentValue = alist[startPosition];

        while startPosition >= gap and alist[startPosition-gap] > currentValue:

            #Always take currentValue and check in sublist (that is, from 0 to start position in alist)
            alist[startPosition] = alist[startPosition - gap];
            startPosition = startPosition - gap;

        alist[startPosition] = currentValue;



alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)