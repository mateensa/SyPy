__author__ = "Mateen";
__descr__  = "Convert any number to any base using stack"

import Stack;

def decimalToBinary(decimalNumber):
    # decimalNumber = str(decimalNumber)
    s = Stack.Stack();

    while True and decimalNumber > 0 :
        remainder = decimalNumber % 2;
        s.push(remainder);
        decimalNumber = decimalNumber // 2;

    return s.getAllItemsReverse();

def BaseConvertor(decimalNumber, base):

    remainderStack = Stack.Stack();
    while decimalNumber > 0:
        # if decimalNumber == base:
        #     remainderStack.push(0);
        #     decimalNumber =0;
        # else:
        remainder = decimalNumber % base;
        remainderStack.push(remainder);
        decimalNumber = decimalNumber // base;

    baseString = None;

    if base == 16:
        baseString = "0123456789ABCDEF";

    if base == 8:
        baseString = "012345678";

    if base == 26:
        baseString = "0123456789abcdefghijklmnopqrstuvwxyz";

    retString = "";
    while not remainderStack.isEmpty():
        retString = retString + baseString[remainderStack.pop()];
    return retString;



print(decimalToBinary(25))
print(BaseConvertor(256,16))
print(BaseConvertor(25,8))
print(BaseConvertor(26,26))




