#
#Linear Search: It returns index of item if found else returns -1
#

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


def linearsearch(searchitem) :
    i = 0;
    while i < len(li):
        if li[i] == searchitem:
            return  i + 1;
        i = i + 1;

returnvalue = linearsearch(9)

print(-1 if returnvalue == None else returnvalue)



