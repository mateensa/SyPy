#Binary Search: The binary search is used to find an item in an ORDERED list.

# To search for an item, look in the middle of the list and see if the number you want is in the middle,
# above the middle or below the middle.
#
# If it is in the middle, you have found the item.
# If it is higher than the middle value, then adjust the bottom of the list so that you search in a smaller list
# starting one above the middle of the list.
# If the number is lower than the middle value, then adjust the top of the list so that you search in a smaller list
# which has its highest position one less than the middle position.
#Complexity: O(n * log n), with worst case it is O(n*2*2)


def binarysearch(li, searchitem) :
    found = False;
    first = 0;
    last = len(li)-1;

    while not found and  first <= last :
        middle = int((first + last) / 2);
        if searchitem == li[middle]:
            print("found at index " ,middle)
            found = True;
        else :
            if searchitem < li[middle] :
                last = middle-1;
            else :
                first = middle+1;

    return found;


print(binarysearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))



print(range(10-1 ,-1))