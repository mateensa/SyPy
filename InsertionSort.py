#Name: SelectionSort
#Author: Mateen SA
#Comments: It always maintains a sorted sublist in the lower positions of the list.
            # Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger.
#Complexity: O(n*2*2)

def insertionSort(alist):

    for index in range(1, len(alist)):

        startPosition = index;
        currentValue = alist[startPosition];

        while startPosition > 0 and alist[startPosition-1] > currentValue:

            #Always take currentValue and check in sublist (that is, from 0 to start position in alist)
            alist[startPosition] = alist[startPosition -1 ];
            startPosition = startPosition - 1;

        alist[startPosition] = currentValue;



alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)