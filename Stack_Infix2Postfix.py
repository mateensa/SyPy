import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack.Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def evaluatePostfixExpression(exp):

    s = Stack.Stack()
    li = exp.split();
    for c in li:
        if c in "0123456789":
            s.push(c)
        else:
            left = s.pop();
            right = s.pop();
            value = calC(right, left, c)
            s.push(value);
    return int(s.pop());

def calC(operand1, operand2, operator):
    if operator == "+":
        return int(operand1) + int(operand2);
    elif operator == "-":
        return int(operand1) + int(operand2);
    elif operator == "*":
        return int(operand1) * int(operand2);
    else :
        return int(operand1) / int(operand2);


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(evaluatePostfixExpression("2 3 +"))
print(evaluatePostfixExpression('7 8 + 3 2 + /'))
print(evaluatePostfixExpression('17 10 + 3 * 9 / ==')); #  This needs to be implemented
