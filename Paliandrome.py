
def checkPaliandrome(s1,s2):

    c1 = [0] * 26;
    c2 = [0] * 26;

    for item in range(len(s1)):
        value = ord(s1[item]) - ord('a');
        c1[item] = c1[item] + 1;

    for item in range(len(s2)):
        # value = ord(s2[item]) - ord('a');
        value = ord(s2[len(s2)-1-item]) - ord('a');
        c2[item] = c2[item] + 1;

    index = 0;
    found = False;
    while index < len(c1) and not found:
        if c1[index] != c2[index]:
            found = True;
            break;
        else:
            found = False;
        index+=1;
    return not found;

print(checkPaliandrome("mateena","neetama"))

# s3 = "dcba";
# for item in range(len(s3)):
#     print(s3[len(s3)-1-item]);