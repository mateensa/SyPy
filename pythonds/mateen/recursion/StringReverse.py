__Author__ = "Mateen";
__Desc__   = "Reversing a string without using loops and check if its palindrome";


def stringReverse(astring):
    if len(astring) == 1:
        return astring;
    else:
        return astring[-1] + stringReverse(astring[:-1]);

def checkPalindrome(astring):
    return astring == stringReverse(astring);

print(checkPalindrome("kayak"));
print(checkPalindrome("aibohphobia"));
print(checkPalindrome("live not on evil"));
print(checkPalindrome("reviled did i live, said i, as evil i did deliver"));
print(checkPalindrome("go hang a salami; i’m a lasagna hog."));
print(checkPalindrome("able was i ere i saw elba"));
print(checkPalindrome("kanakanak"));
print(checkPalindrome("wassamassaw"));