class Stack:

    def __init__(self):
        self.item = [];

    def isEmpty(self):
        return self.item == [];

    def push(self, x):
        self.item.append(x);

    def pop(self):
        return self.item.pop();

    def peek(self):
        return self.item[len(self.item) - 1];

    def size(self):
        return len(self.item);


#
# s=Stack()
#
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print("Popping ",   s.pop())
# print(s.pop())
# print(s.size())

def parChecker(symbolString):

    s = Stack();
    balanced = True;
    for c in symbolString:
        if c in '([{':
            s.push(c);
        else:
            balanced = False if not symbolChecker(s.pop(), c) and s.isEmpty() else True;
    return True if balanced and s.isEmpty() else False;

def symbolChecker(popedValue, symbolChar):
    item1 = "([{";
    item2 = ")]}"
    return item1.index(popedValue) == item2.index(symbolChar);


print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))