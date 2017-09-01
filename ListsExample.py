list = [1,  2.2, 3.33, 4.44, 'a', 'bcdefg']

for item in list:
    print  (item);
    if item == 'bcdefg':
        alist = list[len(list)-1]
        for subitem in alist:
            print("Printing subitem ", subitem)



print("++++++++++++++++++++++++Sceanrio 2222++++++++++++++++++++++++++")
#Scenario 2
list2 = [1,  2.2, 3.33, 4.44, 'a', ['b','c','d','e','f','g']]


alist2 = list2[len(list2)-1]
for subitem2 in alist2:
    print("Printing subitem ", subitem2)




