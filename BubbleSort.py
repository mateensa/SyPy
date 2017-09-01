#Bubble Sort:
# The bubble sort makes multiple passes through a list.
# It compares adjacent items and exchanges those that are out of order.
# Each pass through the list places the next largest value in its proper place.
# In essence, each item “bubbles” up to the location where it belongs.

def bubblesort(list) :
    for looper in range(len(list)-2) :
        for i in range(len(list)-1) :
            if list[i] > list[i+1] :
                temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
                # swapnumber(list[i], list[i+1])
            else :
                pass
    return list;

def swapnumber(i, j):
    temp = i;
    i = j;
    j = temp;
    return i, j;

print(bubblesort([100, 80, 90, 10 ,40]))
print(list(range(5,10,2)));