#Name: SelectionSort
#Author: Mateen SA
#Comments: Its is very similar to Bubble sort except it exchanges max item to max position.
#Complexity: O(n*2*2)

def SelectionSort(alist):


    for fillslot in range(len(alist)-1, 0 , -1):

        #Checking from length-1 in descending order to replace max value to max position
        #unlike Bubble Sort

        positionOfMax = 0;
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location;

            temp = alist[positionOfMax];
            alist[positionOfMax] = alist[fillslot];
            alist[fillslot] = temp;


li = [54,26,93,17,77,31,44,55,20];
SelectionSort(li);
print(li)