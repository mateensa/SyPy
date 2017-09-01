def sequentialSearch(li, searchItem):

    position = 0;
    found = False;
    while position < len(li) and not found:
        if li[position] == searchItem:
            found = True;
        position = position + 1;
    return position;

def sequentialSearchForOrderedLists(li, searchItem):

    position = 0;
    found = False;
    while position < len(li) and not found:
        if searchItem <= li[position]:
            found = True;
        position = position + 1;
    return position if searchItem == li[position] else None;

print(sequentialSearch([1, 10, 20, 2, 100, 30, 50], 100))
print("Ordered list result")
print(sequentialSearchForOrderedLists([1, 2, 10, 20, 30, 50, 100], 21))
