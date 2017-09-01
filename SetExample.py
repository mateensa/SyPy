# List is collection of heterogeneous, mutable, indexed data type
# Tuple is also collection of heterogeneous and indexed but mutable type (mutability is only difference between list and tuple)
# Set is collction of heterogeneous, unordered, immutable and it does not allow duplicates

#Set Example
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
s.remove(5) # removes elemenet 5 from set if 5 does not exists then it teturns key error
print(s)
s.discard(0) #Removes element 0 from set if does not exists then it does not return any error
print(s)
# s.remove(0) #KeyError: 0
s.pop() # Removes arbitary element from set
print(s)
s2 = set(); # Declare empty set
# s2.pop(); #KeyError: 'pop from an empty set'

#Another way of creating set
s3 = {3,6,"cat",4.5,False};
print(s3)
print(3 in s3)