
def cumulativeSumSolution1(li):
    theSum = 0;
    for i in li:
        theSum = theSum + i;
    return theSum;

def cumulativeSumSolution2(li):
    if len(li) == 1:
        return li[0];
    else:
        return li[0] + cumulativeSumSolution2(li[1:])

print(cumulativeSumSolution1([100, 30, 10, 50]))
print(cumulativeSumSolution2([100, 30, 10, 50]))