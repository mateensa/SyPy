# Shakes

import random;


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = "";
    for i in range(strlen):
        res = res + alphabet[random.randrange(6)]
    return res;


def score(goal, teststring):
    numsame = 0;
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame = numsame + 1;
    return numsame / len(goal);


def main():
    goalstring = "mateen";
    best = 0;
    while True:
        newstring = generateOne(6);
        newscore = score(goalstring, newstring);
        if newscore >= 0.6:
            print(newscore, newstring);
            break;


main()
