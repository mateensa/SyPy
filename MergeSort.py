#Name: MergeSort
#Author: Mateen SA
#Comments: we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted,
                # the fundamental operation, called a merge, is performed
#Complexity: A merge sort is O(n * log n), but requires additional space for the merging process.



def mergeSort(alist):

    if len(alist) > 1 :
        midPoint = len(alist) // 2;

        left = alist[:midPoint];
        right = alist[midPoint:];

        mergeSort(left);
        mergeSort(right);

        i = 0;
        j = 0;
        k = 0;

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                alist[k] = left[i];
                i = i + 1;
            else :
                alist[k] = right[j];
                j = j + 1;
            k = k + 1;

        while i < len(left):
            alist[k] = left[i];
            i = i + 1;
            k = k + 1;

        while j < len(right):
            alist[k] = right[j];
            j = j + 1;
            k = k + 1;

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
