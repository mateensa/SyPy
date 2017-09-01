# Created by: Mateen
# Description: Example to demonstrate list comprehension


squarelist = []
for x in range(1,11):
    squarelist.append(x * x);
print(squarelist)

#List comprehension
newlist = [x * x for x in range(1, 11)];
print(newlist)

newlist = ['C','O','M','P','R','E','H','E','N','S','I','O','N']
print(newlist);
print([item.lower() for item in newlist if item not in 'AEIOU']);

print([ch for ch in ['cat','dog','rabbit']]) # iterates over index
print([ch for ch in "".join(['cat','dog','rabbit'])])
# Iterates over index but joining each elements gives list of chars like 'c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't'

# Nested comprehension, yet another way
print([ch[i] for ch in ['cat','dog','rabbit'] for i in range(len(ch))])

#Removing duplicates using set

print(list(set([ch[i] for ch in ['cat','dog','rabbit'] for i in range(len(ch))])))