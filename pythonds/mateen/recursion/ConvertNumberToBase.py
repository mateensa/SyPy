__Author__ = "Mateen";
__Desc__   = "Convert any number to any base using recursion";


def convertDecimalToBase(num, base, remainder):

    if base == 2:
        baseString = "0 1".split();
    elif base == 10:
        baseString = "0 1 2 3 4 5 6 7 8 9".split();
    elif base == 16:
        baseString = "0 1 2 3 4 5 6 7 8 9 A B C D E F".split();
    else:
        baseString = None;
        raise RuntimeError("Error initializing base");
    if num < base:
        return baseString[num]+remainder;
    else:
        remainder = baseString[num%base] + remainder
        return convertDecimalToBase(num//base, base, remainder);

print(convertDecimalToBase(1453, 16, ""));












