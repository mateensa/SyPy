# Description: This will check if each char in first string occurs in second, if yes then return true else false
# Solution: Check off each char in string with null value

def AnagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def AnagramSolution2(s1, s2):

    alist1 = list(s1);
    alist1.sort();
    alist2 = list(s2);
    alist2.sort();

    found = True;
    position = 0;
    while position < len(alist1)-1 and position < len(alist2)-1 and found :
        if not alist1[position] == alist2[position]:
            found = False;
        position+=1;
    return found;

#Solution3: we will first count the number of times each character occurs.
# Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character. Each time we see a particular character, we will increment the counter at that position.
# In the end, if the two lists of counters are identical, the strings must be anagrams



def AnagaramSolution3(s1, s2):

    c1 = [0]*26;
    c2 = [0]*26;

    for item in range(len(s1)):
        position = ord(s1[item])-ord('a');
        c1[position] = c1[position] + 1; # for counting no of repeated chars in c1, if no repetations then
                                         # we can simply assign it to 1
    for item in range(len(s2)):
        position = ord(s2[item])-ord('a');
        c2[position] = c2[position] + 1;

    isOk = True;
    index = 0;
    while index < len(c1) and isOk:
        isOk = False if c1[index] != c2[index] else True;
        index+=1;
    return isOk;

print(AnagaramSolution3("asdf", "fdsa"));