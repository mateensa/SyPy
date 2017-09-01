import timeit

l = [x for x in range(10)]
print(l)

# POP: Returns arbitary popped value (most of time last value in list) its complexity is O(1)
popValue = l.pop()
print(l)
print(popValue)

#Same as previous pop but it takes index its complexity is O(n)
popValue = l.pop(0)
print(l)
print(popValue)

# Returns null
popValue = l.remove(1)
print(l)
print(popValue);

#Its operator rather than function
del l[2];

print(l)

print("+++++++++++++++++++++++++++++++++++++++++++++++++")



popzero = timeit.Timer("alist.pop()","from __main__ import alist");
alist = list(range(1000000));
print(popzero.timeit(number=10000));

# popi = timeit.Timer("alist.pop(0)","from __main__ import alist");
# alist = list(range(1000000));
# print(popi.timeit(number=10000));

print("++++++++++++++++++++++++++++++++++++++++++++++++++++-")

popi = timeit.Timer("x.pop(0)", "from __main__ import x");
popLast = timeit.Timer("x.pop()", "from __main__ import x");



for i in range(10000, 1000001, 10000):
    x = list(range(i))
    print("Pop i time taken ",popi.timeit(number=100));

    x = list(range(i))
    print("Pop time taken ", timeit.timeit(number=100));