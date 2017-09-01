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

    def getAllItemsReverse(self):
        strRet = "";
        while not self.isEmpty():
            strRet = strRet + str(self.item.pop());
        return strRet;
